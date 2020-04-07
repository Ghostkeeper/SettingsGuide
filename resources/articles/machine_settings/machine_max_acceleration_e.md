Maximum Filament Acceleration
====
This setting indicates the maximum acceleration that your printer's feeder motors handle, according to the printer's firmware.

This setting is only used to obtain correct time estimates. The [acceleration](../speed/acceleration_print.md) set by Cura has no limit, but Cura will assume that your firmware sets a certain limit per axis. If the acceleration for the feeder exceeds this setting, the time estimate of those moves will be adjusted to assume that your firmware limits the acceleration. The total acceleration may still be greater when accelerating diagonally with multiple axes at the same time.

It is quite common that the acceleration limits for the feeder are hit, since (depending on the firmware) the acceleration set by Cura also affects the feeder. So it is crucial that this setting is configured correctly in order to get correct time estimates for retractions.

*Since this is a machine setting, this setting is not normally visible in the settings list.*