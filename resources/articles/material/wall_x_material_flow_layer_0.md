Initial Layer Inner Wall Flow
====
The flow of the initial layer can be changed with the [Initial Layer Flow](material_flow_layer_0.md) setting, but this setting allows control over the finer details of the initial layer by changing only the flow of the inner walls on the first layer.

Some parts of the initial layer are more likely to get loose from the build plate than others. The first lines of the print are the most dangerous. Using this setting you can change the inner walls to have a higher flow to attach it better to the build plate. This is particularly useful when printing the inner walls before the outer wall, because then the first inner wall is printed as a single, loose line before attaching to the outer wall and the brim.

By changing only the flow rate of the inner wall, problems with high flow rate such as [Elephant's Foot](../troubleshooting/elephants_foot.md) can be avoided.