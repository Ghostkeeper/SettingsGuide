By enabling this setting, the print head will try to avoid hitting other objects when travelling around the build volume. It will take a small detour instead. If a detour is possible that doesn't hit any other objects, no retraction is triggered unless the length of the path exceeds the [Max Comb Distance With No Retract](retraction_combing_max_distance.md) setting.

![When disabled, travel moves can cross through other parts](../../../articles/images/travel_avoid_other_parts_disabled.png)
![When enabled, travel moves will avoid other parts](../../../articles/images/travel_avoid_other_parts_enabled.png)

Aside from avoiding other parts, the travel moves will also try to stay near the walls as shortly as possible. This means that when exiting or entering a part through a wall, it will exit or enter it perpendicular to the wall.

This setting tends to improve the surface quality of the print, because the nozzle will not cross through the walls as often. Crossing through the walls leaves a scar in the wall, so that should be avoided.

However, this setting does increase the amount of oozing, since more travel moves will be made without retracting and the travel moves will be longer. With materials that ooze a lot, it may be advisable to disable avoiding other parts.

Printing time could be slightly increased because the travel moves are longer, but usually this is completely offset by the reduction in the number of retractions that this causes.