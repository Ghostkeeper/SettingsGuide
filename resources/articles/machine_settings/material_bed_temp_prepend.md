Include Material Temperatures
====
This setting communicates to the slicing back-end whether or not it should write nozzle temperature commands for the start of the print before the start g-code. It is automatically set upon starting a slice.

For most operations during the [start g-code](machine_start_gcode.md) it makes sense to have the nozzle up to the correct temperature for printing. To make it easier for people designing printer definitions, Cura will automatically heat up the nozzle before the start g-code is executed. However if the start g-code contains any reference to a nozzle temperature setting, it will not heat up the nozzle automatically any more.

*Since this is a machine setting, this setting is not normally visible to the user. Changing it also has no effect since it will be changed automatically by Cura.*