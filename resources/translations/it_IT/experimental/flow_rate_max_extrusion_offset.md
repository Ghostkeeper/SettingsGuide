Flow Rate Compensation Max Extrusion Offset
====
Flow rate compensation is an experiment similar to the [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) functionality of Marlin. The purpose of flow rate compensation is to compensate for underextrusion and overextrusion when the flow rate of material out the nozzle changes. This setting puts a limit on the distance that the material will be retracted or pushed forward in order to compensate for flow changes.

Flow rate compensation will move the filament further ahead from its original position or farther behind during printing. This setting limits how far away the filament is allowed to move from its original position.

The compensation will introduce extra filament movements throughout the print. These make the print head slow down from time to time to move the filament. To reduce the effect of this, you can limit the distance that the filament moves. This prevents the print head from needing to slow down for the feeder to keep up. However, this makes the flow rate compensation less effective.