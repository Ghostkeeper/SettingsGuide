Auto Temperature
====
When printing faster, it's best to print at a slightly higher temperature. This makes the thermoplastic more fluid, allowing it to flow more quickly out of the nozzle opening. This setting adjusts the temperature automatically depending on the average flow rate of material out of the nozzle.

To know how much the temperature must be adjusted, the [Flow Temperature Graph](material_flow_temp_graph.md) is referenced. The flow rate is calculated in cubic millimetres per second. Putting that in the flow temperature relation results in a certain temperature. This temperature will get used as the printing temperature. When this setting is activated, the ordinary [printing temperature](../material/material_print_temperature.md) setting will no longer be used in favour of the temperature calculated from the flow rate.

The aim of this setting is to achieve a better print quality, reducing overextrusion and underextrusion, if there are big flow changes within a print. A common case for this is the border between skin and infill. Because skin is normally printed much slower than the infill, the layers where there is a lot of infill should be printed at a slightly higher temperature so that the material can properly be extruded during the printing of that infill.

For many printers, the PID regulator that regulates temperatures in the printer's nozzle tends to overreact when there are many temperature changes in a short amount of time. This can cause the printing temperature to be wildly inaccurate when this setting is used.

**This setting is currently not visible in Cura's interface and cannot be activated.**