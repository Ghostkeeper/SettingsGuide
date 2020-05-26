Offset with Extruder
====
This setting decides whether Cura should write coordinates for the print head to move to, or for the nozzle to move to.

If your printer has just a single nozzle, the coordinate system of your printer is most likely aligned to your nozzle. This means that moving to position [50,50] actually moves the tip of the nozzle to that position. If your printer has multiple nozzles though, and those nozzles are next to each other in the print head, then it does matter.

Some printers would move the print head to the same location regardless of which nozzle is currently activated. While the g-code might command the printer to move to position [50,50], the tip of the currently active nozzle might be moved to position [68,50] instead since it is, for instance, 18mm to the right of the first nozzle. If this is the case, this setting should be enabled.

Other printers automatically adjust the position of the print head such that the active nozzle is moved to the position indicated in the g-code. This means that if the g-code commands the printer to move to position [50,50], the currently active extruder would move to that position. The print head itself would move a bit to the side to position the active extruder there. If your printer behaves in that way, this setting should be disabled.

**Since this is a machine setting, this setting is not normally visible in the settings list.**