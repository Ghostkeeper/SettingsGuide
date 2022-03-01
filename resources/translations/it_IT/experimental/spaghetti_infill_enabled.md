Spaghetti Infill
====
If this setting is enabled, Cura will extrude all infill of multiple layers at once in a higher layer. This serves as an extreme form of [Infill Layer Thickness](../infill/infill_sparse_thickness.md), but without the aim of maintaining rigidity of the infill. It has a bit of functionality to deal with the extreme amounts of extrusion.

This feature is not functional for ordinary materials. You'll normally either want the strength of ordinary infill patterns, or leave out the infill altogether. There are two use cases for it though.

Use cases
----
With flexible materials, this technique can produce some very soft textures. Spaghetti infill tends to produce loosely placed rings that don't adhere well to each other. These rings are equally squishy in all directions. To achieve this effect, the infill density cannot be too low though, or all of the spaghetti will end up on the bottom of the print. It's advisable to use an [flow density](spaghetti_flow.md) between 30% and 60%, depending on the line width and layer height. The result will be an infill that is equally rigid in all directions and fairly soft.

The other application for spaghetti infill is casting. If you have a printer that includes a tool to cast in specific places, this feature can be used to fill up your model pretty much evenly with controlled material depositions. If this is used, the [flow density](spaghetti_flow.md) likely needs to be approximately 100%, depending on the shrinkage/expansion ratio of the cast material.

Adjusting other settings for spaghetti infill
----
Both of these applications require very special handling of your infill. These are a few settings that you'll most likely want to adjust to your need:
* The [printing speed of infill](../speed/speed_infill.md) needs to be massively reduced. If the nozzle needs to extrude the infill of 10 layers at the same time, you'll want to reduce the printing speed by at least a factor of 8.
* Set your [infill layer thickness](../infill/infill_sparse_thickness.md) to be equal to the layer height.
* Increase your [printing temperature](../material/material_print_temperature.md) slightly (for the extruder that will print the infill). This allows the material to flow properly out the nozzle and allows for faster extrusion.
* Set the [seam alignment](../shell/z_seam_type.md) to be random to spread out the structure randomly.

**In Cura's layer view, the infill will show up as very fat lines. This is because Cura assumes that material stays on the same layer and spreads out there. In reality, it will fall down.**

**While spaghetti infill is being used, the [infill line width](../resolution/infill_line_width.md) setting has no effect any more. The line width is adjusted to meet the needs of the [infill line distance](../infill/infill_line_distance.md) and [spaghetti flow](spaghetti_flow.md) settings.**