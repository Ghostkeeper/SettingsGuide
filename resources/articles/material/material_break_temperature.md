Break Temperature
====
For some printers, when a material is retracted for a filament switch, the material needs to be broken off cleanly in order to move it through the feeder without tangling. This setting configures part of the procedure to break it cleanly.

This setting adjusts the temperature to cool down to before breaking the filament off. This cooling will occur between the second and the third stage (as shown in the images below). The aim is to allow the filament to harden, which allows the printer to break it off cleanly rather than drawing it out in a long strand which could get caught in the feeder.

![First, the material is retracted to stop oozing](../images/filament_switch_anti_ooze.svg)
![Second, the filament is slowly retracted to draw a thin thread that is easy to break and let this thread solidify](../images/filament_switch_break_preparation.svg)
![Third, the filament is quickly retracted further to break off the filament](../images/filament_switch_break.svg)

**This setting is currently never visible in Cura's interface. It can only be set by the profiles. It is also not used by Cura during slicing. However, printers that understand Cura's material file format may use it to configure their filament switching procedure correctly.** Through a post-processing script the `M600` command can be inserted in the print, which will trigger a filament switch.