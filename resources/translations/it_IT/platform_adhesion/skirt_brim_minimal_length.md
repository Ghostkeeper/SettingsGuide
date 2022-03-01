Skirt/Brim Minimum Length
====
This setting makes sure that the nozzle is primed enough before starting a print, by adding more skirt or brim lines than originally requested by the [Skirt Line Count](skirt_line_count.md) or [Brim Line Count](brim_line_count.md) setting. If the minimum length in this setting is not reached by the total circumference of all the skirt or brim lines added together, more contours will be added.

The aim of this setting is to ensure that the material is sufficiently primed before starting with the print. The value of this setting should be set such that the volume extruded by this minimal length is just enough to prime the nozzle before a print.

**The disallowed areas around the build plate can't take this setting into account because its effect is not known before slicing. Placing tiny objects at the edge of your printer when this setting is high can cause the printer to move outside of the bounds of the print volume.**