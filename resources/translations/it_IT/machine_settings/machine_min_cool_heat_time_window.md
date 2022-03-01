Minimal Time Standby Temperature
====
This setting configures the minimum duration of a stand-by in which it'll bother to cool the nozzle down to stand-by temperature. If the nozzle is set to be standing by for a shorter duration than this, it will not be cooled down but instead stay at the [Final Printing Temperature](../material/material_final_print_temperature.md).

Your nozzle has a PID regulator, which regulates how much power is used to heat your nozzle in order to reach the correct temperatures. When the nozzle is commanded to cool down and heat up with big temperature differences in quick succession, the PID regulator tends to mispredict how much heat is necessary. This causes wide fluctuations in the actual temperature of the nozzle. With this, you can prevent it from going to the [stand-by temperature](../material/material_standby_temperature.md) if the nozzle is inactive for a very short time.

The optimal value for this setting depends on the tuning of your PID regulator. Some regulators handle rapid target temperature changes better than others, and those may be able to handle a brief stand-by period better. Lowering this setting would then help to prevent the material from degrading inside the nozzle.

**Since this is a machine setting, this setting is not normally visible in the settings list.**