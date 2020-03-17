Raft Top Layer Thickness
====
This setting adjusts the thickness of the surface layers. This is just the height of one layer, so the total height of the surface layers will be this setting multiplied by the value of the [Raft Top Layers](raft_surface_layers.md) setting.

![Dimensions related to the raft](../images/raft_dimensions.svg)

A small layer height tends to improve the effect of cooling on the raft. This improves overhang and through that the smoothness of the raft. A smoother raft causes the print on top of it to be smoother as well and improves adhesion between the raft and the object. However, making the layer too shallow causes underextrusion, which is not beneficial for adhesion. Also consider that there will be a large change of flow rate between the top layer of the raft and the bottom layer of the object, which will cause some underextrusion when printing the first layer of the object.