This setting specifies how fast the nozzle will move up while making a vertical motion in the saw-tooth pattern. The speed of moving upwards can be configured separately from the rest of the wire printing speed.

![Where the different Wire Printing speeds apply](images/wireframe_printspeed.svg)

The upward motion will not have the specified speed for the entire motion. For the lowest bit of the upward motion, as defined by the [Ease Upward](wireframe_up_half_speed.md) setting, the print head will move at half of this speed.

Moving up slower will take more time but gives the material more time to solidify. This way it won't get dragged along as much in the direction of the diagonal. However moving too slow will also push the line downward due to the inertia of the filament with pressure in the nozzle chamber. The filament tends to wobble then which makes it less likely that the next horizontal line can make a proper connection.