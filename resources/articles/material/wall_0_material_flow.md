This setting adjusts the flow rate for the outer wall only. The flow rate for the outer wall can be adjusted separately from the flow rate of the inner walls.

Adjusting the flow rate during the outer wall is a stop gap method to fix problems with extrusion rate or dimensional accuracy. The same effect can also be achieved by adjusting the [Outer Wall Line Width](wall_line_width_0.md) and [Outer Wall Inset](wall_0_inset.md) settings, but this setting could be a more intuitive way to tune initially.

If there is a problem with extrusion rate only during the outer wall, it is better to look at the [printing speeds](speed_wall_0.md) and [printing temperature](material_print_temperature.md). Perhaps the material doesn't get enough momentum out the nozzle and a greater print speed could help. Perhaps the lines are too thin to extrude properly. Perhaps the material is too cool or too hot.

If there is a problem with dimensional accuracy, it is better to look at [line widths](wall_line_width_0.md), [horizontal expansion](xy_offset.md) and the [printing order](outer_inset_first.md).