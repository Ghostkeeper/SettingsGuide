Bed Adhesion Problems
====
One of the most common failure modes for 3D prints is that the print got loose from the build plate while it was still being printed. This article goes over some adjustments you can make to prevent this from happening.

If the print got lost from the build plate, you will generally see a lot of loose wires all over the build plate. If you have more luck, it may manifest also as just a [layer shift](layer_shift.md) (and there will be less to clean up). Either way, the print is ruined.

Bed adhesion methods
----
Cura provides several methods to improve bed adhesion. You can choose between these methods with the [Build Plate Adhesion Type](../platform_adhesion/adhesion_type.md) setting. The following options are available.
* Brim, the most common technique, adds a rim around the bottom side of the print, which adds to the surface area so that the print will stick better to the build plate.
* A raft is a plate underneath the entire print. This plate gets a larger surface area as well, so that it sticks well. If the raft is printed with a material that sticks well to the print (like with the same material) then the print will stay in its place that way.
* A skirt is not attached to the print, but just encircles it. This line ensures that the material is flowing before the actual print starts, so there is no underextrusion in the first layer which could ruin the adhesion.
* You can also have no adhesion by selecting "None". This saves on time and material and prevents other negative effects from the aforementioned methods. Only use this if your printer has a different priming technique, such as a purge bucket.

The brim and the raft are the most effective techniques to increase the adhesion, as they are designed expressly for this purpose. Most reasonably-sized prints will need either of those.

If a brim is being used, you can increase the adhesion further by increasing the [width of the brim](../platform_adhesion/brim_width.md). You can also add a brim to the [inside of the supports](../support/support_brim_enable.md) and the [prime tower](../dual/prime_tower_brim_enable.md) as well as between the [model and support](../platform_adhesion/brim_replaces_support.md) and the [inside holes](../platform_adhesion/brim_outside_only.md) of the model.

Similarly, if a raft is being used, you can increase the adhesion further by increasing the [width of the raft](../platform_adhesion/raft_margin.md). The raft will always be printed underneath everything though, since the layers need to match up. If the adhesion between the model and the raft is a problem, consider reducing the [air gap](../platform_adhesion/raft_airgap.md) between the raft and the model. Furthermore you can consider increasing the [raft base line width](../platform_adhesion/raft_base_line_width.md).

Preventing warping
----
If your print suffers from warping, the contact area between the print and the build plate is greatly reduced. To prevent this, refer to the article on [warping](warping.md). To summarise, these are a few adjustments to make to prevent warping.
* Set the [Initial Layer Bottom Pattern](../shell/top_bottom_pattern_0.md) to concentric.
* Reduce the [Build Plate Temperature](../material/material_bed_temperature.md) and increase the [Build Volume Temperature](../material/build_volume_temperature.md).
* Adjust the model such that there are fewer sharp outer corners on the first layer.

Miscellaneous adjustments
----
These settings can also be adjusted if the normal bed adhesion methods are not sufficient.
* Increase the [Initial Layer Height](../resolution/layer_height_0.md). This offers a bit more room for error, if the build plate is not perfectly level. It also increases the force with which the material is pushed out of the nozzle and onto the build plate.
* Increase the [Initial Layer Line Width](../resolution/initial_layer_line_width_factor.md). Similarly, this pushes the material out with more force, sticking it well to the build plate.
* Increasing the [Printing Temperature Initial Layer](../material/material_print_temperature_layer_0.md) makes the material flow out more onto the build plate, increasing contact area.
* Like increasing the temperature, you can also reduce the [Initial Layer Fan Speed](../cooling/cool_fan_speed_0.md) or increase the [duration of that setting](../cooling/cool_fan_full_at_height.md) to keep the material fluid for longer.
* Similarly, reduce the [Initial Layer Speed](../speed/speed_layer_0.md). Reducing the [Initial Layer Print Speed](../speed/speed_print_layer_0.md) makes the material flow out more again, as the material is kept fluid for longer by the hot nozzle. Reducing the [Initial Layer Travel Speed](../speed/speed_travel_layer_0.md) reduces the chance that a travel move pulls previously printed lines off the build plate. Likewise, consider adjusting the [Initial Layer Acceleration](../speed/acceleration_layer_0.md) and [Initial Layer Jerk](../speed/jerk_layer_0.md) as well. 
* Increase the [Number of Slower Layers](../speed/speed_slowdown_layers.md). This reduces the chance that fast movements pull off the previous layers.

Build plates
----
Aside from a good print, a good build plate is important for adhesion as well. A good build plate should be:
* ...clean! It's very important that the build plate contains no grease (such as from your fingers) and no dust. Cleaning it under a hot tap is very effective. Using some rubbing alcohol and a microfibre cloth is ideal.
* ...level! If the build plate is too close, the flow out the nozzle will be inconsistent, resulting in bumps that the nozzle will tear off when it comes around next time. If the build plate is too far, the material is not pushed well onto the build plate, which reduces surface area greatly. Most printers allow adjusting the build plate with some thumb screws, so make sure that it is perfectly level and spaced correctly from the nozzle.
* ...rough! With a slightly roughened build plate, the contact area between the build plate and the print is greatly increased as opposed to a perfectly smooth build plate. Some printers come with frosted glass or anodised metal for this reason.

The material of the build plate also has a big impact on the adhesive properties. This can differ greatly with different print materials. Common build plate materials are glass, acrylic, aluminium, steel or anodised aluminium. Each of these stick to different materials. Plastic build plates may stick chemically to your material. Other materials rely on a rough surface to increase the contact area.

There are also add-on bed adhesion methods you can apply to any build plate:
* Generic paper glue sticks work very well. Although the glue dries up quickly, it produces a rough surface with increased surface area for the print to stick to.
* Masking tape has a similar effect, since it has a rough surface made of paper, but unlike paper it stays perfectly flat on the build plate. The thicker types of masking tape made for outdoor use are most effective.
* Hair spray works similar to glue in that it leaves a finely grained rough surface on the build plate. It's very easy to apply this evenly.
* Apply some sandpaper to the build plate to roughen it up and increase the contact area. Don't roughen it up too much though, or you'll have an uneven surface to print on. Use very fine-grained sand paper to do this, of grit 500 or more.
* Specialised "adhesion sheets" are sold by many 3D printer vendors, which can be stretched over the build plate. They function similarly to masking tape, but are made to last longer. Some are made out of a plastic that bonds chemically to the printed material as well.