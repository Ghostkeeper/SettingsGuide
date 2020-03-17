Overhanging Wall Angle
====
This setting indicates the threshold angle after which a wall will be marked as an "overhanging wall". These overhanging walls can be printed at a different speed using the [Overhanging Wall Speed](wall_overhang_speed_factor.md) setting.

If this setting is set to 0°, all walls will be treated as overhanging walls. If this setting is set to 90°, no walls will be treated as overhanging walls. Walls that rest on support are not treated as overhanging walls either.

The aim of this feature is to provide better overhang qualities for areas that would almost need to be supported by [support](../support/support_enable.md), but not quite. Instead of spending extra time and material on support and scarring the surface when removing that support, you can choose to print these overhanging walls a bit slower and set the [Support Overhang Angle](../support/support_angle.md) somewhat higher. This achieves a more staged approach to printing increasing overhang angles better.

Setting this setting higher than the Support Overhang Angle reduces the effect of this feature greatly since walls on top of support are not marked as overhanging walls, and so any walls that are printed at an overhang angle that would be considered an overhanging wall would also be supported and not printed at different speeds. However this feature still has an effect then if support is disabled or for parts of overhang that are not supported for other reasons, such as [Minimum Support Area](../support/minimum_support_area.md).