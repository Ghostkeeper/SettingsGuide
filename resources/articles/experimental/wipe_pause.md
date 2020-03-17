Wipe Pause
====
With this setting, the nozzle can be made to pause briefly just after the wiping procedure has completed.

The wiping procedure is fairly long, for a travel move. The nozzle moves all the way to the side of the build volume and moves back and forth there, and then needs to travel back to the print. During this time there will be a lot of oozing and a [longer retraction](wipe_retraction_amount.md) may be necessary. After the unretraction, there will be a period when the flow out the nozzle needs to get started still. This pause allows the nozzle chamber to come back to pressure when the material is unretracted again, allowing the first line to be printed properly without significant underextrusion.

Pausing for too long causes a blob to appear where the nozzle lands. Depending on the [printing order](../infill/infill_before_walls.md), this may not be significant since the blob may appear on the inside of the print where it's not visible. However the material used for this blob will not be used for the subsequent printed lines, causing underextrusion there still. This setting requires some careful tuning.