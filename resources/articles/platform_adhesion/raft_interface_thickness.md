Raft Middle Thickness
====
<!--if cura_version<5.0:This setting adjusts the vertical thickness of the middle layer of the raft.-->
<!--if cura_version>=5.0-->This setting adjusts the vertical thickness of the middle layers of the raft. This is just the height of one layer, so the total height of the middle layers will be this setting multiplied by the value of the [Raft Middle Layers](raft_interface_layers.md) setting.<!--endif-->

![Dimensions related to the raft](../images/raft_dimensions.svg)

Having a thicker raft layer tends to make the raft a bit stiffer. This prevents it from bending, both during printing and after printing. During printing, you'd want the raft to be stiff as to not warp, which breaks the adhesion to the build plate and causes the raft to fuse to the model. After printing, you'd want the raft to be flexible so that you can break it away from the model more easily. That is the balance that needs to be struck for this setting.