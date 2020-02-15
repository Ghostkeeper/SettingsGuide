For some printers, when a material is retracted for a filament switch, the material needs to be broken off cleanly in order to move it through the feeder without tangling. This setting configures part of the procedure to break it cleanly.

This setting adjusts the third position that the material is retracted to in order to finally break the filament off of the blob that inevitably remains in the nozzle. While the blob in the nozzle cannot be pulled out due to its molten state, the part that does get pulled out should not have a thin thread at its tip, because that could get caught stuck in the feeder. This final retraction breaks the filament, but hopefully it breaks cleanly thanks to the preceding two stages.

![First, the material is retracted to stop oozing](../images/filament_switch_anti_ooze.svg)
![Second, the filament is slowly retracted to draw a thin thread that is easy to break and let this thread solidify](../images/filament_switch_break_preparation.svg)
![Third, the filament is quickly retracted further to break off the filament](../images/filament_switch_break.svg)

**This setting is currently never visible in Cura's interface. It can only be set by the profiles. It is also not used by Cura during slicing. However, printers that understand Cura's material file format may use it to configure their filament switching procedure correctly.** Through a post-processing script the `M600` command can be inserted in the print, which will trigger a filament switch.