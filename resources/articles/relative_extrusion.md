Cura writes instructions for the printer to print your object in g-code. These instructions move the print head to certain positions and the engages the feeder. Cura normally records both the coordinates for the print head to move to and the rotation of the feeder as absolute coordinates. If this setting is enabled however, the coordinates for the feeder will be recorded relatively.

If this is disabled (i.e. absolute extrusion) the position of the filament at the start of the print is held as the zero coordinate. The position of the filament will increase throughout the file as more material gets extruded and the filament needs to move further and further from the starting point at the beginning of the print.

If this is enabled however, each separate line in the g-code will have their extrusion written separately, relative to the position of the previous line. Every line then contains only the amount of material extruded for that particular line.

Relative extrusion makes it easier to edit the g-code after it has been generated. If extra material needs to be extruded somewhere in between (to add or remove line segments or to adjust flow rates) the new extrusion simply needs to be written down in the part that is edited. If absolute extrusion is used, the position of the feeder needs to be reset using `G92` afterwards to make sure all subsequent commands are correct.

However if any rounding errors are introduced at any time during the processing of the g-code (in Cura, the firmware or the motion) absolute extrusion will automatically correct for that in the next line. In relative extrusion, this will lead to overextrusion or underextrusion, albeit extremely minor.

Not all printer firmware supports relative extrusion.

**When absolute extrusion is used, Cura will still reset the filament position every 10 metres in order to prevent floating point rounding errors in the firmware.**