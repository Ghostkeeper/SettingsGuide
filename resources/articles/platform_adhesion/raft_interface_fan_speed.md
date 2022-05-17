Raft Middle Fan Speed
====
<!--if cura_version<5.0:This setting configures the fan speed while printing the middle layer of the raft. The fan speed while printing the middle layer can be configured separately from the base and top layers.-->
<!--if cura_version>=5.0-->This setting configures the fan speed while printing the middle layers of the raft. The fan speed while printing the middle layers can be configured separately from the base and top layers.<!--endif-->

![Where the middle layer is located in the raft](../images/raft_dimensions_simplified.svg)

Configuring the fan speed for the middle <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->layers<!--endif--> separately is useful since reducing the fan speed can improve bed adhesion and reduce warping. Increasing the fan speed can improve the smoothness of the surface, but that is not a concern for the middle <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->layers<!--endif-->. Because of this, it's useful to set the fan speed a bit lower than in the top layers.