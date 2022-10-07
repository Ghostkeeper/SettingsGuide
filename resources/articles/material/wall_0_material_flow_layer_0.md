Initial Layer Outer Wall Flow
====
The flow of the initial layer can be changed with the [Initial Layer Flow](material_flow_layer_0.md) setting, but this setting allows control over the finer details of the initial layer by changing only the flow of the outer wall on the first layer.

Some parts of the initial layer are more likely to get loose from the build plate than others. The first lines of the print are the most dangerous. Using this setting you can change the outer wall to have a higher flow to attach it better to the build plate. This is useful when there is no brim in the print, because the outer wall is then printed as a single, loose line on the build plate with relatively little surface area to stick to.

By changing only the flow rate of the outer wall, problems with high flow rate such as [Overextrusion](../troubleshooting/overextrusion.md) can be avoided.