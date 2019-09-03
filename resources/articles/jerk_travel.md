This setting determines the speed at which the nozzle can go through corners while travelling across the build volume. This can be configured separately from the when the nozzle is extruding material.

Since the nozzle is not extruding any material during this time, it doesn't matter much that the printer is vibrating. If you've configured Cura to [avoid printed parts when travelling](travel_avoid_other_parts.md), then keeping a sufficient [distance](travel_avoid_distance.md) will prevent the nozzle from hitting your print even if it vibrates a bit. It's therefore useful to set the jerk very high during the travel moves to save on printing time.

Setting the jerk too high can cause the motors to skip though, which can cause a layer shift to appear.