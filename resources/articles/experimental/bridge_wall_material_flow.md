Bridge Wall Flow
====
This setting adjusts the amount of material that is extruded to print bridging walls.

Reducing the amount of material will effectively reduce the line width of the walls that are bridging a gap. With reduced line width, the lines' surface-to-mass ratio is greater, which allows them to cool down faster and this will prevent them from sagging as much.

However reducing the flow rate too much will cause a great change in the flow rate, especially when combined with a [slower printing speed](bridge_wall_speed.md). In reality the material will not be able to change its flow rates very quickly, which causes the lines to be somewhat thicker than intended as the flow rate is slowed down, and somewhat thinner than intended as the flow rate is sped up. The first of those effects can be compensated for by some [coasting](bridge_wall_coast.md), but this requires careful tuning.