# Copyright (C) 2021 Ghostkeeper
# This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import collections  # For namedtuple.
import json  # Screenshot instructions are stored in JSON format.
import numpy  # To crop the screenshots.
import os  # To store temporary files.
import os.path  # To store temporary files.
import re  # To find the screenshot instructions.
import subprocess  # To call external applications to do conversions and optimisations for us.
import time  # Crude way to make asynchronous calls synchronous: Spinlock until we get a signal that the asynchronous method is completed.
import typing

import cura.CuraApplication  # To change the settings before slicing.
import cura.Utils.Threading  # To render on the Qt thread.
import UM.Backend.Backend  # To know when the slice has finished.
import UM.Logger
import UM.Math.Vector  # To move the camera.
import UM.Mesh.ReadMeshJob  # To load STL files to slice or take pictures of.
import UM.View.GL.OpenGL  # To load the shaders to render screenshots with.
import UM.Resources  # To store converted OpenSCAD documents long-term.
import UM.Scene.Iterator.DepthFirstIterator  # To find the layer view data.
import UM.Scene.Selection  # To clear the selection before taking screenshots.

if typing.TYPE_CHECKING:
	from PyQt5.QtGui import QImage  # Screenshots are returned as QImage by the Snapshot tool of Cura.

"""
This module provides an automatic way to generate screenshots for the Settings Guide.

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
* Gifsicle: To optimise GIF files.

These dependencies can be installed on Ubuntu by running:
`sudo apt install openscad gimp optipng gifsicle`
Only Efficient-Compression-Tool has to be compiled separately from source. Make sure it ends up in the path. It can
be found here: https://github.com/fhanau/Efficient-Compression-Tool

The tool is available by setting the preference "settings_guide/screenshot_tool" to True. A button will then be
visible on every article. When pressed, it will re-create the images for that article. A button will also be present
on the landing page that will re-create ALL images. This takes a long time!
"""

# These are several system commands we can execute to perform various tasks using external tools.
commands = {
	"openscad": ["openscad", "-o", "{output}", "{input}"],  # Compile an OpenSCAD file.
	"reduce_palette": ["convert", "-colors", "{colours}", "+dither", "{input}", "png:{output}"],  # Reduce colour palette of an image.
	"optimise_png1": ["optipng", "-o7", "-strip", "all", "-snip", "-out", "{output}", "{input}"],
	"optimise_png2": ["ect", "-9", "-strip", "--allfilters-b", "--pal_sort=120", "--mt-deflate", "{output}"],  # Reduce file size of PNG images.
	"merge_gif": ["convert", "-colors", "{colours}", "-delay", "{delay}", "-loop", "0", "{inputs}", "{output}"],  # Merge multiple images into a GIF.
	"optimise_gif": ["gifsicle", "-O3", "{input}"]  # Reduce file size of GIF images.
}

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

ScreenshotInstruction = collections.namedtuple("ScreenshotInstruction", ["image_path", "model_path", "camera_position", "camera_lookat", "layer", "line", "settings", "colours", "delay"])
"""
All the information needed to take a screenshot.
* image_path: The filename of the image to refresh in the articles/images folder.
* model_path: The filename of the 3D model in the models folder.
* camera_position: The X, Y and Z position of the camera (as list).
* camera_lookat: The X, Y and Z position of the camera focus centre.
* layer: The layer number to look at. Use layer -1 to not use layer view. Use a list to define an animation.
* line: The number of lines to show on the current layer. Use 0 to view the entire layer. Use a list to define an
  animation.
* settings: A dictionary of setting keys and values to slice the object with.
* colours: The colour depth of the resulting image. Reduce colours to reduce file size. Max 256.
* delay: If this is an animation, the delay between consecutive images in milliseconds.
"""

def refresh_screenshots(article_text) -> None:
	"""
	Refresh the screenshots nested in the selected article text.

	This function serves as glue code and an overview of the stages through which we go in order to refresh the
	screenshots.
	:param article_text: The text containing embedded screenshots to refresh.
	"""
	for screenshot_instruction in find_screenshots(article_text):
		setup_printer(screenshot_instruction.settings)
		stl_path = convert_model(screenshot_instruction.model_path)
		load_model(stl_path)

		layers = screenshot_instruction.layer
		if type(layers) != list:  # To simplify processing, always use lists for the layer and line, pretending it's always an animation.
			layers = [layers]
		lines = screenshot_instruction.line
		if type(lines) != list:
			lines = [lines]
		while len(lines) < len(layers):  # Make the lines array equally long as the layers array by repeating it.
			lines *= 2
		while len(lines) > len(layers):
			lines.pop()

		is_animation = len(layers) > 1
		if layers[0] >= 0:
			slice_scene()

		full_image_path = os.path.join(os.path.dirname(__file__), "resources", "articles", "images", screenshot_instruction.image_path)

		# Track saved images in case we're making multiple that need to be combined into a GIF later.
		saved_images = []
		index = 0
		for layer, line in zip(layers, lines):
			is_layer_view = layer >= 0
			if is_layer_view:
				switch_to_layer_view()
				navigate_layer_view(layer, line)
			else:  # Need to show the model itself.
				switch_to_solid_view()
			screenshot = take_snapshot(screenshot_instruction.camera_position, screenshot_instruction.camera_lookat, is_layer_view)
			if not is_animation:
				target_file = full_image_path
			else:
				target_file = full_image_path + str(index) + ".png"
			save_screenshot(screenshot, target_file)
			saved_images.append(target_file)
			index += 1

		if is_animation:
			combine_animation(saved_images, full_image_path, screenshot_instruction.colours)
			optimise_gif(full_image_path)
			for image in saved_images:
				os.remove(image)
		else:
			reduce_colours(full_image_path, screenshot_instruction.colours)
			optimise_png(full_image_path)

def find_screenshots(article_text) -> typing.Generator[ScreenshotInstruction, None, None]:
	"""
	Finds the screenshot instructions and parses them to ScreenshotInstruction instances, so that the rest of the
	module may more easily process them and refresh screenshots.
	:param article_text: The article to find screenshots in, HTML-formatted.
	:return: A sequence of ScreenshotInstruction instances.
	"""
	screenshot_regex = re.compile(r"<!--screenshot\s*({.*?})\s*-->", re.DOTALL)
	for part in article_text:
		if part[0] == "rich_text":
			for match in re.finditer(screenshot_regex, part[1]):
				json_serialised = match.group(1)
				json_document = json.loads(json_serialised)
				yield ScreenshotInstruction(
					image_path=json_document["image_path"],
					model_path=json_document["model_path"],
					camera_position=json_document["camera_position"],
					camera_lookat=json_document["camera_lookat"],
					layer=json_document.get("layer", 99999),
					line=json_document.get("line", 0),
					settings=json_document.get("settings", {}),
					colours=json_document.get("colours", 256),
					delay=json_document.get("delay", 500)
				)
	return

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
	silver_pla = registry.findInstanceContainers(id="ultimaker_pla_silver-metallic")[0]
	printer.extruderList[1].setMaterial(blue_pla)
	printer.extruderList[2].setMaterial(red_pla)
	printer.extruderList[3].setMaterial(silver_pla)
	printer.definitionChanges.setProperty("machine_width", "value", "1000")
	printer.definitionChanges.setProperty("machine_height", "value", "1000")
	printer.definitionChanges.setProperty("machine_depth", "value", "1000")
	for extruder_nr in range(4):
		printer.extruderList[extruder_nr].userChanges.clear()
	printer.userChanges.clear()

	# Set the settings that we want to override for this slice.
	for key, value in settings.items():
		# Just set it anywhere without really checking whether it's per-extruder or whatever.
		for extruder_nr in range(4):
			printer.extruderList[extruder_nr].userChanges.setProperty(key, "value", value)
		printer.userChanges.setProperty(key, "value", value)

def convert_model(scad_path) -> str:
	"""
	Convert an OpenSCAD file into an STL model.

	The STL model will be saved in a temporary file.
	:param scad_path: A path to an OpenSCAD model file.
	:return: A path to an STL model file.
	"""
	scad_path = os.path.join(os.path.dirname(__file__), "resources", "models", scad_path)
	file_name = os.path.splitext(os.path.basename(scad_path))[0]
	stl_dir = os.path.join(UM.Resources.Resources.getDataStoragePath(), "settings_guide_screenshots")
	if not os.path.exists(stl_dir):
		os.mkdir(stl_dir)
	stl_path = os.path.join(stl_dir, file_name + ".stl")
	if not os.path.exists(stl_path):
		call_with_args("openscad", input=scad_path, output=stl_path)
	return stl_path

def load_model(stl_path) -> None:
	"""
	Load a 3D model into the scene to take a screenshot of.
	:param stl_path: A path to an STL model to load.
	"""
	application = cura.CuraApplication.CuraApplication.getInstance()
	application._currently_loading_files.append(stl_path)
	job = UM.Mesh.ReadMeshJob.ReadMeshJob(stl_path, add_to_recent_files=False)
	job.run()  # Don't plan it in on the job queue or anything. Actually run it on this thread.
	application._readMeshFinished(job)  # Abuse CuraApplication's implementation to properly put the model on the build plate.
	UM.Scene.Selection.Selection.clear()  # If the preference was enabled to auto-select objects, clear selection.
	time.sleep(1)

def slice_scene() -> None:
	"""
	Trigger a slice, so that we can show layer view in the screenshot.
	"""

	application = cura.CuraApplication.CuraApplication.getInstance()
	backend = application.getBackend()
	backend.slice()
	time.sleep(1)  # Give stuff some time to spin up.

	# Now do a spinloop, blocking this thread until the slice is completed.
	while backend._process:
		time.sleep(0.1)
	time.sleep(1)  # Give stuff some time to wind down.


def switch_to_layer_view() -> None:
	"""
	Show layer view in the screenshot.
	"""
	cura.CuraApplication.CuraApplication.getInstance().getController().setActiveStage("PreviewStage")

	layer_view_completed = False
	while not layer_view_completed:
		for node in UM.Scene.Iterator.DepthFirstIterator.DepthFirstIterator(cura.CuraApplication.CuraApplication.getInstance().getController().getScene().getRoot()):
			if node.callDecoration("getLayerData"):
				layer_view_completed = True
		time.sleep(0.2)

def navigate_layer_view(layer_nr, line_nr) -> None:
	"""
	Set the layer slider and line slider to the correct positions for the screenshot.
	:param layer_nr: The layer number to show on the screenshot.
	:param line_nr: The line to show on the screenshot. Use 0 to show the entire layer.
	"""
	layer_view_plugin = cura.CuraApplication.CuraApplication.getInstance().getPluginRegistry().getPluginObject("SimulationView")
	layer_view_plugin.setLayer(layer_nr)
	layer_view_plugin.setMinimumLayer(0)
	if line_nr > 0:
		layer_view_plugin.setPath(line_nr)
		layer_view_plugin.setMinimumPath(0)

def switch_to_solid_view() -> None:
	"""
	Show solid view in the screenshot.
	"""
	cura.CuraApplication.CuraApplication.getInstance().getController().setActiveStage("PrepareStage")

@cura.Utils.Threading.call_on_qt_thread  # Must be called from the Qt thread because the OpenGL bindings don't support multi-threading.
def take_snapshot(camera_position, camera_lookat, is_layer_view) -> "QImage":
	"""
	Take a snapshot of the current scene.
	:param camera_position: The position of the camera to take the snapshot with.
	:param camera_lookat: The position of the focal point of the camera.
	:return: A screenshot of the current scene.
	"""
	application = cura.CuraApplication.CuraApplication.getInstance()
	plugin_registry = application.getPluginRegistry()

	# Set the camera to the desired position. We'll use the actual camera for the snapshot just because it looks cool while it's busy.
	camera = application.getController().getScene().getActiveCamera()
	camera.setPosition(UM.Math.Vector.Vector(camera_position[0], camera_position[2], camera_position[1]))  # Note that these are OpenGL coordinates, swapping Y and Z.
	camera.lookAt(UM.Math.Vector.Vector(camera_lookat[0], camera_lookat[2], camera_lookat[1]))
	time.sleep(1)  # Some time to update the scene nodes. Don't know if this is necessary but it feels safer.

	if is_layer_view:
		render_pass = plugin_registry.getPluginObject("SimulationView").getSimulationPass()
	else:
		render_pass = plugin_registry.getPluginObject("SolidView").getRenderer().getRenderPass("composite")

	# Use a transparent background.
	gl_bindings = UM.View.GL.OpenGL.OpenGL.getInstance().getBindingsObject()
	gl_bindings.glClearColor(0.0, 0.0, 0.0, 0.0)
	gl_bindings.glClear(gl_bindings.GL_COLOR_BUFFER_BIT | gl_bindings.GL_DEPTH_BUFFER_BIT)

	render_pass.render()
	image = render_pass.getOutput()

	# Crop this image to the non-transparent pixels.
	pixel_data = image.bits().asarray(image.byteCount())
	numpy_pixels = numpy.frombuffer(pixel_data, dtype=numpy.uint8).reshape([image.height(), image.width(), 4])
	opaque_pixels = numpy.nonzero(numpy_pixels)
	min_y, min_x, _ = numpy.amin(opaque_pixels, axis=1)
	max_y, max_x, _ = numpy.amax(opaque_pixels, axis=1)
	image = image.copy(min_x, min_y, max_x - min_x, max_y - min_y)

	return image

def save_screenshot(screenshot, image_path) -> None:
	"""
	Save the screenshot to file in the plug-in folder.
	:param screenshot: The image to save to the file.
	:param image_path: The file path to store the screenshot in.
	"""
	screenshot.save(image_path)

def combine_animation(frames, image_path, colours) -> None:
	"""
	Combine the frames of an animation into a GIF file.
	:param frames: A list of PNG files storing the frames of the animation, in order.
	:param image_path: The path to the GIF file to store.
	:param colours: The number of colours to use in the palette of the GIF.
	"""
	pass  # TODO

def optimise_gif(image_path) -> None:
	"""
	Do a compression optimisation on a GIF file.
	:param image_path: A path to the GIF file to optimise.
	"""
	pass  # TODO

def reduce_colours(image_path, colours) -> None:
	"""
	Reduce the colour palette of a PNG image.
	:param image_path: A path to the PNG image to reduce the colour palette of.
	:param colours: The desired number of colours to use in the palette of the PNG file.
	"""
	call_with_args("reduce_palette", input=image_path, output=image_path, colours=colours)

def optimise_png(image_path) -> None:
	"""
	Do a compression optimisation on a PNG file.
	:param image_path: A path to the PNG file to optimise.
	"""
	call_with_args("optimise_png1", input=image_path, output=image_path)
	call_with_args("optimise_png2", output=image_path)