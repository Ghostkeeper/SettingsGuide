Enable Coasting
====
If this setting is enabled, the nozzle will stop extruding material slightly before closing up a wall contour. The idea is that the nozzle chamber can then empty itself on the last bit of line there, which reduces the pressure on the nozzle and allows it to be blocked by the start of the contour. This then produces less of a seam where the contour is started and reduces stringing in the subsequent travel move.

![In layer view, the seam is easy to see if coasting is enabled, because there is a travel move there then](../images/coasting_enable.png)

Enabling coasting is intended to reduce the visibility of the seam in the walls. If you normally have big fat seams, enabling this can reduce that effect. It is basically the opposite of what the [Outer Wall Wipe Distance](../shell/wall_0_wipe_dist.md) does, so it is a good idea to try reducing the wipe first before attempting coasting.

Coasting will always produce underextrusion, in theory. Whether this is visible in the actual print or not depends on the circumstances. Coasting tends to be somewhat more effective with printers using direct drive. If your printer has a direct drive, you'll want to reduce the [coasted volume](coasting_volume.md) to a lower value than when using Bowden tubes or flexible drive shafts, because the reaction of the flow rate is much faster then. With Bowden-style feeding systems it will also be much harder to control the coasting amount to effectively reduce the seam's visibility.