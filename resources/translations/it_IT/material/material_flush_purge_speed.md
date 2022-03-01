Flush Purge Speed
====
If the printer needs to switch which filament goes through a certain nozzle, it needs to flush out the leftover material that was still in the nozzle chamber. This setting determines how fast the filament is being pushed through the feeder in order to purge out the old material.

This only applies to the moment after switching to a different type of material. If the same type of material is reloaded (e.g. because the previous spool was empty), a [different speed](material_end_of_filament_purge_speed.md) is used.

**This setting is currently never visible in Cura's interface. It can only be set by the profiles. It is also not used by Cura during slicing. However, printers that understand Cura's material file format may use it to configure their filament switching procedure correctly.** Through a post-processing script the `M600` command can be inserted in the print, which will trigger a filament switch.