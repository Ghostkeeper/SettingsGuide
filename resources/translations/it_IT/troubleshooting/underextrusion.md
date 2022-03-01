Underextrusion
====
One of the most common problems in 3D printing is that the printer doesn't extrude enough material to produce a nice, solid object. When this happens, we speak of "underextrusion": The nozzle extrudes less material than intended.

![An extreme case of underextrusion, where you can even see the insides of the object](../images/underextrusion.jpg)

Underextrusion can also manifest itself in many ways. In the most extreme case, the object is very brittle and the insides can be seen through the surface. Sometimes it's visible by the line widths being too small, so that they don't connect to the adjacent lines. Sometimes it only manifests as small holes in the top surface or tiny fractures in the walls.

There are myriad possible causes for underextrusion, making it very hard to troubleshoot this. The rest of this article describes some of the most likely causes and how to remedy them.

Clogged nozzle
----
If your printer was previously printing fine, and suddenly exhibits underextrusion without any significant changes to the printed object or settings, it's likely that the problem is somewhere in the extruder train. Usually the weakest link here is the nozzle.

Clogged nozzles are a regular occurrence with any 3D printer. This can happen when the filament is contaminated with things that don't melt well and gets pushed into the nozzle. It may also happen when the filament itself is burnt in the nozzle. That can happen when the plastic is heated too high or kept at a high temperature for too long. The material will degrade, the polymers will crystallize and you're left with a piece of hard plastic that won't melt out of the nozzle. To remedy this, you need to pull the debris out of the nozzle.

There are several techniques to pull out debris from the nozzle. If you have an acupuncture needle or some other thin metal pin you can push it out from the bottom. However the most common technique is known as the "Atomic Pull". To execute this technique, take a piece of filament at least 50cm long, preferably of some material with a high melting point. Heat up the nozzle to the melting point of that filament (e.g. 190°C for PLA), then push the filament in with pliers until some material is coming out of the nozzle. Then let the nozzle cool down towards its glass transition temperature (e.g. 60°C for PLA), all the while pushing the filament down into the nozzle. Just before the glass transition temperature is reached, pull the filament out quickly. If the tip of the filament is dirty with blackened plastic, snip off the tip and try again until it's clean. Try printing something again and hopefully it's extruding better now.

Slipping feeder
----
Sometimes the feeder doesn't get enough grip on the filament to push it down hard enough through the nozzle. During printing, you can hear the filament slip periodically then, with a soft clack every few seconds. This is the feeder trying to push the filament in, but the filament slipping out again once in a while.

Most feeders will have points of adjustments to adjust how much force they exert on the filament. Try adjusting the feeder a bit more tightly onto the filament. If the feeder is pushing too hard against the filament, it might break the filament or cause too much friction and start grinding. If it's too loose, you'll often see some underextrusion.

Inconsistent filament diameter
----
While most filaments are fine, sometimes a batch gets produced where the filament is just a bit too thin. This can have big consequences on the amount of extrusion in your print. Cheaper filaments are often more prone to show this problem. You can use calipers to measure the actual diameter of your filament. Be sure to measure in several different spots along the length of the filament, and don't measure where the feeder has ground down the filament.

If the filament's diameter is too far off (a 50μm difference starts to be seen in the print) then you can adjust the diameter of your filament in the material manager. If you're using a built-in material of Cura, you'll need to duplicate that material before editing it. Cura will then compensate for the new diameter by adjusting the speed of the feeder.

Material melting
----
Aside from your 3D printer being in top shape, the settings you print with also need to match the material properties of the material you're using. The most important one is the printing temperature.

If the [printing temperature](../material/material_print_temperature.md) is too low, you'll see underextrusion very quickly. If the material is too cold, it will be very viscous, making it harder for it to flow properly out of the nozzle. When combined with a high printing speed, the material doesn't have time to melt properly and also doesn't have time to flow into position. Some materials, like PVA or Nylon, are prone to absorbing moisture from the air. This moisture will evaporate when the material is printed, which cools the plastic down. To compensate for that effect, those materials need to be printed at a higher temperature if they've been exposed to air for a while.

If the temperature is too high, the material can degrade very quickly. Degraded filament may not melt properly either, which will clog the nozzle. The added heat may also cause the material to melt further up in the extruder train. This can cause friction in the extruder train, which makes it harder to push the material out. Look carefully at the temperature specifications on the label of your filament to see which temperature range it can be printed at.

Rather than adjusting the temperature, you may also choose to adjust the [fan speed](../cooling/cool_fan_speed.md). If the fan is set too high, the nozzle may cool down faster while extruding material, causing it to be colder than what the temperature sensor is actually measuring. Especially for materials that naturally print at a high temperature, such as polycarbonate, reducing the fan speed is often necessary to prevent underextrusion.

Printing too fast will also result in underextrusion, since the material doesn't have time to melt inside the nozzle chamber. Reducing the [printing speed](../speed/speed_print.md) may also help to combat underextrusion.

Getting the material flowing
----
There is always some latency between when the printer feeds the material forward and when it actually starts extruding. This latency can cause underextrusion if it's not taken into account. When the printer pushes the material forward, the pressure in the nozzle chamber will increase gradually until it's enough to push the molten material out on the other end. It may take up to a second for the material to reach its normal flow rate. If the printer has a Bowden tube between the feeder and the nozzle, this delay may even be many times greater, in the ball park of 10 seconds or so.

When the printer needs to start extruding more material than before, it'll feed the material faster but it will take a while before this arrives at the nozzle tip. In the meanwhile, the nozzle will try to draw a line, but this line will be underextruding. Especially when the print is very detailed, this can cause considerable underextrusion.

There are two adjustments you can make to fix this: Priming and speed adjustments.

Priming the material is to push out a bit of material before the important part of the print starts. Often this is done at the beginning of a print in a separate routine, by printing a small line or droplet of plastic in a corner of the build plate. Alternatively, you can use a [skirt or a brim](../platform_adhesion/adhesion_type.md), which will print a number of lines around the print itself. When the material is flowing properly and all air is out of the nozzle chamber, it'll extrude more consistently.

When the material is retracted, the flow of material is interrupted. When the material is pushed back into the nozzle, it may take a while to get it flowing again. Reducing the [speed at which it pushes back](../travel/retraction_prime_speed.md) allows the material to melt better before it's extruded, which helps a bit. Otherwise you can also try to push the material slightly further than before the retraction by [priming a bit more](../travel/retraction_extra_prime_amount.md) to compensate for the underextrusion. Tuning this is very finicky though.

Equalising speeds
----
If you're seeing underextrusion only in certain structures of the print, such as infill and support, look at equalising the flow rate in your print more. There is always a delay between the feeder feeding the material and this material actually flowing out of the nozzle. If the print speed is increased for some part of the print, then the print head will accelerate relatively quickly, but the material flow will lag behind until the pressure in the nozzle chamber is increased to deal with the greater extrusion rate. This causes underextrusion as well. Similarly, when slowing down the extrusion rate, there is always some overextrusion.

Some firmware is able to compensate for this effect. Marlin has a feature called [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) where it will start increasing the pressure inside the nozzle chamber in advance so that it's able to flow out of the nozzle earlier. Sailfish has a [similar feature](https://www.sailfishfirmware.com/doc/tuning-jkn-advance.html) that they call JKN Advance. To adjust the parameters of these features, look into what g-code you need to write in the start g-code.

If such features are unavailable or ineffective, you'll need to make sure that there are no sudden, big flow changes in the print. Reduce the [Infill Layer Thickness](../infill/infill_sparse_thickness.md) and [Support Layer Thickness](../support/support_infill_sparse_thickness.md). These settings will multiply the extrusion rate to achieve a greater layer height.

More importantly, you need to make sure that the infill, inner walls, outer wall, skin and support are printed with a similar extrusion rate. The extrusion rate of a line is the product of its line width, layer height, flow and (average) speed. Multiply those four together, and make sure that the result is approximately the same for the infill ([layer height](../infill/infill_sparse_thickness.md), [line width](../resolution/infill_line_width.md), [flow](../material/infill_material_flow.md) and [speed](../speed/speed_infill.md)), skin ([line width](../resolution/skin_line_width.md), [flow](../material/skin_material_flow.md) and [speed](../speed/speed_topbottom.md)), outer wall ([line width](../resolution/wall_line_width_0.md), [flow](../material/wall_0_material_flow.md) and [speed](../speed/speed_wall_0.md)), inner wall ([line width](../resolution/wall_line_width_x.md), [flow](../material/wall_x_material_flow.md) and [speed](../speed/speed_wall_x.md)) and support ([layer height](../support/support_infill_sparse_thickness.md), [line width](../resolution/support_line_width.md), [flow](../material/support_material_flow.md) and [speed](../speed/speed_support.md)). If [compensating for overlap in walls](../shell/travel_compensate_overlapping_walls_enabled.md), make sure to enable [flow equalisation](../speed/speed_equalize_flow_enabled.md) so that the speed is adjusted rather than the flow.

Nozzle limits
----
Extruding too much material through a small nozzle may also cause underextrusion. When printing at great layer heights, line widths or speeds using a small nozzle, the material physically won't be able to flow out of the nozzle in time. Increasing the temperature may help to make the material more runny up to a certain point, but there are still limits to what a nozzle can extrude. Beyond this limit, consider buying a bigger nozzle.

On the other side, extruding too little material can also cause underextrusion. If the pressure in the nozzle chamber is very low, then the surface tension of the liquid plastic can keep the material in the nozzle chamber. Occasionally it will get pushed out with a big droplet, leaving air in other places. This can give a similar effect to underextrusion.

Adjusting flow directly
----
If all else fails, Cura also has a setting to adjust the flow directly: [Flow](../material/material_flow.md). This stop-gap method can compensate for an unknown fault somewhere in the system.

This will not work if the material is physically prevented from flowing any faster (e.g. because of a clogged nozzle). In other cases it will likely cause overextrusion in some places. It is a simple way to adjust the print as needed though.