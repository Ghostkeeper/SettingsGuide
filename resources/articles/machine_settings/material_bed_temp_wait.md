Wait for Build Plate Heatup
====
If this setting is enabled, the printer will wait until the build plate temperature is reached every time the build plate temperature is changed.

The build plate temperature is normally only changed after the first layer, if the [Build Plate Temperature Initial Layer](../material/material_bed_temperature_layer_0.md) is different from the normal [Build Plate Temperature](../material/material_bed_temperature.md). If printing in [one-at-a-time mode](../blackmagic/print_sequence.md), the build plate is also changed when it starts with the initial layer again for the next model. In these cases, the printer will wait until the new temperature is reached before continuing printing.

*Since this is a machine setting, this setting is not normally visible in the settings list.*