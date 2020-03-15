Wipe Retraction Distance
====
This setting configures how far to retract the material while the wiping procedure is going on. This can be configured separately from the [normal retraction amount](../travel/retraction_amount.md).

The wiping procedure makes the nozzle go all the way to the side of the printer, move back and forth there, and then move all the way back. This is essentially a very long travel move. Since this travel move is longer than the average travel moves throughout the print, you may want to increase the retraction distance during wipes beyond the distance used during ordinary printing.

Retracting the material farther will take more time and wear down the filament faster, but will reduce the amount of material lost due to oozing.