Extruders Share Nozzle
====
With this setting, you can indicate that your printer only has a single nozzle, and all filament is pushed through that same nozzle. Cura will then change its priming strategy.

Normally Cura assumes that after the [start g-code](machine_start_gcode.md) is ran, all extruders have their filament at the tip of the nozzle, ready to print. When the extruders share a nozzle, this is not possible since only one filament can be inside the nozzle at a time. Instead of the normal priming procedure with a [prime blob](../platform_adhesion/prime_blob_enable.md) or extra skirt lines, the nozzle needs to prime as if for a full extruder switch. This involves printing in the [prime tower](../dual/prime_tower_enable.md), if enabled.

If all extruders share a single nozzle, it stands to reason that they also [share a heater](machine_extruders_share_heater.md). However Cura makes no link between the two by itself, so be sure to enable both if indeed your printer has a single nozzle and a single heater for all extruders.

**Since this is a machine setting, it will not normally be listed in the normal list of settings. There is a checkbox for this setting though in the printer settings dialogue, which can be found in the list of added printers in the preferences dialogue.**