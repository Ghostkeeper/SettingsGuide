Include Build Plate Temperature
====
This setting communicates to the slicing back-end whether or not it should write build plate temperature commands for the start of the print before the start g-code. It is automatically set upon starting a slice.

For most operations during the [start g-code](machine_start_gcode.md) it makes sense to have the build plate up to the correct temperature for printing. To make it easier for people designing printer definitions, Cura will automatically heat up the build plate before the start g-code is executed. However if the start g-code contains any reference to a build plate temperature setting, it will not heat up the build plate automatically any more.

**Since this is a machine setting, this setting is not normally visible in the settings list. Changing it also has no effect since it will be changed automatically by Cura.**