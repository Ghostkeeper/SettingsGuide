Disallowed Areas
====
This setting indicates any areas on your build plate where the print head is not allowed to go. The user is not allowed to place any objects in those areas, or nearby enough that they would cause something to be printed there (like a brim).

These areas are typically necessary to prevent the print head for colliding into things. For instance, there may be a wiping brush within reach of the print head somewhere, or a switching bay, or a camera that protrudes slightly too far inside the build volume. If the user were to print too close to these objects, the print head would collide with them. At best you'd get a [layer shift](../troubleshooting/layer_shift.md). At worst you'd damage the print head or whatever the print head is colliding with.

The disallowed areas are drawn as a grey shadow on the build plate, indicating to the user that he cannot place any objects there. These shadows may be expanded in all directions to prevent the brim or skirt from hitting it and for various other reasons. There are also other shadows on the build plate, for instance to limit the range of motion if the nozzles have an offset.

If only the active nozzle would collide with the obstacles, then the similar setting [Nozzle Disallowed Areas](nozzle_disallowed_areas.md) can prevent the nozzle from colliding with it while still allowing the print head to move over it.