Raft Middle Print Speed
====
<!--if cura_version<5.0:This setting configures the speed at which the middle layer of the raft is printed. The speed of the middle layer can be configured separately from the speed of the top and base layers.-->
<!--if cura_version>=5.0-->This setting configures the speed at which the middle layers of the raft are printed. The speed of the middle layers can be configured separately from the speed of the top and base layers.<!--endif-->

![Where the middle layer is located in the raft](../images/raft_dimensions_simplified.svg)

Printing the middle <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->layers<!--endif--> more slowly keeps the material hot for longer, which reduces internal stresses. This reduces warping once the material cools down. However printing more slowly also takes more time.