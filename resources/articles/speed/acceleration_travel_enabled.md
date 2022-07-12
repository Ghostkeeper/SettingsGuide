Enable Travel Acceleration
====
If this setting is enabled, travel moves get their own acceleration rates. The [Travel Acceleration](acceleration_travel.md) setting then controls the rate of acceleration during travel moves.

The acceleration value during the travel move will take on the value of the line that gets printed at the destination of the travel. For instance, when it is travelling towards infill, the acceleration during the travel move is the [Infill Acceleration](acceleration_infill.md). When it's travelling towards the outer wall, the acceleration will be the [Outer Wall Acceleration](acceleration_wall_0.md). This way it will effectively approach more sensitive structures a bit more carefully than other structures.

This setting is enabled by default, allowing control over the acceleration during travels. This is good for most situations, because an increased travel acceleration can save time, while such high acceleration would cause [ringing](../troubleshooting/ringing.md) when used for printing itself.

However there are two reasons why you might want to disable it:

* To change the acceleration rate for travel moves, Cura changes the acceleration back and forth very often. It switches between extruding and travelling frequently, especially with some infill patterns and with small details in the walls. The firmware needs to process these commands and may not be able to keep up with the necessary calculations. Disabling travel accelerations reduces that problem.
* Increasing the travel accelerations cause the printer to vibrate a lot. These vibrations are not quite stopped yet at the end of the travel move when printing needs to start. This can also lead to ringing at the end of a travel move. Disabling travel acceleration will cause the nozzle to approach the sensitive structures of the print (like the outer wall) with more care than less sensitive structures (like infill).