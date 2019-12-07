For some printers, when a material is retracted for a filament switch, the material needs to be broken off cleanly in order to move it through the feeder without tangling. This setting configures part of the procedure to break it cleanly.

This setting adjusts the speed at which the material is retracted towards the second position to stretch the material to a thin thread. This thin thread stretches out of the heated zone in the nozzle, allowing it to cool down and solidify. The thin, hard strand of material can then be broken off in the next stage of the retraction.

![First, the material is retracted to stop oozing, as per this setting](../images/filament_switch_anti_ooze.svg)
![Second, the filament is slowly retracted to draw a thin thread that is easy to break and let this thread solidify](../images/filament_switch_break_preparation.svg)
![Third, the filament is quickly retracted further to break off the filament](../images/filament_switch_break.svg)

**This setting is currently never visible in Cura's interface. It can only be set by the profiles. It is also not used by Cura during slicing. However, printers that understand Cura's material file format may use it to configure their filament switching procedure correctly.** Through a post-processing script the `M600` command can be inserted in the print, which will trigger a filament switch.