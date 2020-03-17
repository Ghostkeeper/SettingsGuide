Wipe Move Distance
====
With this setting you can define how wide the wipe movements need to be. The nozzle will move this distance for [every wiping movement](wipe_repeat_count.md).

Initially the nozzle will be placed just beyond the wiping brush in a [certain X coordinate](wipe_brush_pos_x.md). The distance indicated in this setting needs to be such that moving this distance places it on the other side of the brush. Moving too far introduces unnecessary movements and may cause the nozzle to move back into the build volume, which may cause it to unnecessarily strike the model if [Z hops are not enabled](wipe_hop_enable.md). Moving not far enough may prevent it from striking the brush properly.

The distance may also be negative. The nozzle will wipe into the other direction then. Depending on your choice of [X coordinate](wipe_brush_pos_x.md), this may be necessary in order to wipe in the correct direction.