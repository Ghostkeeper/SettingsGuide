Skirt/Brim Jerk
====
This setting determines the speed at which the nozzle can go through corners while printing the skirt or brim. This can be configured separately from the rest of the initial layer.

When the nozzle is going through corners, the print head will not only vibrate horizontally, but the build plate can also vibrate vertically. This vibration causes the adhesion between the skirt or brim and the build plate to be less consistent. Reducing the jerk during the printing of the skirt or the brim can reduce the chance of the print letting go of the build plate.

That said, the adhesion between the skirt and the build plate is not very important. If the skirt lets go, the print will likely still succeed. Also, there are not usually very sharp corners during the printing of the skirt or brim that could cause any vibrations. The effect of adjusting this setting will be very small.

Even though the skirt and brim are always part of the initial layer, the [Initial Layer Print Jerk](jerk_print_layer_0.md) has no effect on them. This setting overrides the Initial Layer Print Jerk.