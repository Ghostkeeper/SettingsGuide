Overextrusion is a term used when the printer extrudes too much material in one place. This causes the material to flow over to the sides or upwards, which makes the surface very rough and irregular. It can also cause [stringing](stringing.md) and lots of [blobs](blobs.md).

![Massive overextrusion occurred in this print](../images/overextrusion.jpg)

Temperature control
----
The most common cause of overextrusion is printing too hot. If the [printing temperature](../material/material_print_temperature.md) is set too high, then the material will have a lower viscosity, making it flow out the nozzle without control. Typically the result is overextrusion in some areas like the outer walls, but underextrusion in others like the infill.

To remedy this you need to reduce your temperature gradually. Take a careful look at the specifications sheet of the material you're printing with to see which temperature range is acceptable and reduce your printing temperature towards the lower end of that range.

Filament diameter
----
There are several standards for filament diameters. The most common ones are 1.75mm and 2.85mm, but 3.00mm is also still around. Apart from that, not all manufacturers produce their filament with a consistent diameter. If your filament is wider than what Cura expects, you will extrude too much material, since Cura instructs the printer to extrude a certain length of filament which will have too much volume then.

To fix this, first measure the actual diameter of the filament using calipers. It is best to measure this in several spots, in case it varies, and at various angles around the circumference. Take the average of these measurements. This average can be filled into Cura in the Material Management page, as a property of the material. If the diameter can't be edited because it's a built-in material, you may need to duplicate the material first. It should then allow you to edit the diameter.

Directly adjusting flow rate
----
If it's for the rest unknown what is causing this overextrusion, you can also directly adjust the [flow rate](../material/material_flow.md). Reduce the flow rate until your surface appears smooth again. This can compensate for some unknown factor directly.