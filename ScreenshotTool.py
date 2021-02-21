# Copyright (C) 2021 Ghostkeeper
# This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

class ScreenshotTool:
	"""
	This class provides an automatic way to generate screenshots for the Settings Guide.

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
		"openscad": "openscad -o {output} {input}",  # Compile an OpenSCAD file.
		"reduce_palette": "convert -colors {colours} {input} png:{output}",  # Reduce colour palette of an image.
		"optimise_png": "optipng -o7 -strip all -snip -out {output} {input} && ect -9 -strip --allfilters-b --pal_sort=120 --mt-deflate {output}",  # Reduce file size of PNG images.
		"merge_gif": "convert -delay {delay} -loop 0 {inputs} {output}",  # Merge multiple images into a GIF.
		"optimise_gif": "gifsicle -O3 {input}"  # Reduce file size of GIF images.
	}