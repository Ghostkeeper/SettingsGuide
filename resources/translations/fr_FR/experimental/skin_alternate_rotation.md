When the top and bottom are printed with the lines or zigzag [pattern](../shell/top_bottom_pattern.md), the lines are normally oriented in the diagonal directions, alternating the two directions every later. If this setting is activated, it will alternate in four directions instead: two diagonal directions, vertical and horizontal.

![Alternating four directions](../../../articles/images/skin_alternate_rotation.gif)

This setting will override the [Top/Bottom Line Directions](../shell/skin_angles.md) setting. The behaviour is the same though. In fact, this setting can be emulated completely by entering the angles `[45, 135, 0, 90]`.

Generally, your print will be the stiffest in the direction lengthwise to the direction of the lines. If this setting is not enabled, that will be in the two diagonal directions, making it weaker in the orthographic directions. These diagonal directions are chosen because the most common gantry mechanisms for 3D printers use more motors for diagonal movement, which allows them to accelerate faster in those directions.

If this setting is enabled, the directions of the lines are spread around more evenly. This spreads the strength of the object around more evenly as well. This makes the object stronger in the vertical and horizontal directions but slightly weaker in the diagonal directions. It will also take slightly longer to print the object.