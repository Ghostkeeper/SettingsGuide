Minimum Polygon Circumference
====
Cura normally removes details of the model that are smaller than what the nozzle can feasibly print. With this setting, you can adjust that threshold to remove more or fewer details. This setting measures the circumference of every shape on every layer and if it's smaller than this setting's value, that shape will not be printed.

Removing details that are smaller than one line width is a good idea. This speeds up slicing slightly. However this doesn't always hold with parts that are smaller than the [Outer Wall Line Width](../resolution/wall_line_width_0.md) when the [Print Thin Walls](../shell/fill_outline_gaps.md) features is enabled. If very small pieces still need to be attempted, you can make this setting smaller.

Increasing this setting can also help to remove small details and achieve a faster print. If it doesn't need to print these small details it may save some travel moves to get to them.