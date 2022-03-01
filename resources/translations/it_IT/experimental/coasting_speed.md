Coasting Speed
====
During the coasting, the nozzle doesn't extrude any more. However it doesn't quite behave as a travel move. The nozzle still continues travelling at approximately the same rate. With this setting, the exact rate at which the nozzle continues travelling can be configured.

The speed of coasting is configured by ratio of the normal printing speed. This means that if the [outer wall](../speed/speed_wall_0.md) and [inner wall](../speed/speed_wall_x.md) have different speeds, they will also coast at different speeds. Typically the coasting is done at a slightly lower speed than the normal printing speed, to combat the underextrusion.

Reducing the speed of coasting reduces the underextrusion effect that coasting naturally causes during the wall, but increases the underextrusion effect after the nozzle has moved on to print the next structure because the nozzle has been oozing for longer. Reduced speed is best paired with a reduced [volume](coasting_volume.md) for the coasting, so that the nozzle doesn't stay oozing for too long.

Reducing the speed also reduces the effect of coasting overall, since the nozzle will be resting on the seam for longer as well. This makes the seam more visible.