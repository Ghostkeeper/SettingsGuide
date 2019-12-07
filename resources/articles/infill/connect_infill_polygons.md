When the infill consists of closed loops, these closed loops can be fused together to form one single loop. Enabling this will make small connections where polygons are adjacent.

This setting is only available when the infill consists of loops that are adjacent to each other. That means that either:
* The [infill pattern](infill_pattern.md) is set to Cross or Cross 3D.
* The infill lines are [multiplied](infill_multiplier.md) to an even number.
* There are at least 2 [extra walls around the infill](infill_wall_line_count.md).

![With multiplied infill lines, there are lots of loops in this infill pattern](../images/connect_infill_polygons_disabled.png)
![Enabling this setting fuses the loops together](../images/connect_infill_polygons_enabled.png)

The aim of this function is to prevent travel moves. The final line will be one single loop for every connected part of infill, so there will not be any travel moves. This makes it easier to work with flexible filaments, because those are harder to retract and work best if they can keep flowing through the nozzle.

Connecting these loops can also make the infill stronger by enhancing the connection between the loops internally. However, when the polygons are connected the print head often has to make 180 degree turns just before a joint. These turns sometimes prevent the joint from being fully connected. This can also make infill weaker in some cases. It all depends on how the loops mesh out through the shape of your model.