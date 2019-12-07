With this setting, at the end of every outer wall, the nozzle will travel slightly further without extrusion, wiping the contour closed.

![A small travel move after completing the outer wall](images/wall_0_wipe_dist.png)

The goal of this feature is to reduce the visibility of the seam. When the wall is completed normally the bead is still slightly behind the nozzle. This little travel move connects the bead with the start of the contour, so that the seam is closed.

The seam will still be visible, but the result should be slightly better with a small wipe distance. Increasing this setting too much has no more effect since the nozzle travels beyond the seam, and may cause some underextrusion later as the nozzle chamber empties by oozing on the outer wall.

This effect is basically the opposite of [coasting](coasting_enable.md), which will stop extruding slightly before the contour is finished.