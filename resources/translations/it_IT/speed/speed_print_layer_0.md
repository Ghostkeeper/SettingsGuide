Initial Layer Print Speed
====
This setting adjusts the speed at which the bottom layer of the model is printed.

Adjusting this setting will adjust the speed of the extrusion moves in the first layer, but not the travel moves. For that, adjust the [Initial Layer Travel Speed](speed_travel_layer_0.md) setting. Even though the walls, skin and support can normally be printed at different speeds, they cannot for the initial layer. All will be printed at the speed in this setting. By default, this setting influences the [Skirt/Brim Speed](skirt_brim_speed.md) setting, but it can still be adjusted separately. The [speed of the raft base layer](../platform_adhesion/raft_base_speed.md) is not affected.

Reducing the initial layer printing speed will improve the adhesion between the model and the build plate. This is because the material stays hotter for a longer time and can then flow out longer. This reduces the internal stresses in the material and increases the contact area, both of which increase the adhesion.