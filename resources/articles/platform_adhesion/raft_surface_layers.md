Raft Top Layers
====
<!--if cura_version<5.0:This is the number of layers in the top portion of the raft. There will always be one base layer and one middle layer, but there may be any number of top layers. These top layers are normally very dense, as to produce a smooth surface to print the model on.-->
<!--if cura_version>=5.0-->This is the number of layers in the top portion of the raft. There will always be one base layer, but there may be any number of [middle layers](raft_interface_layers.md) and top layers. These top layers are normally very dense, as to produce a smooth surface to print the model on.<!--endif-->

![Where the top layers are located in the raft](../images/raft_dimensions_simplified.svg)

More layers makes for a smoother surface to print the model on, because the sparsely filled base and middle layers need to be bridged. A smoother surface makes the bottom side of your print look better and makes the adhesion between the raft and the model stronger.

However, more layers also take considerably more time to print.