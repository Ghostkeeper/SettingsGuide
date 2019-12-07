This setting adjusts the flow rate for the top and bottom only. The flow rate for the top and bottom can be adjusted separately from the flow rate of the rest of the print.

Adjusting the flow rate during the top and bottom is a stop gap method to fix problems with extrusion rate or not being water tight.

If there is a problem with extrusion rate only during the printing of the top side, it is better to look at the [infill density](infill_sparse_density.md) and [pattern](infill_pattern.md) or perhaps [gradual infill](gradual_infill_steps.md), in order to reduce the distance the top side needs to bridge. If there is a problem with extrusion rate only during the printing of the bottom side, take a look at the [density](support_infill_rate.md), [pattern](support_pattern.md) and [gradual infill](gradual_support_infill_steps.md) for support. The temperature and printing speed are also important factors for achieving good, consistent extrusion.

If the top or bottom is not water tight, it is better to tune the temperature. Pillowing should be prevented, but if the temperature is too low you will see underextrusion.