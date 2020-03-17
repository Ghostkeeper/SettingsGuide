Initial Layer Print Jerk
====
This setting determines the speed at which the nozzle can go through corners while the initial layer is being extruded. This can be configured separately from the travel moves during the initial layer.

Reducing the jerk will make the printer deposit more material in sharp corners because the nozzle slows down while the material flow has some delay in when the flow is reduced. These sharp corners are often where the print lets go of the build plate first due to warping. Depositing some extra material in those corners is advantageous then, since it'll make the corners stick better. This effect is not present during the travel moves of the initial layer. For this reason, the jerk during the extrusion of the first layer is normally a bit lower than the jerk during travel moves of the first layer.

The individual structures of the print could all have different jerk values. There are separate settings for the infill, bottom side, outer and inner walls, support and prime tower. This setting will override all of those. Only the [Skirt/Brim Jerk](jerk_skirt_brim.md) setting will override this jerk, since the skirt and brim can only occur in the first layer.