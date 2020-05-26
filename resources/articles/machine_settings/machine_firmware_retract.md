Firmware Retraction
====
Normally, Cura causes a retraction by controlling the movement of the feeder, commanding it to move the filament a bit back. If this setting is enabled, it will instead write a `G10` command to mean that the printer must retract the filament, or a `G11` command to unretract.

By choosing to use firmware retractions, the firmware of the printer controls how far and how fast to retract the filament. The printer may know more about its own geometry than Cura, so it may be able to decide better on how to retract the filament. However, this means that Cura is no longer in control of these retractions and Cura knows more about the print itself. Essentially, the slicer and the firmware have different information, and this setting decides which of the two gets to choose.

**Since this is a machine setting, this setting is not normally visible in the settings list.**