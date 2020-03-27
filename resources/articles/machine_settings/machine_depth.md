Machine Depth
====
This setting indicates the range of Y coordinates through which the nozzle(s) are able to move. It's basically the usable size of the printer.

This is not equal to the actual depth of your printer on the shelf. The actual printer will also have a frame or an arm around its build volume, and this measurement doesn't include that size. It's only the size of the build volume, the coordinates where the nozzle could move.

![The build volume dimensions](../images/build_volume_dimensions.svg)

If multiple nozzles are involved, not all nozzles may be able to reach the entire build volume. If [Offset with Extruder](machine_use_extruder_offset_to_offset_coords.md) is enabled and the printer has different nozzles offset from one another, some nozzles won't be able to reach all the way to one side of the build volume. This setting merely indicates the union of the volumes that all nozzles are able to reach.

*Since this is a machine setting, it will not normally be listed in the normal list of settings. The width can be changed in the printer settings dialogue, which can be found in the list of added printers in the preferences dialogue.*