Wipe Retraction Extra Prime Amount
====
If [retracting during the wipe procedure](wipe_retraction_enable.md), the material will be unretracted after the wiping procedure has completed. When this happens, you may want the material to be pushed a little bit further than the original [retraction distance](wipe_retraction_amount.md) to compensate for any material that was lost despite the retraction. This may be configured separately from the [normal extra prime amount](../travel/retraction_extra_prime_amount.md).

The wiping procedure makes the nozzle go all the way to the side of the printer, move back and forth there, and then move all the way back. This is essentially a very long travel move. Since this travel move is longer than the average travel moves throughout the print, more material may have been lost due to oozing. To compensate for this, you may need to prime more after the wipe procedure than after normal travel moves.

If too much extra material is primed, there will be some overextrusion. This manifests itself as a blob in the location where the nozzle lands after the wiping procedure.