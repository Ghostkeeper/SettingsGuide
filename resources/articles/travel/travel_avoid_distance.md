Travel Avoid Distance
====
When [avoiding collisions with other objects](travel_avoid_other_parts.md), this setting defines how much clearance the nozzle keeps to the other objects that it needs to avoid.

Keep in mind that this defines the distance between the other objects and the centreline of the travel move. The travel move has no thickness. It's advisable to give a value to this setting that is at least big enough so that the nozzle tip doesn't hit the other parts.

Increasing the value of this setting reduces the chance that the nozzle hits previously printed objects when travelling around them. However, increasing the value of this setting will also slightly increase the length of travel moves, since the nozzle must take a greater detour. This increases printing time and the amount of oozing slightly. More pressing perhaps is that this reduces the chance of a valid path being found that doesn't come too close to any previously printed parts. If no valid path is found, the nozzle will (perhaps) retract and travel in a straight line instead, resigning that the other parts will be hit anyway. So increasing this setting too much can also be detrimental to the surface quality.