Default X-Y Jerk
====
This setting indicates the jerk rate that your firmware uses for the X and Y directions, if Cura is not [controlling the jerk](../speed/jerk_enabled.md) of the print.

Cura assumes that your firmware uses the same jerk rate for the X and Y directions, but this jerk rate might be different for the Z direction and the feeder.

This is used to obtain correct time estimates for your print if Cura is not controlling the jerk rates. The entire print will use the same jerk rate then.

**Since this is a machine setting, this setting is not normally visible in the settings list.**