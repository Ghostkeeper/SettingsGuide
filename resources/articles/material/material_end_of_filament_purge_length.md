Some printers, when they run out of material, are able to load in a new spool automatically. When this happens, they need to prime the material again before the print. This setting determines the length of filament that is used to prime the new spool.

This only applies when the new material is the same as the previous material. When switching to a different material, a [different length](material_flush_purge_length.md) is used.

**This setting is currently never visible in Cura's interface. It can only be set by the profiles. It is also not used by Cura during slicing. However, printers that understand Cura's material file format may use it to switch to new spools correctly.**