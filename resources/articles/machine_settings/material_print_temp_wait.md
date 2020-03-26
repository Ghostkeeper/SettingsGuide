Wait for Nozzle Heatup
====
The initial layer can have a different [nozzle temperature](../material/material_print_temperature_layer_0.md) than the [nozzle temperature of the rest of the print](../material/material_print_temperature.md). If this setting is enabled, the printer will wait until that temperature is reached before continuing the print.

It will wait until the temperature is heated up or cooled down to the appropriate temperature. While the label of this setting says that it'll wait for heating up, it'll cool down just as well. The nozzle will not wait for other temperature changes, such as for the [Initial Printing Temperature](../material/material_initial_print_temperature.md), the [Final Printing Temperature](../material/material_final_print_temperature.md) or the [Stand-by Temperature](../material/material_standby_temperature.md). If printing in [one-at-a-time mode](../blackmagic/print_sequence.md), the nozzle will also wait until the initial layer temperature is reached when it needs to go back to the first layer for the next objects.

*Since this is a machine setting, this setting is not normally visible to the user.*