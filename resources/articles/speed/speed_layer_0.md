Initial Layer Speed
====
This setting adjusts the speed at which the bottom layer of the model is printed.

All of the initial layer will normally be printed with this speed, even though the walls, skin and support can normally be printed at separate speeds. Not so for the initial layer! For the initial layer, the [printing speed](speed_print_layer_0.md) can be adjusted separately from the [travel speed](speed_travel_layer_0.md). The speed at which the [brim and skirt](skirt_brim_speed.md) is printed can also be adjusted. By default, this setting affects all of those. However the [speed of the base layer of the raft](../platform_adhesion/raft_base_speed.md) is not affected.

Reducing the initial layer speed will improve the adhesion between the model and the build plate. This is because the material stays hotter for a longer time and can then flow out longer. This reduces the internal stresses in the material and increases the contact area, both of which increase the adhesion.