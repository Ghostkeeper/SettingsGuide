Enable Prime Blob
====
When enabled, this causes Cura to output a command for the printer to prime, just before the extruder is first used. The printer will prime by creating a small blob of material on the build plate.

Priming is meant to get the material to flow properly. If the prime blob is not enabled, the printer will prime during the skirt or brim instead. That's the major use case for the skirt in the first place, but for a brim this will reduce the adhesion strength of the brim slightly.

The effect of this setting on the g-code is that Cura will put the M280 command in a certain location. **This currently only works on Ultimaker printers since the Ultimaker 3** since they are the only ones that implement the M280 command. For other printers the setting will not be visible.