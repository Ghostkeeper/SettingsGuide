Initial Layer Bottom Flow
====
The flow of the initial layer can be changed with the [Initial Layer Flow](material_flow_layer_0.md) setting, but this setting allows control over the finer details of the initial layer by changing only the flow of the skin on the first layer.

Some parts of the initial layer are more likely to get loose from the build plate than others. The first lines of the print are the most dangerous. Using this setting, you can reduce the flow of the skin to prevent getting overextrusion there, while keeping the flow of the walls of the print higher.

Having the flow of the initial layer too high can cause the skin to ripple, which gives an ugly effect on the bottom of the print and may cause the print to be torn off the build plate during the print. This is not as much of a problem for the walls. It is advisable to keep this flow lower than the flow of the [outer](wall_0_material_flow_layer_0.md) and [inner walls](wall_x_material_flow_layer_0.md).