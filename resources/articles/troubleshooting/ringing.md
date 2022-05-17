Ringing
====
Ringing (sometimes called "ghosting") is an effect where ripples appear on otherwise flat surfaces near small details on that surface. The ripples start occurring just after printing the small details.

![Ripples on the surface](../images/ringing.jpg)

Causes
----
Ringing is caused by vibrations in your 3D printer. Trying to prevent ringing is to reduce these vibrations. They are especially pronounced if the print head moves in one of the resonance frequencies of your printer's frame.

It is one of these things that more expensive 3D printers usually try to prevent with a more rigid frame that vibrates less. They have a stronger gantry with hardened steel bars and rods, or provide a fully closed frame made out of very rigid material. This is expensive though, so cheap 3D printer models don't have the resources to prevent ringing. Printers with a Bowden tube set-up also don't have as much ringing, since the print head is much lighter than that of a direct drive print head (since the heavy feeder motor is resting on the print head).

Although the ringing manifests itself horizontally, the vibrations are not always horizontal. The build plate vibrating up and down with respect to the nozzle is a very significant effect too, because the plastic bead gets squished to become wider as the build plate vibrates closer, or thinner as it vibrates farther.

Hardware solutions
----
Before adjusting your print in Cura, it's a good idea to see first if you can improve your hardware to prevent ringing. This can provide overall improvements of the print results without having to sacrifice other qualities of the print such as strength or productivity. Here are some things you can consider:
* Add dampeners underneath your printer. You can use rubber feet or just place the printer on a block of soft foam. This will prevent vibrations if the table vibrates, and prevent the printer from vibrating the table as well. It will reduce the feedback that the vibrating printer gets from the table, which helps to reduce the high-frequency vibrations.
* Tighten the driving belts of the gantry. If these belts are not tight, the springiness of their rubber allows the print head to vibrate.
* If your print head has flexible attachments, such as a Bowden tube, consider affixing those so that they can no longer wobble. Tie wraps work well for Bowden tubes if there is something you can tie them to.
* Add more mass to the frame of your 3D printer. This will make it harder to move the frame due to its increased inertia, and so it will be harder to make it vibrate.
* Increase the rigidity of the frame of your 3D printer with extra braces or cross bars. You could manufacture these out of durable materials like steel, but if this is not an option, perhaps something can be found in a hardware store that fits with minimal adjustments. You can also consider 3D printing these braces and cross bars, but be aware that most plastics don't cope well with sustained force being applied.

Cura's solutions
----
If the hardware solutions are not an option, you can also reduce the ringing effect through some adjustments in Cura settings.

Since the vibrations are caused by accelerating the print head, the most prominent improvements are geared towards reducing those accelerations.
* Reducing the maximum [printing speed](../speed/speed_print.md) reduces the duration of the accelerations.
* Reducing the [acceleration rate](../speed/acceleration_print.md) directly reduces the acceleration and will reduce the strength of the vibrations.
* In 3D printing, [jerk](../speed/jerk_print.md) is an industry term for instantaneous velocity changes through corners. What that means is that it's essentially trying to accelerate infinitely in order to prevent needing to slow down too much in every corner. This causes very high accelerations for short amounts of time in every corner. Reducing the jerk can then also help to reduce vibrations. Instead of a brief, strong acceleration it will accelerate more slowly and for a longer time, which reduces high frequency vibrations but increases low frequency vibrations.

Those adjustments will make your print take longer. You can also prevent ringing in other ways though, by preventing the type of movements that cause them:
<!--if cura_version<5.0:* Disable the [gap filling](../shell/fill_perimeter_gaps.md) technique and don't [print thin walls](../shell/fill_outline_gaps.md), since these techniques sometimes use very small line segments and extra travel moves. If a wall is being printed afterwards, the printer will still be vibrating a bit.-->
* If your printer moves the build plate up and down rather than the print head, don't use [Z hops](../travel/retraction_hop_enabled.md). These cause the build plate to vibrate up and down long after the hop has been completed.

You can also print the [inner walls before the outer wall](../shell/outer_inset_first.md). Since the printing of the walls doesn't usually cause as much vibrations as other parts, this allows the printer to stop vibrating before the all-important outer wall is printed.

Lastly, depending on the geometry of your gantry, vibrations are sometimes absorbed differently in different directions. Rotating your print by 45 degrees may help too. 