Raft Base Print Speed
====
This setting configures the speed at which the base layer of the raft is printed. The speed of the base layer can be configured separately from the speed of the top and middle layers.

![Where the base layer is located in the raft](../images/raft_dimensions_simplified.svg)

Printing the base layer more slowly allows the material to flow out more. This increases the contact area between the raft and the build plate, allowing it to stick better to the build plate. Keeping the material hot for longer will also anneal the plastic, reducing internal stress. Both of these effects reduce warping. The base layer is typically printed slower than the others. Of course, reducing the printing speed of the base layer too much makes the print take longer.

When the raft is used, the [initial layer printing speed](../speed/speed_print_layer_0.md) applies to the initial layer of the model, not the initial layer of the raft. The travel moves within the raft will be the ordinary [travel speed](../speed/speed_travel.md).