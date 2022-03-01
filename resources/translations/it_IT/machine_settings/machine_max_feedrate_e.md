Maximum Speed E
====
This setting indicates the highest speed that your feeder can move the filament at.

This is used to limit the speed of [retractions](../travel/retraction_speed.md). You can't retract any faster than what your feeder can take.

It is also used to compute correct time estimates if the speed of the feeder would ever be a limiting factor in how fast a line can be printed. However in reality, the feeder normally moves orders of magnitude faster than the speed at which the plastic can melt inside your nozzle and the speed at which the print head can move to draw a neat line in your print, so this is never really a limiting factor.

**Since this is a machine setting, this setting is not normally visible in the settings list.**