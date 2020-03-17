Initial Layer Jerk
====
This setting determines the speed at which the nozzle can go through corners while the initial layer is being printed. This can be configured separately from the rest of the layers.

Going through sharp corners at great speeds not only causes the print head to vibrate horizontally. It can also cause the build plate to vibrate vertically. This affects bed adhesion negatively. Going through corners a bit more carefully during the first layer allows for more consistent bed adhesion, but will take longer to print.

Additionally, reducing the jerk will normally make the printer deposit more material in sharp corners because the nozzle slows down while the material flow has some delay in when the flow is reduced. These sharp corners are often where the print lets go of the build plate first due to warping. Depositing some extra material in those corners is advantageous then, since it'll make the corners stick better.

The individual structures of the print could all have different jerk values. There are separate settings for the infill, bottom side, outer and inner walls, support and prime tower. This setting will override all of those. Only the [Skirt/Brim Jerk](jerk_skirt_brim.md) setting will override this jerk, since the skirt and brim can only occur in the first layer.