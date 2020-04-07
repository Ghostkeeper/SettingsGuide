Nozzle Disallowed Areas
====
This setting indicates any areas on your build plate where the active nozzle is not allowed to go. The user is not allowed to place any objects in those areas, or nearby enough that they would cause something to be printed there (like a brim).

![Grey patches denote disallowed areas around where the clips are on the build plate](../images/machine_disallowed_areas.png)

This setting only applies to the *active nozzle*, meaning that you may still print objects next to these disallowed areas even if that would cause other nozzles to move over those disallowed areas. As such, this setting is really only useful for printers which lift the inactive nozzles up or park them outside the build volume when inactive. Contrary to the ordinary [Disallowed Areas](machine_disallowed_areas.md), these disallowed areas are not moved depending on the offset between the nozzles.

These forbidden areas are necessary to prevent the nozzle from colliding into things. For instance, there may be some clips on the build plate, or a sticker or a logo. If the user were to print too close to these objects, the nozzle would collide with them. At best you'd get a [layer shift](../troubleshooting/layer_shift.md). At worst you'd damage the nozzle or whatever the nozzle is colliding with.

The disallowed areas are drawn as a grey shadow on the build plate, indicating to the user that they cannot place any objects there. These shadows may be expanded in all directions to prevent the brim or skirt from hitting it and for various other reasons. There are also other shadows on the build plate, for instance to limit the range of motion if the nozzles have an offset.

*Since this is a machine setting, this setting is not normally visible in the settings list.*