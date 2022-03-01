Maximum Acceleration X
====
This setting indicates the maximum acceleration that your printer's motor and frame can handle in the X direction, according to the printer's firmware.

This setting is only used to obtain correct time estimates. The [acceleration](../speed/acceleration_print.md) set by Cura has no limit, but Cura will assume that your firmware sets a certain limit per axis. If the acceleration in the X axis exceeds this setting, the time estimate of those moves will be adjusted to assume that your firmware limits the acceleration. The total acceleration may still be greater when accelerating diagonally with multiple axes at the same time.

**Since this is a machine setting, this setting is not normally visible in the settings list.**