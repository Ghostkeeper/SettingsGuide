A 3D printer can't make the liquid plastic float in mid-air. It'll fall down if it doesn't have anything to rest on. If a part of your print is not overhanging quite enough to warrant [support](../support/support_enable.md), but still hangs over too wide to rest properly on the previous layer, you might see that the surface becomes very rough, sags down a bit, or even produces loose strings along the surface.

![This overhang didn't print nicely](../images/bad_overhang.jpg)

Support placement
----
The most common and reliable way to improve the quality of overhangs is to support the overhang using a support structure. If [support is enabled](../support/support_enable.md), Cura's automatic support generation will work fine for most models. But if it places too much or too little support, there are many ways to customise it.
* Adjusting the [overhang angle](../support/support_angle.md) is the most basic way to tune how much support material is placed. You should tune this parameter such that all of your overhanging areas are supported. This setting also determines which areas get drawn in red in the Prepare stage.
* You can remove overhanging parts above other parts by setting the [Support Placement](../support/support_type.md) setting to "Touching Buildplate". Setting this to "Everywhere" instead may prevent bad overhang.
* Make sure that the [Minimum Support Area](../support/minimum_support_area.md) is not erasing thin bits of support.
* With the Support Blocker tool, you can place cubes in your scene to prevent generating support there. You can also select these blocks and in the Per Model Settings tool tell Cura to "print them as support". They will then be printed as a new piece of support. This way you can carefully customise exactly where support gets placed. You can even load a complete 3D model into Cura with the exact shape of your support, and tell Cura to print it as support in the Per Model Settings tool.

Placing support for your overhang is a very reliable way to improve the overhang quality, but it will take a lot of extra time and material. This support also needs to be removed afterwards, which can leave a visible scar on your surface. Below are some alternative methods to improve your overhang quality.

Bridging
----
If there is a bit of your model that is completely flat overhang, but gets supported on at least two sides, Cura will try to print it as bridging. It will orient the overhanging lines such that they cross from one supported side to another.

If the [extra bridging settings](../experimental/bridge_settings_enabled.md) are enabled, there are many more settings that can be adjusted to reduce or compensate for the sagging overhang.
* Reduce the flow rate of both the [walls](../experimental/bridge_wall_material_flow.md) and the [skin](../experimental/bridge_skin_material_flow.md). Reduced flow will push the material out the nozzle less strongly, which prevents it from sagging as much.
* Reduce the printing speed of both the [walls](../experimental/bridge_wall_speed.md) and the [skin](../experimental/bridge_skin_speed.md). Again, this reduces the force with which the material gets pushed out the nozzle, but it also gives more time for the material to solidify under the powerful fans on the print head.
* Increase the [fan speed](../experimental/bridge_fan_speed.md) during bridging. This solidifies the material more quickly, preventing it from sagging as much.

Other settings
----
Some other settings you can adjust in order to improve the quality of overhangs are:
* The [Overhanging Wall Speed](../experimental/wall_overhang_speed_factor.md) can be reduced in order to reduce the force with which the nozzle pushes the material down while printing overhangs more than a [given angle](../experimental/wall_overhang_angle.md).
* Print the [inner wall before the outer wall](../shell/outer_inset_first.md) (disable the setting) to give the outer wall something to attach to. This makes it sag down a bit less.
* You could just [remove all overhangs](../experimental/conical_overhang_enabled.md) greater than a [given angle](../experimental/conical_overhang_angle.md) from your model. Effectively this functions as a support structure. However that support is not removable from your model, but instead is printed seamlessly as if it belongs to the design.