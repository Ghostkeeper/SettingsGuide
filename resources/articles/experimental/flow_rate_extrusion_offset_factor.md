Flow Rate Compensation Factor
====
Flow rate compensation is an experiment similar to the [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) functionality of Marlin. The purpose of flow rate compensation is to compensate for underextrusion and overextrusion when the flow rate of material out the nozzle changes. This setting configures the magnitude of the effect.

The flow rate compensation moves the filament forward by the extra material that is needed in the next second, during every move. In between every move, there are three possible scenarios.
* If the two adjacent movement commands have the same flow rate (because their line width, layer height and speed are the same), then the advancement will also be the same. The filament will not be moved in any direction in between these lines.
* If the flow rate increases with the next line, the filament is moved further forward during the second line. This increases the pressure in the nozzle chamber, such that the material can then extrude faster during the printing of the line and the lines following.
* If the flow rate reduces with the next line, the filament is moved back during the second line. This reduces the pressure in the nozzle chamber, such that the material will slow down during the printing of the second line and the lines afterwards.

The distance that the filament is moved is equal to the amount of material that would be extruded each second during the line (if the line were long enough to print a full second). However using this setting, this distance can be adjusted. Increasing the factor will make the compensation effect stronger. Reducing it will make the compensation effect weaker. Higher factors will also take more time to print, since the filament needs to be moved up and down more.

If this flow rate compensation is activated, the pressure inside the nozzle chamber should be better equipped to handle the upcoming flow rate. This can reduce both underextrusion and overextrusion and will give the object more accurate dimensions.

However the compensation is applied during one single line. This may sometimes be a short line, during which the filament has to move very quickly. The print head may need to slow down for the feeder to keep up then, which will cause a blob to appear. Sometimes this may be a long line, which reduces the strength of the effect. This makes the entire feature of compensation for extrusion rates unreliable, and is the reason why this setting is still experimental.