Extrusion Cool Down Speed Modifier
====
If [Auto Temperature](../experimental/material_flow_dependent_temperature.md) is enabled, the printing temperature will be adjusted depending on how much material is extruded.

When the material is heated up inside the nozzle chamber, this takes away heat from the nozzle. Extruding material faster tends to take away more heat from the nozzle. If the temperature probe is not exactly at the tip of the nozzle this causes the nozzle to have a slightly lower temperature while extruding material than when idle even with a good PID controller.

This setting describes how much heat is lost in the nozzle while printing. The extra heat lost by extruding will then be compensated for by increasing the desired printing temperature from the g-code. The setting's value depends on the nozzle design, the heat capacity of the printed material and the extrusion rate.