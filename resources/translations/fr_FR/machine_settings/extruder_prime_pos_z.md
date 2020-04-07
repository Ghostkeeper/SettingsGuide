Extruder Prime Z Position
====
If the [prime blob](../platform_adhesion/prime_blob_enable.md) is enabled, this setting indicates the Z coordinate at which the motion of the prime blob starts. Cura will move to that position before the prime blob is executed.

Unlike the X and Y coordinate, this is a machine setting. This is because the act of priming is assumed to have a fixed Z coordinate. To create a prime blob, the nozzle will need to move to the build plate and perhaps move up and down a bit. The [X](../platform_adhesion/extruder_prime_pos_x.md) and [Y](../platform_adhesion/extruder_prime_pos_y.md) can be chosen with normal settings to move the position of the prime blob in case the space on the build plate is limiting, but the Z coordinate cannot.

The only thing this changes is the Z coordinate that Cura will command the nozzle to move to before the prime blob command is executed.

*Since this is a machine setting, this setting is not normally visible in the settings list.*