If this setting is enabled, Cura will extrude all infill of multiple layers at once in a higher layer. This serves as an extreme form of [Infill Layer Thickness](infill_sparse_thickness.md), but without the aim of maintaining rigidity of the infill. It has a bit of functionality to deal with the extreme amounts of extrusion.

This feature is not functional for ordinary materials. You'll normally either want the strength of ordinary infill patterns, or leave out the infill altogether. There are two use cases for it though.

With flexible materials, this technique can produce some very soft textures. Spaghetti infill tends to produce loosely placed rings that don't adhere well to each other. These rings are equally squishy in all directions. To achieve this effect, the infill density cannot be too low though, or all of the spaghetti will end up on the bottom of the print. It's advisable to use an [infill density](infill_sparse_density.md) between 30% and 60%, depending on the line width and layer height. The result will be an infill that is equally rigid in all directions and fairly soft.

The other application for spaghetti infill is casting. If you have a printer that includes a tool to cast in specific places, this feature can be used to fill up your model pretty much evenly with controlled material depositions.

Both of these applications require very special handling of your infill. These are a few settings that you'll most likely want to adjust to your need:
* The [printing speed of infill](speed_infill.md) needs to be massively reduced. If the nozzle needs to extrude the infill of 10 layers at the same time, you'll want to reduce the printing speed by at least a factor of 8.
* Set your [infill layer thickness](infill_sparse_thickness.md) to be equal to the layer height.
* Increase your [printing temperature](material_print_temperature.md) slightly (for the extruder that will print the infill). This allows the material to flow properly out the nozzle and allows for faster extrusion.
* Set your [infill density](infill_sparse_density.md) to be somewhere between 30% and 60% for flexible materials, or to 99% for casting.