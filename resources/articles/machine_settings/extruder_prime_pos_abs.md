Absolute Extruder Prime Position
====
If the [prime blob](../platform_adhesion/prime_blob_enable.md) is used, the position of this prime procedure can be adjusted with an [X](../platform_adhesion/extruder_prime_pos_x.md) and [Y](../platform_adhesion/extruder_prime_pos_y.md) position. This setting determines whether this is the position on the build plate, or a position relative to the current printer position.

If this setting is enabled, the X and Y coordinates refer to a certain fixed position on the build plate. The extruder will always move there in order to create a prime blob.

If this setting is disabled, the X and Y coordinates are relative to the position that the nozzle happens to have when switching to that extruder for the first time. For the first extruder, that would be the [0,0] coordinate. For the other extruders, this would be their start position as defined in the extruder's definition file. This start position can also be relative.

It is strongly advised to use an absolute prime position. An absolute prime position is guaranteed to be free of collisions with other parts of the print, since you are unable to place objects in that place on the build plate. A relative prime position could end up anywhere on the build plate, and as a result you might end up priming somewhere on top of your first layer. Using a relative prime position could save some travel time, but this really isn't worth the risk.

**Since this is a machine setting, this setting is not normally visible in the settings list.**