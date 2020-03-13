With this setting, you can limit the range from which the Adaptive Layers is allowed to select a layer thickness. The layer height is not allowed to deviate more than this variation from the normal [Layer Height](../resolution/layer_height.md).

For example, with a normal layer height of 0.15mm and the variation set to 0.1mm, Adaptive Layers may produce layers with a thickness between 0.05mm and 0.25mm.

This setting limits the power of the Adaptive Layers feature. If the range of layer thicknesses is too narrow, the layer thickness will always be very close to the original layer thickness as set by the Layer Height setting. Adaptive Layers will not do much then to save time or improve quality.

If the range is very wide however, the layers may become very thick or very thin. Very thick layers require a lot of flow out of the nozzle, which is not always possible due to the limited nozzle size and melting capacity of the heating track in the print head. Very thin layers are also not always possible due to the viscosity of the material or inaccuracy of the Z axis. So it is good to limit the range to which Adaptive Layers can tune the layer thickness. Otherwise the printer will struggle to reach the desired layer thickness.

The layer thickness can never go below 0.001mm, even if the range would allow it to.