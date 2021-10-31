# Copyright (C) 2021 Ghostkeeper
# This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import collections  # For namedtuple.
import importlib.util  # To execute Python scripts to generate 3D models.
import json  # Screenshot instructions are stored in JSON format.
import math  # Rendering correct overhang angle.
import numpy  # To crop the screenshots.
import os  # To store temporary files.
import os.path  # To store temporary files.
import re  # To find the screenshot instructions.
import subprocess  # To call external applications to do conversions and optimisations for us.
import threading  # To multi-thread optimisation of the optimisation calls (which take a long time and are not always multi-threaded applications).
import time  # Crude way to make asynchronous calls synchronous: Spinlock until we get a signal that the asynchronous method is completed.
import typing
import PyQt5.QtGui  # For QImage, the result of the renders.

import cura.CuraApplication  # To change the settings before slicing.
import cura.Utils.Threading  # To render on the Qt thread.
import cura.Settings.SettingOverrideDecorator  # To add per-object settings to the loaded models.
import cura.XRayPass  # To render solid objects with their X-ray mode.
import UM.Backend.Backend  # To know when the slice has finished.
import UM.Logger
import UM.Math.AxisAlignedBox  # To calculate the centre of the scene for the camera to look at.
import UM.Math.Quaternion  # Rotating objects after loading them, correcting the camera orientation.
import UM.Math.Vector  # To move the camera and apply transformations.
import UM.Mesh.ReadMeshJob  # To load STL files to slice or take pictures of.
import UM.Operations.MirrorOperation  # Mirroring objects after loading them.
import UM.Operations.RotateOperation  # Rotating objects after loading them.
import UM.Operations.ScaleOperation  # Scaling objects after loading them.
import UM.Operations.TranslateOperation  # Moving objects after loading them.
import UM.Operations.SetTransformOperation  # Resetting objects' transformations after loading them.
import UM.Resources  # To store converted OpenSCAD documents long-term.
import UM.Scene.Iterator.DepthFirstIterator  # To find the layer view data and meshes to transform.
import UM.Scene.Selection  # To clear the selection before taking screenshots.
import UM.Settings.SettingInstance  # To add per-object settings to the loaded models.
import UM.View.GL.OpenGL  # To load the shaders to render screenshots with.

"""
This module provides an automatic way to generate screenshots for the Settings Guide.
It is not supplied with the actual Settings Guide package.

The goals of this tool are:
* To have a canonical way to create screenshots, ensuring that the look and feel is consistent.
* To be able to re-create screenshots automatically, if Cura changes something in the way that their scene looks.
* To ensure that screenshots are compressed properly.
* To allow external contributors to define screenshots through code.

The process of creating these screenshots is very complex! It involves several stages and has a bunch of
dependencies. The dependencies that need to be installed to create the screenshots are:
* Linux: The tool is only designed to work on Linux at the moment.
* OpenSCAD: After downloading the 3D model files, they are compiled with OpenSCAD to STL files that Cura can read.
* ImageMagick: Used to reduce colour depth and to combine screenshots into GIF animations.
* OptiPNG: To pre-process for optimising PNG files.
* Efficient-Compression-Tool: To refine optimisation of PNG files.
* FlexiGIF: To optimise GIF files.

Most of these dependencies can be installed on Ubuntu by running:
`sudo apt install openscad imagemagick optipng`
Efficient-Compression-Tool has to be compiled separately from source. It can be found here:
https://github.com/fhanau/Efficient-Compression-Tool
FlexiGIF is not available from Apt either but can be downloaded as separate application here:
https://create.stephan-brumme.com/flexigif-lossless-gif-lzw-optimization/

The tool is available by setting the preference "settings_guide/screenshot_tool" to True. A button will then be
visible on every article. When pressed, it will re-create the images for that article. A button will also be present
on the landing page that will re-create ALL images. This takes a long time!
"""

# These are several system commands we can execute to perform various tasks using external tools.
commands = {
	"openscad": ["openscad", "-o", "{output}", "{input}"],  # Compile an OpenSCAD file.
	"reduce_palette": ["convert", "-colors", "{colours}", "+dither", "{input}", "{output}"],  # Reduce colour palette of an image.
	"optimise_png1": ["optipng", "-o7", "-strip", "all", "-snip", "-out", "{output}", "{input}"],
	"optimise_png2": ["ect", "-9", "-strip", "--pal_sort=16", "--allfilters", "{output}"],  # Reduce file size of PNG images.
	"merge_gif": ["convert", "-delay", "{delay}", "-loop", "0", "-background", "white", "-alpha", "remove", "-layers", "Optimize", "{inputs}", "{output}"],  # Merge multiple images into a GIF.
	"optimise_gif": ["flexigif", "-f", "{input}", "{output}"]  # Reduce file size of GIF images.
}
render_width = 2524
render_height = 1376

def call_with_args(command, **kwargs) -> None:
	"""
	Call a command with specified arguments.
	:param command: The key of the command to call (from the `commands` dictionary above).
	:param kwargs: Key-word arguments to format the command's arguments with.
	"""
	args = []
	for arg in commands[command]:
		args.append(arg.format(**kwargs))
	UM.Logger.Logger.info("Subprocess: " + " ".join(args))
	subprocess.call(args)

ScreenshotInstruction = collections.namedtuple("ScreenshotInstruction", ["image_path", "models", "camera_position", "camera_lookat", "minimum_layer", "layer", "line", "colour_scheme", "structures", "settings", "colours", "delay"])
ModelInstruction = collections.namedtuple("ModelInstruction", ["script", "scad_params", "transformation", "object_settings"])
"""
All the information needed to take a screenshot.
* image_path: The filename of the image to refresh in the articles/images folder.
* models: The 3D models to showcase. This is a list of the 3D models. Each model is a ModelInstruction with the
  following parameters:
  - script: The file name of the script to generate this 3D model, in the models folder.
  - scad_params: A list of OpenSCAD parameters to generate the model with. Each should be of the form key=value and in a
    separate string in the list. Only applicable for OpenSCAD scripts.
  - transformation: A list of transformations to apply to the model, in order. Implemented transformations are:
    mirrorX(), mirrorY(), mirrorZ(), scale(ratio), scaleX(ratio), scaleY(ratio), scaleZ(ratio), rotateX(angle),
    rotateY(angle), rotateZ(angle), translateX(dist), translateY(dist), translateZ(dist).
  - object_settings: A dictionary of setting keys and values to slice this object with. These can only be per-object
    settings. String setting values can use the key "{root}" to use the path to the plug-in directory.
* camera_position: The X, Y and Z position of the camera (as list).
* camera_lookat: The X, Y and Z position of the camera focus centre. If not specified, look at the centre of the scene.
* minimum_layer: The lowest layer number to display. The bottom part of the range. Can be used to cut off the first
  layer to aid in how the image is cut if the travel moves are included. Use a list to define an animation.
* layer: The layer number to look at. Use layer -1 to not use layer view. Use a list to define an animation.
* line: The number of lines to show on the current layer. Use -1 to view the entire layer. Use a list to define an
  animation.
* colour_scheme: The layer view colour scheme to use. Choose from: line_type, material_colour, speed, layer_thickness,
  line_width.
* structures: List of structures which are visible in layer view. Choose from: travels, helpers, shell, infill, starts.
* settings: A dictionary of setting keys and values to slice the object with. These can be global or per-extruder
  settings. Per-extruder settings are applied to all extruders, unless they are prefixed with "[#]", the extruder number
  in brackets. String setting values can use the key "{root}" to use the path to the plug-in directory.
* colours: The colour depth of the resulting image. Reduce colours to reduce file size. Max 256.
* delay: If this is an animation, the delay between consecutive images in milliseconds. Default 500.
"""

def refresh_screenshots(article_text, refreshed_set) -> None:
	"""
	Refresh the screenshots nested in the selected article text.

	This function serves as glue code and an overview of the stages through which we go in order to refresh the
	screenshots.
	:param article_text: The text containing embedded screenshots to refresh.
	:param refreshed_set: Set of images that have already been refreshed and don't need to be refreshed this pass if
	encountered.
	"""
	for screenshot_instruction in find_screenshots(article_text):
		if screenshot_instruction.image_path in refreshed_set:
			continue  # Has already been refreshed. Don't refresh again.

		setup_printer(screenshot_instruction.settings)
		for model in screenshot_instruction.models:
			stl_path = convert_model(model.script, model.scad_params)
			load_model(stl_path, model.transformation, model.object_settings)

		layers = screenshot_instruction.layer
		if type(layers) != list:  # To simplify processing, always use lists for the layer, line and minimum layer, pretending it's always an animation.
			layers = [layers]
		lines = screenshot_instruction.line
		if type(lines) != list:
			lines = [lines]
		minimum_layers = screenshot_instruction.minimum_layer
		if type(minimum_layers) != list:
			minimum_layers = [minimum_layers]
		num_screenshots = max(len(layers), len(lines), len(minimum_layers))
		# Make the lines, layers and minimum layers equally long by repeating some of them.
		while len(layers) < num_screenshots:
			layers *= 2
		while len(layers) > num_screenshots:
			layers.pop()
		while len(lines) < num_screenshots:
			lines *= 2
		while len(lines) > num_screenshots:
			lines.pop()
		while len(minimum_layers) < num_screenshots:
			minimum_layers *= 2
		while len(minimum_layers) > num_screenshots:
			minimum_layers.pop()

		is_animation = len(layers) > 1
		if layers[0] >= 0:
			slice_scene()

		full_image_path = os.path.join(os.path.dirname(__file__), "resources", "articles", "images", screenshot_instruction.image_path)

		# Track saved images in case we're making multiple that need to be combined into a GIF later.
		saved_images = []
		index = 0
		for layer, line, minimum_layer in zip(layers, lines, minimum_layers):
			is_layer_view = layer >= 0
			if is_layer_view:
				switch_to_layer_view(screenshot_instruction.colour_scheme, screenshot_instruction.structures)
				navigate_layer_view(minimum_layer, layer, line)
			else:  # Need to show the model itself.
				switch_to_solid_view()
			screenshot = None
			while screenshot is None:
				screenshot = take_snapshot(screenshot_instruction.camera_position, screenshot_instruction.camera_lookat, is_layer_view)
				time.sleep(1.5)
			if not is_animation:
				target_file = full_image_path
			else:
				target_file = full_image_path + str(index) + ".png"
			saved_images.append((screenshot, target_file))
			index += 1

		saved_images = crop_images(saved_images)  # Crop all frames at once, to get the same cropping region and correctly align all frames of an animation.

		for screenshot, target_file in saved_images:
			save_screenshot(screenshot, target_file)

		if is_animation:
			combine_animation([fname for _, fname in saved_images], full_image_path, screenshot_instruction.colours, screenshot_instruction.delay)
			optimise_gif(full_image_path)
			for _, filename in saved_images:
				os.remove(filename)
		else:
			reduce_colours(full_image_path, screenshot_instruction.colours)
			optimise_png(full_image_path)

		refreshed_set.add(screenshot_instruction.image_path)

def find_screenshots(article_text) -> typing.Generator[ScreenshotInstruction, None, None]:
	"""
	Finds the screenshot instructions and parses them to ScreenshotInstruction instances, so that the rest of the
	module may more easily process them and refresh screenshots.
	:param article_text: The article to find screenshots in, Markdown-formatted.
	:return: A sequence of ScreenshotInstruction instances.
	"""
	screenshot_regex = re.compile(r"<!--screenshot\s*({.*?})\s*-->", re.DOTALL)
	for match in re.finditer(screenshot_regex, article_text):
		json_serialised = match.group(1)
		print("--------- SCREENSHOT -----------\n" + json_serialised + "\n--------------------------------")
		json_document = json.loads(json_serialised)
		yield ScreenshotInstruction(
			image_path=json_document["image_path"],
			models=[ModelInstruction(
				script=model["script"],
				scad_params=model.get("scad_params", []),
				transformation=model.get("transformation", []),
				object_settings=model.get("object_settings", {})
			) for model in json_document["models"]],
			camera_position=json_document["camera_position"],
			camera_lookat=json_document.get("camera_lookat"),  # If None, look at the centre of the scene.
			minimum_layer=json_document.get("minimum_layer", 0),
			layer=json_document.get("layer", 99999),
			line=json_document.get("line", -1),
			colour_scheme=json_document.get("colour_scheme", "line_type"),
			structures=json_document.get("structures", ["helpers", "shell", "infill", "starts"]),
			settings=json_document.get("settings", {}),
			colours=json_document.get("colours", 256),
			delay=json_document.get("delay", 500)
		)
	return

@cura.Utils.Threading.call_on_qt_thread  # Must be called from the Qt thread because it creates QML objects (the global stack).
def setup_printer(settings) -> None:
	"""
	Set up a Cura printer and set the settings as desired in the screenshot instruction.

	This makes sure that the model will be sliced with the correct settings.
	:param settings: The settings to slice the model with, as a dictionary of setting keys to setting values.
	"""
	application = cura.CuraApplication.CuraApplication.getInstance()
	registry = application.getContainerRegistry()
	machine_manager = application.getMachineManager()

	# Clear the build plate.
	application.deleteAll()

	# Some global preferences that we need for this tool.
	preferences = application.getPreferences()
	preferences.setValue("general/camera_perspective_mode", "perspective")
	preferences.setValue("physics/automatic_push_free", "False")

	# Create a printer if necessary and activate it if necessary.
	settings_guide_printer = registry.findContainerStacksMetadata(name="Settings Guide Printer")
	if settings_guide_printer:
		if machine_manager.activeMachine.getId() != settings_guide_printer[0]["id"]:  # Added, but not active yet.
			machine_manager.setActiveMachine(settings_guide_printer[0]["id"])
	else:  # There is no printer yet. Create one.
		machine_manager.addMachine("custom", name="Settings Guide Printer")

	# Restore the printer to a certain baseline.
	machine_manager.setActiveMachineExtruderCount(4)
	printer = machine_manager.activeMachine
	blue_pla = registry.findInstanceContainers(id="ultimaker_pla_blue")[0]
	red_pla = registry.findInstanceContainers(id="ultimaker_pla_red")[0]
	white_pla = registry.findInstanceContainers(id="ultimaker_pla_white")[0]
	printer.extruderList[1].setMaterial(blue_pla)
	printer.extruderList[2].setMaterial(red_pla)
	printer.extruderList[3].setMaterial(white_pla)
	printer.definitionChanges.setProperty("machine_width", "value", "1000")
	printer.definitionChanges.setProperty("machine_height", "value", "1000")
	printer.definitionChanges.setProperty("machine_depth", "value", "1000")
	for extruder_nr in range(4):
		printer.extruderList[extruder_nr].userChanges.clear()
	printer.userChanges.clear()

	# Some defaults that we'll want for most screenshots to make them look good. Remove distractions.
	printer.userChanges.setProperty("layer_height", "value", "0.06")  # Reducing layer height makes the sides look smoother. This improves compression but also reduces distraction from the layer lines.
	printer.userChanges.setProperty("adhesion_type", "value", "none")  # Except for settings concerning bed adhesion, remove adhesion type to remove distraction from the actual object.
	printer.userChanges.setProperty("z_seam_type", "value", "back")  # Seam alignment to "User Specified" to align the seam. This makes the seam more recognisable as such, and allows us to find a camera angle that hides it if necessary.
	printer.userChanges.setProperty("z_seam_position", "value", "backleft")  # In case of axis-aligned models (which is pretty common) this puts the seam in a corner rather than spreading it out over a side.

	# Set the settings that we want to override for this slice.
	specific_extruder_setting = re.compile(r"\[(\d)](.+)")
	for key, value in settings.items():
		if type(value) is str:
			value = value.format(root=os.path.dirname(__file__))
		is_specific_extruder = re.match(specific_extruder_setting, key)
		if is_specific_extruder:
			extruder_nr = int(is_specific_extruder.group(1))
			actual_key = is_specific_extruder.group(2)
			printer.extruderList[extruder_nr].userChanges.setProperty(actual_key, "value", value)
		else:
			# Just set it anywhere without really checking whether it's per-extruder or whatever.
			for extruder_nr in range(4):
				printer.extruderList[extruder_nr].userChanges.setProperty(key, "value", value)
			printer.userChanges.setProperty(key, "value", value)

def convert_model(script_path, scad_params) -> str:
	"""
	Use an OpenSCAD or Python script to generate a 3D model.

	The STL model will be saved in a temporary file.
	:param script_path: A path to an OpenSCAD model file.
	:param scad_params: A list of parameters to pass to OpenSCAD scripts, of the form "key=value".
	:return: A path to an STL model file.
	"""
	script_path = os.path.join(os.path.dirname(__file__), "resources", "models", script_path)
	file_name = os.path.splitext(os.path.basename(script_path))[0]
	stl_dir = os.path.join(UM.Resources.Resources.getDataStoragePath(), "settings_guide_screenshots")
	if not os.path.exists(stl_dir):
		os.mkdir(stl_dir)
	stl_path = os.path.join(stl_dir, ",".join([file_name] + scad_params) + ".stl")
	if not os.path.exists(stl_path):
		extension = os.path.splitext(script_path)[1]
		if extension == ".scad":
			if not scad_params:
				call_with_args("openscad", input=script_path, output=stl_path)
			else:  # Insert OpenSCAD parameters in the command.
				args = []
				for arg in commands["openscad"]:
					args.append(arg.format(input=script_path, output=stl_path))
				for param in scad_params:
					args.insert(-1, "-D")
					args.insert(-1, param)
				UM.Logger.Logger.info("Subprocess: " + " ".join(args))
				subprocess.call(args)
		elif extension == ".py":
			spec = importlib.util.spec_from_file_location(file_name, script_path)
			generator = spec.loader.load_module(file_name)
			generator.generate(stl_path)
	return stl_path

def load_model(stl_path, transformations, object_settings) -> None:
	"""
	Load a 3D model into the scene to take a screenshot of.
	:param stl_path: A path to an STL model to load.
	:param transformations: A list of transformation commands to apply to the model.
	:param object_settings: A dictionary of key-value pairs for per-object settings to apply to the model.
	"""
	application = cura.CuraApplication.CuraApplication.getInstance()
	application._currently_loading_files.append(stl_path)
	job = UM.Mesh.ReadMeshJob.ReadMeshJob(stl_path, add_to_recent_files=False)
	job.run()  # Don't plan it in on the job queue or anything. Actually run it on this thread.
	mesh_data = [node.getMeshData() for node in job.getResult()]  # Find the nodes by finding their mesh data in the scene after _readMeshFinished is done with them, since that re-creates the nodes.
	application._readMeshFinished(job)  # Abuse CuraApplication's implementation to properly put the model on the build plate.
	time.sleep(2)  # Wait for scene node update triggers to be processed.

	# Apply transformations and per-object settings to the resulting mesh.
	for node in UM.Scene.Iterator.DepthFirstIterator.DepthFirstIterator(application.getController().getScene().getRoot()):
		if not node.isSelectable():
			continue
		if not node.getMeshData():
			continue
		if node.getMeshData() not in mesh_data:  # This node was not part of the models just loaded.
			continue

		# First move the object to the 0,0 position and undo its rotation, in case it was moved by the arranger.
		reset_operation = UM.Operations.SetTransformOperation.SetTransformOperation(node, UM.Math.Vector.Vector(0, 0, 0), UM.Math.Quaternion.Quaternion(), UM.Math.Vector.Vector(1, 1, 1))
		reset_operation.push()

		for transformation in transformations:
			transformation = transformation.lower()
			if transformation.startswith("mirrorx"):
				operation = UM.Operations.MirrorOperation.MirrorOperation(node, UM.Math.Vector.Vector(-1, 1, 1), mirror_around_center=True)
			elif transformation.startswith("mirrory"):
				operation = UM.Operations.MirrorOperation.MirrorOperation(node, UM.Math.Vector.Vector(1, 1, -1), mirror_around_center=True)
			elif transformation.startswith("mirrorz"):
				operation = UM.Operations.MirrorOperation.MirrorOperation(node, UM.Math.Vector.Vector(1, -1, 1), mirror_around_center=True)
			elif transformation.startswith("scale(") and transformation.endswith(")"):
				scale_factor = float(transformation[len("scale("):-len(")")])
				operation = UM.Operations.ScaleOperation.ScaleOperation(node, UM.Math.Vector.Vector(scale_factor, scale_factor, scale_factor))
			elif transformation.startswith("scalex(") and transformation.endswith(")"):
				scale_factor = float(transformation[len("scalex("):-len(")")])
				operation = UM.Operations.ScaleOperation.ScaleOperation(node, UM.Math.Vector.Vector(scale_factor, 1, 1))
			elif transformation.startswith("scaley(") and transformation.endswith(")"):
				scale_factor = float(transformation[len("scaley("):-len(")")])
				operation = UM.Operations.ScaleOperation.ScaleOperation(node, UM.Math.Vector.Vector(1, 1, scale_factor))
			elif transformation.startswith("scalez(") and transformation.endswith(")"):
				scale_factor = float(transformation[len("scalez("):-len(")")])
				operation = UM.Operations.ScaleOperation.ScaleOperation(node, UM.Math.Vector.Vector(1, scale_factor, 1))
			elif transformation.startswith("rotatex(") and transformation.endswith(")"):
				angle = float(transformation[len("rotatex("):-len(")")]) / 180 * math.pi
				rotation = UM.Math.Quaternion.Quaternion.fromAngleAxis(angle, UM.Math.Vector.Vector.Unit_X)
				operation = UM.Operations.RotateOperation.RotateOperation(node, rotation, rotate_around_point=node.getPosition())
			elif transformation.startswith("rotatey(") and transformation.endswith(")"):
				angle = float(transformation[len("rotatey("):-len(")")]) / 180 * math.pi
				rotation = UM.Math.Quaternion.Quaternion.fromAngleAxis(angle, UM.Math.Vector.Vector.Unit_Z)
				operation = UM.Operations.RotateOperation.RotateOperation(node, rotation, rotate_around_point=node.getPosition())
			elif transformation.startswith("rotatez(") and transformation.endswith(")"):
				angle = float(transformation[len("rotatez("):-len(")")]) / 180 * math.pi
				rotation = UM.Math.Quaternion.Quaternion.fromAngleAxis(angle, UM.Math.Vector.Vector.Unit_Y)
				operation = UM.Operations.RotateOperation.RotateOperation(node, rotation, rotate_around_point=node.getPosition())
			elif transformation.startswith("translatex(") and transformation.endswith(")"):
				distance = float(transformation[len("translatex("):-len(")")])
				operation = UM.Operations.TranslateOperation.TranslateOperation(node, UM.Math.Vector.Vector(distance, 0, 0))
			elif transformation.startswith("translatey(") and transformation.endswith(")"):
				distance = float(transformation[len("translatey("):-len(")")])
				operation = UM.Operations.TranslateOperation.TranslateOperation(node, UM.Math.Vector.Vector(0, 0, distance))
			elif transformation.startswith("translatez(") and transformation.endswith(")"):
				distance = float(transformation[len("translatez("):-len(")")])
				operation = UM.Operations.TranslateOperation.TranslateOperation(node, UM.Math.Vector.Vector(0, distance, 0))
			else:
				continue  # Unknown transformation.
			operation.push()
		for key, value in object_settings.items():  # Add the per-object settings.
			stack = node.callDecoration("getStack")
			if not stack:
				node.addDecorator(cura.Settings.SettingOverrideDecorator.SettingOverrideDecorator())
				stack = node.callDecoration("getStack")
			if key == "extruder_nr":  # Extruder index gets special handling.
				extruder_id = application.getExtruderManager().getExtruderStack(value).getId()
				node.callDecoration("setActiveExtruder", extruder_id)
				continue
			container = stack.getTop()
			definition = stack.getSettingDefinition(key)
			new_instance = UM.Settings.SettingInstance.SettingInstance(definition, container)
			if type(value) is str:
				value = value.format(root=os.path.dirname(__file__))
			new_instance.setProperty("value", value)
			container.addInstance(new_instance)

	UM.Scene.Selection.Selection.clear()  # If the preference was enabled to auto-select objects, clear selection.
	time.sleep(2)  # Wait for scene node update triggers to be processed.

def slice_scene() -> None:
	"""
	Trigger a slice, so that we can show layer view in the screenshot.
	"""
	application = cura.CuraApplication.CuraApplication.getInstance()
	backend = application.getBackend()

	while True:
		print("------------- (re)starting engine for slice")
		backend.slice()
		time.sleep(2)  # Give stuff some time to spin up.

		# Now do a spinloop, blocking this thread until the slice is completed.
		while backend._process:
			time.sleep(1.2)
			if backend._backend_state == UM.Backend.Backend.BackendState.Error:
				break  # Restart the slice.
		else:
			break

	time.sleep(2)  # Give stuff some time to wind down.


def switch_to_layer_view(colour_scheme, visible_structures) -> None:
	"""
	Show layer view in the screenshot.
	:param colour_scheme: The colour scheme to use for this layer view.
	:param visible_structures: Which parts of the layer view should be made visible.
	"""
	colour_schemes = ["material_colour", "line_type", "speed", "layer_thickness", "line_width"]  # In order in which they appear, so that we can find the correct index to set the preference to.
	application = cura.CuraApplication.CuraApplication.getInstance()
	application.getController().setActiveStage("PreviewStage")
	preferences = application.getPreferences()
	preferences.setValue("layerview/layer_view_type", colour_schemes.index(colour_scheme))
	preferences.setValue("layerview/show_travel_moves", "travels" in visible_structures)
	preferences.setValue("layerview/show_helpers", "helpers" in visible_structures)
	preferences.setValue("layerview/show_skin", "shell" in visible_structures)
	preferences.setValue("layerview/show_infill", "infill" in visible_structures)
	preferences.setValue("layerview/show_starts", "starts" in visible_structures)

	layer_view_completed = False
	while not layer_view_completed:
		for node in UM.Scene.Iterator.DepthFirstIterator.DepthFirstIterator(cura.CuraApplication.CuraApplication.getInstance().getController().getScene().getRoot()):
			if node.callDecoration("getLayerData"):
				layer_view_completed = True
		time.sleep(1.2)

def navigate_layer_view(minimum_layer_nr, layer_nr, line_nr) -> None:
	"""
	Set the layer slider and line slider to the correct positions for the screenshot.
	:param minimum_layer_nr: The lower range of the layer number to show on the screenshot.
	:param layer_nr: The layer number to show on the screenshot.
	:param line_nr: The line to show on the screenshot. Use 0 to show the entire layer.
	"""
	layer_view_plugin = cura.CuraApplication.CuraApplication.getInstance().getPluginRegistry().getPluginObject("SimulationView")
	layer_view_plugin.setLayer(layer_nr - 1)
	layer_view_plugin.setMinimumLayer(minimum_layer_nr)
	if line_nr >= 0:
		layer_view_plugin.setPath(1)  # Due to a bug in layer view, setting the line sometimes makes it display the entire layer.
		time.sleep(1.2)
		layer_view_plugin.setPath(line_nr)
		layer_view_plugin.setMinimumPath(0)

def switch_to_solid_view() -> None:
	"""
	Show solid view in the screenshot.
	"""
	cura.CuraApplication.CuraApplication.getInstance().getController().setActiveStage("PrepareStage")

@cura.Utils.Threading.call_on_qt_thread  # Must be called from the Qt thread because the OpenGL bindings don't support multi-threading.
def take_snapshot(camera_position, camera_lookat, is_layer_view) -> typing.Optional[PyQt5.QtGui.QImage]:
	"""
	Take a snapshot of the current scene.
	:param camera_position: The position of the camera to take the snapshot with.
	:param camera_lookat: The position of the focal point of the camera.
	:param is_layer_view: Whether we're looking at layer view or the model itself.
	:return: A screenshot of the current scene.
	"""
	application = cura.CuraApplication.CuraApplication.getInstance()
	plugin_registry = application.getPluginRegistry()

	# Set the camera to the desired position. We'll use the actual camera for the snapshot just because it looks cool while it's busy.
	camera = application.getController().getScene().getActiveCamera()
	camera.setPosition(UM.Math.Vector.Vector(camera_position[0], camera_position[2], camera_position[1]))  # Note that these are OpenGL coordinates, swapping Y and Z.
	if not camera_lookat:
		bounding_box = UM.Math.AxisAlignedBox.AxisAlignedBox()
		for node in UM.Scene.Iterator.DepthFirstIterator.DepthFirstIterator(cura.CuraApplication.CuraApplication.getInstance().getController().getScene().getRoot()):
			if node.isSelectable():
				bounding_box = bounding_box + node.getBoundingBox()
		camera_lookat = bounding_box.center
	else:
		camera_lookat = UM.Math.Vector.Vector(camera_lookat[0], camera_lookat[2], camera_lookat[1])
	camera.lookAt(camera_lookat)
	if abs(camera.getPosition().x - camera_lookat.x) < 0.01 and abs(camera.getPosition().z - camera_lookat.z) < 0.01:  # Looking straight up or straight down.
		# Make sure the yaw of the camera is consistent regardless of previous position.
		if camera.getPosition().y > camera_lookat.y:
			camera.setOrientation(UM.Math.Quaternion.Quaternion(-2, 0, 0, 2))
		else:
			camera.setOrientation(UM.Math.Quaternion.Quaternion(2, 0, 0, 2))
	time.sleep(2)  # Some time to update the scene nodes. Don't know if this is necessary but it feels safer.

	# Use a transparent background.
	gl_bindings = UM.View.GL.OpenGL.OpenGL.getInstance().getBindingsObject()
	gl_bindings.glClearColor(0.0, 0.0, 0.0, 0.0)
	gl_bindings.glClear(gl_bindings.GL_COLOR_BUFFER_BIT | gl_bindings.GL_DEPTH_BUFFER_BIT)

	if is_layer_view:
		# Remove any nozzle node. It can get in the way of what we want to see and influence cropping of the image badly.
		simulation_view_plugin = plugin_registry.getPluginObject("SimulationView")
		for node in UM.Scene.Iterator.DepthFirstIterator.DepthFirstIterator(application.getController().getScene().getRoot()):
			if hasattr(node, "_createNozzleMesh"):  # This node is a NozzleNode (the actual class is not exposed to us outside the plug-in).
				node.getParent().removeChild(node)

		render_pass = simulation_view_plugin.getSimulationPass()
		render_pass.render()
		time.sleep(1.2)
		screenshot = render_pass.getOutput()
		print("---- screenshot size:", screenshot.width(), "x", screenshot.height())
		if screenshot.width() != render_width or screenshot.height() != render_height:
			print("---- render output not correct size! Resizing window to compensate.")
			main_window = application.getMainWindow()
			delta_width = render_width - screenshot.width()
			delta_height = render_height - screenshot.height()
			main_window.setWidth(main_window.width() + delta_width)
			main_window.setHeight(main_window.height() + delta_height)
			return None  # Failed to render. Try again after waiting outside of Qt thread.

		# Remove alpha channel from this picture. We don't want the semi-transparent support since we don't draw the object outline here.
		# Sadly, QImage.convertToFormat has only 2 formats with boolean alpha and they both premultiply. So we'll go the hard way: Through Numpy.
		pixel_bits = screenshot.bits().asarray(screenshot.byteCount())
		pixels = numpy.frombuffer(pixel_bits, dtype=numpy.uint8).reshape([screenshot.height(), screenshot.width(), 4])
		opaque = numpy.nonzero(pixels[:, :, 0])
		pixels[opaque[0], opaque[1], 3] = 255
		return PyQt5.QtGui.QImage(pixels.data, pixels.shape[1], pixels.shape[0], PyQt5.QtGui.QImage.Format_ARGB32).copy()  # Make a copy because the pixel data will go out of scope for Numpy, so that would be invalid memory.
	else:  # Render the objects themselves! Going to be quite complex here since the render is highly specialised in what it shows and what it doesn't.
		view = plugin_registry.getPluginObject("SolidView")
		view._checkSetup()
		renderer = view.getRenderer()

		support_angle = application.getGlobalContainerStack().getProperty("support_angle", "value")
		view._enabled_shader.setUniformValue("u_overhangAngle", math.cos(math.radians(90 - support_angle)))  # Correct overhang angle.
		view._enabled_shader.setUniformValue("u_lowestPrintableHeight", -1.0)  # Don't show initial layer height.
		object_batch = renderer.createRenderBatch(shader=view._enabled_shader)
		renderer.addRenderBatch(object_batch)
		for node in UM.Scene.Iterator.DepthFirstIterator.DepthFirstIterator(application.getController().getScene().getRoot()):
			if not node.getMeshData() or not node.isSelectable():
				continue
			uniforms = {}

			# Get the object's colour.
			extruder_index = int(node.callDecoration("getActiveExtruderPosition"))
			material_color = application.getExtrudersModel().getItem(extruder_index)["color"]
			uniforms["diffuse_color"] = [
				int(material_color[1:3], 16) / 255,
				int(material_color[3:5], 16) / 255,
				int(material_color[5:7], 16) / 255,
				1.0
			]

			# Render with special shaders for special types of meshes, or otherwise in the normal batch.
			if node.callDecoration("isNonPrintingMesh") and (node.callDecoration("isInfillMesh") or node.callDecoration("isCuttingMesh")):
				renderer.queueNode(node, shader=view._non_printing_shader, uniforms=uniforms, transparent=True)
			elif node.callDecoration("isSupportMesh"):
				uniforms["diffuse_color_2"] = [
					uniforms["diffuse_color"][0] * 0.6,
					uniforms["diffuse_color"][1] * 0.6,
					uniforms["diffuse_color"][2] * 0.6,
					1.0
				]
				renderer.queueNode(node, shader=view._support_mesh_shader, uniforms=uniforms)
			else:
				object_batch.addItem(node.getWorldTransformation(copy=False), node.getMeshData(), uniforms=uniforms, normal_transformation=node.getCachedNormalMatrix())

		default_pass = renderer.getRenderPass("default")
		default_pass.render()
		time.sleep(1.2)
		normal_shading = default_pass.getOutput()
		xray_pass = renderer.getRenderPass("xray")
		renderer.addRenderPass(xray_pass)
		xray_pass.render()
		time.sleep(1.2)
		xray_shading = xray_pass.getOutput()

		# Manually composite these shadings. Because the composite shader also adds a background colour.
		normal_data = normal_shading.bits().asarray(normal_shading.byteCount())
		composite_pixels = numpy.frombuffer(normal_data, dtype=numpy.uint8).reshape([normal_shading.height(), normal_shading.width(), 4])  # Start from the normal image.
		colours = numpy.true_divide(composite_pixels[:, :, 0:3], 255)  # Scaled to [0, 1].
		alpha = numpy.true_divide(composite_pixels[:, :, 3], 255)
		xray_data = xray_shading.bits().asarray(xray_shading.byteCount())
		xray_pixels = numpy.frombuffer(xray_data, dtype=numpy.uint8).reshape([xray_shading.height(), xray_shading.width(), 4])
		xray_pixels = numpy.mod(xray_pixels[:, :, 0:3], 10) // 5  # The X-ray shader creates increments of 5 for some reason. If there are an odd number of increments (not divisible by 10) then it must be highlighted.
		hue_shift = ((alpha - 0.333) * 6.2831853)
		cos_shift = numpy.repeat(numpy.expand_dims(numpy.cos(-hue_shift), axis=2), 3, axis=2)
		sin_shift = numpy.repeat(numpy.expand_dims(numpy.sin(-hue_shift), axis=2), 3, axis=2)
		k = numpy.array([0.57735, 0.57735, 0.57735])  # 1/sqrt(3), resulting in a diagonal unit vector around which we rotate the channels.
		cross_colour = numpy.cross(colours, k) * -1
		dot_colour = numpy.repeat(numpy.expand_dims(numpy.dot(colours, k), axis=2), 3, axis=2)
		rotated_hue = colours * cos_shift + cross_colour * sin_shift + (cos_shift * -1 + 1.0) * dot_colour * k  # Rodrigues' rotation formula!
		rotated_hue = rotated_hue * 255

		composite_pixels[:, :, 0:3] -= composite_pixels[:, :, 0:3] * xray_pixels  # Don't use the normal colour for x-rayed pixels.
		composite_pixels[:, :, 0:3] += (rotated_hue * xray_pixels).astype("uint8")  # Use the rotated colour instead.
		composite_pixels[:, :, 3][alpha > 0.1] = 255
		return PyQt5.QtGui.QImage(composite_pixels.data, composite_pixels.shape[1], composite_pixels.shape[0], PyQt5.QtGui.QImage.Format_ARGB32).copy()  # Make a copy because the pixel data will go out of scope for Numpy, so that would be invalid memory.

def crop_images(images) -> typing.List[typing.Tuple[PyQt5.QtGui.QImage, str]]:
	"""
	Crop a list of images to eliminate any transparent borders.

	All images will be cropped to the same dimensions and the same region of the original snapshots. This makes sure
	that nothing will get cropped off any frame and all frames are correctly aligned with each other.

	The images will be cropped in-place.
	:param images: A list of tuples of images and their filenames.
	:return: A new list of cropped images and their filenames.
	"""
	min_x = images[0][0].width()
	min_y = images[0][0].height()
	max_x = 0
	max_y = 0

	# Find the cropping dimensions that work for all images.
	for image, _ in images:
		pixel_data = image.bits().asarray(image.byteCount())
		numpy_pixels = numpy.frombuffer(pixel_data, dtype=numpy.uint8).reshape([image.height(), image.width(), 4])
		opaque_pixels = numpy.nonzero(numpy_pixels)
		image_min_y, image_min_x, _ = numpy.amin(opaque_pixels, axis=1)
		image_max_y, image_max_x, _ = numpy.amax(opaque_pixels, axis=1)
		min_x = min(image_min_x, min_x)
		min_y = min(image_min_y, min_y)
		max_x = max(image_max_x, max_x)
		max_y = max(image_max_y, max_y)

	# Crop each image to the same dimensions.
	result = []
	for image, filename in images:
		result.append((image.copy(min_x, min_y, max_x - min_x, max_y - min_y), filename))

	return result

def save_screenshot(screenshot, image_path) -> None:
	"""
	Save the screenshot to file in the plug-in folder.
	:param screenshot: The image to save to the file.
	:param image_path: The file path to store the screenshot in.
	"""
	screenshot.save(image_path)

def combine_animation(frames, image_path, colours, delay) -> None:
	"""
	Combine the frames of an animation into a GIF file.
	:param frames: A list of PNG files storing the frames of the animation, in order.
	:param image_path: The path to the GIF file to store.
	:param colours: The number of colours to use in the palette of the GIF.
	:param delay: The duration to show each frame, in milliseconds.
	"""
	args = []
	for arg in commands["merge_gif"]:
		if arg == "{inputs}":
			args.extend(frames)  # Frames need to be supplied as individual arguments.
		else:
			args.append(arg.format(delay=round(delay / 10.0), output=image_path))
	UM.Logger.Logger.info("Subprocess: " + " ".join(args))
	subprocess.call(args)
	reduce_colours(image_path, colours)

def optimise_gif(image_path) -> None:
	"""
	Do a compression optimisation on a GIF file.
	:param image_path: A path to the GIF file to optimise.
	"""
	def optimise_threaded():
		call_with_args("optimise_gif", input=image_path, output=image_path + ".opt.gif")
		os.remove(image_path)
		os.rename(image_path + ".opt.gif", image_path)
	thread = threading.Thread(target=optimise_threaded)
	thread.start()  # Fire and forget.

def reduce_colours(image_path, colours) -> None:
	"""
	Reduce the colour palette of an image.
	:param image_path: A path to the image to reduce the colour palette of.
	:param colours: The desired number of colours to use in the palette of the file.
	"""
	call_with_args("reduce_palette", input=image_path, output=image_path, colours=colours)

def optimise_png(image_path) -> None:
	"""
	Do a compression optimisation on a PNG file.
	:param image_path: A path to the PNG file to optimise.
	"""
	def optimise_threaded():
		call_with_args("optimise_png1", input=image_path, output=image_path)
		call_with_args("optimise_png2", output=image_path)
	thread = threading.Thread(target=optimise_threaded)
	thread.start()  # Fire and forget.