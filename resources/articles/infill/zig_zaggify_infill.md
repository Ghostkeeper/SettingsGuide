Connect Infill Lines
====
This setting connects the endpoints of the infill pattern, where the infill meets the inner wall or skin, using a line that follows the edge of the infill area.

![No connected infill lines](../images/zig_zaggify_infill_disabled.png)
![Connected infill lines](../images/zig_zaggify_infill_enabled.png)

This converts the entire infill pattern into a single or very few lines. Converting it into a single line is not always possible. The starting point of this line is arbitrary, so it might not be the same for every layer, especially if the shape that the infill is contained in is different from layer to layer.

Connecting the infill has a couple of benefits, but also some downsides:
* Your part will be stronger in the end, since there is practically half a contour extra.
* The infill will adhere better to the walls due to increased surface area, which also makes the part stronger.
* The flow rate will be held more constant, allowing you to print the infill at greater speed without flow problems. This is especially important for materials that are hard to extrude properly.
* Significantly fewer retractions will be made during the printing of the infill, which prevents the material from grinding.
* The effect of the [Infill Overlap](infill_overlap.md) setting is amplified, since a greater part of the infill lines will be made to overlap the walls.
* It will take more material to print the infill.
* Usually it will take more time to print the infill, since travel moves are normally faster than printing infill lines.
* The infill will typically shine more through the walls, since it gets pushed into a greater portion of the walls.