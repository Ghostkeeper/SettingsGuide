X Endstop in Positive Direction
====
This setting tells Cura in which direction the printer will move along the X axis when it is ordered to home. If this setting is disabled, it assumes that the endstop for the X axis is at the zero (or negative) coordinate of the build volume. If the setting is enabled, it assumes that the endstop for the X axis is at the printer's maximum X coordinate.

This setting is not used by Cura at all. However it is used by the X3GWriter plug-in to implement the homing g-code command correctly when writing an X3G tool path file.

*Since this is a machine setting, this setting is not normally visible in the settings list.*