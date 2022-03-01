Wipe Retraction Enable
====
If this setting is enabled, the material will be retracted throughout the wiping procedure. This can be configured separately from the [normal retractions](../travel/retraction_enable.md).

The wiping procedure makes the nozzle go all the way to the side of the printer, move back and forth there, and then move all the way back. This is essentially a very long travel move. Since this travel move is longer than the average travel moves throughout the print, you may want to have the material retracted during this procedure even if retractions are normally disabled.

Having the material retracted will reduce the amount of material that oozes during the wiping procedure. The material that is oozed during the wiping procedure will normally be wiped off by the brush. However this material is then lost. As a result, there will be some underextrusion just after the wipe has been completed since this material has oozed out instead of being placed in its proper location.

On the other hand, the retraction may take some time and cause unnecessary wear on the filament. If underextrusion is not a problem, disabling the retraction may save some time and improve reliability. This can work well if, for instance, the [infill is printed before the walls](../infill/infill_before_walls.md), because some underextrusion during the infill is not really a problem. 