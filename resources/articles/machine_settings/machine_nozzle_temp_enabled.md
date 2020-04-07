Enable Nozzle Temperature Control
====
If this setting is disabled, Cura will not output any temperature commands to the g-code. Instead, Cura will leave it up to the firmware of the printer to heat the nozzles before the print.

This is similar to [Has Heated Build Plate](machine_heated_bed.md) in how it functions. If this setting is disabled, the temperature control settings such as [Printing Temperature](../material/material_print_temperature.md) will not be shown to the user.

Disabling this temporarily could be used to perform a dry run of the print. For that, you would also need to [disable the build plate](machine_heated_bed.md), the [heating of the build volume](machine_heated_build_volume.md) and set the [flow rate](../material/material_flow.md) to 0%.

*Since this is a machine setting, this setting is not normally visible in the settings list.*