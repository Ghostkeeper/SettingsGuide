G-code Flavor
====
While g-code is a standardised format for communicating instructions to CNC machines such as 3D printers, there are still some differences in which g-codes are supported by each printer, what their initial state is, and sometimes in how they interpret the commands. With the g-code flavour you can indicate largely what set of commands your printer accepts.

The difference between these g-code flavours is generally quite small. The most important commands, like moving around and heating the nozzle, are generally the same.

To select the correct g-code flavour, refer to the documentation of your printer's firmware. It should tell you which features are supported and which are not. These are the available flavours in Cura, and their differences.

Marlin
----
Marlin is considered the default g-code flavour. It's intended for the mainline [Marlin firmware](https://marlinfw.org/) that is the most popular 3D printing firmware and the basis of most alternative firmware out there.

Marlin (Volumetric)
----
This is a variant on Marlin where the extrusion commands specify how much they extrude in cubic millimetres, rather than in lengths of filament. These are the notable changes:
* The `E` parameter of the `G1` command is computed in cubic millimetres, the volume of the fed plastic, rather than the length of the filament to feed during this move.
* The statistics at the start of the g-code also mention the used filament in cubic millimetres.

RepRap
----
This is a flavour focussed on supporting printers that evolved from the [RepRap project](https://reprap.org/wiki/RepRap). It has a number of notable exceptions:
* Always mention the extruder when setting the initial layer temperature, even if there is only one extruder.
* Revert to relative extrusion after the print.
* Change accelerations using the `P` and `T` parameters of the `M204` command, for respectively printing acceleration and travel acceleration, rather than the `S` parameter.
* Change jerk using the `M566` command, rather than the `M205` command.

Ultimaker 2
----
This g-code flavour is intended for the Ultimaker 2 family. The firmware of this family had the odd idea that it should let the printer control material-related settings rather than the slicer. These are the exceptions:
* There will be no print temperature commands in the g-code.
* There will be no build plate temperature commands in the g-code.
* There will be no build volume temperature commands in the g-code.
* The first nozzle is assumed to have the [initial layer printing temperature](../material/material_print_temperature_layer_0.md) when the print starts.
* The build plate is assumed to have the [initial layer build plate temperature](../material/material_bed_temperature_layer_0.md) when the print starts.
* The `E` parameter of the `G1` command is computed in cubic millimetres, the volume of the fed plastic, rather than the length of the filament to feed during this move.
* The statistics at the start of the g-code mention the used filament in cubic millimetres.

Griffin
----
This is the g-code flavour for modern Ultimaker printers, the Ultimaker 3 and newer. These printers require a bunch of metadata in a certain format at the start of the g-code. The differences in this g-code flavour are:
* There is a large header at the start of the g-code containing metadata information such as the duration of the print, the name of the print job, and some practical information such as the starting temperature and the bounding box of the print.
* THere will be no build volume temperature commands in the g-code.
* The first nozzle is assumed to have the [initial layer printing temperature](../material/material_print_temperature_layer_0.md) when the print starts.
* The build plate is assumed to have the [initial layer build plate temperature](../material/material_bed_temperature_layer_0.md) when the print starts.
* The printer is not assumed to start on the first extruder, so it will always switch to the starting extruder at the start of the print using a `T` command.
* A prime blob is printed with `G280` for each extruder when it first starts printing, instead of a retraction.

Makerbot
----
This is a g-code flavour intended for [Sailfish](https://www.sailfishfirmware.com/) based firmware. This firmware is used in offspring of the original Makerbot printers. Some notable differences are:
* When changing the printing temperature, `M109` (set temperature and wait) is not supported. It outputs `M104` instead, which doesn't wait until the temperature is reached. It then uses `M116` to command the printer to wait until this temperature is reached.
* The `E` dimension of the `G1` extrusion command doesn't get reset during the print. For other flavours this parameter gets reset after every 10 metres of filament using a `G92 E0` command, to prevent floating point rounding errors in the firmware, but not with this one.
* Switching extruders happens with the `M135` command rather than with the `T` commands.
* The fan speed is not output. The fan is either on completely, or turned off. Cura will command the printer to turn the fan on if it would otherwise desire a fan speed of 50% or more.

Bits from Bytes
----
This is a g-code flavour targeted at the Bits from Bytes printers which had their own custom firmware. Their g-code flavour differs considerably from others. These are the changes that Cura will make:
* Extrusion amounts are written using RPM of the feeder rather than the `E` parameter.
* Retractions are written with `M101` or `M201`, depending on the active extruder.
* The retraction speed is written with a separate `M108` command.
* Travel moves are indicated with a `M103` command, instead of switching out `G1` for `G0`. There will be no `G0` commands.
* The printer is set to use automatic retraction using the `M227` command.
* Cura will output Windows-style newlines with a carriage return in front, rather than just a newline symbol.
* The `E` dimension of the `G1` extrusion command doesn't get reset during the print. For other flavours this parameter gets reset after every 10 metres of filament using a `G92 E0` command, to prevent floating point rounding errors in the firmware, but not with this one.

Mach3
----
This is a g-code flavour that stays closer to the way that CNC mills expect the g-code to be. There is only one notable difference:
* Extrusion amounts are written using the `A` parameter of the `G1` command, rather than the `E` parameter.

Repetier
----
This is a g-code flavour aimed at the 3D printers by Repetier. It mimics the output of the Repetier slicer. These are the notable differences with this g-code flavour:
* If firmware retractions are enabled, the retractions for an extruder switch use `G10 S1` to indicate that this is a retraction for an extruder switch.
* Acceleration changes are made using the `M201` and `M202` commands (for respectively printing acceleration and travel acceleration) rather than `M204`.
* Jerk changes are made using the `M207` command, rather than the `M205` command.

*Since this is a machine setting, it will not normally be listed in the normal list of settings. There is a selection menu for this setting though in the printer settings dialogue, which can be found in the list of added printers in the preferences dialogue.*