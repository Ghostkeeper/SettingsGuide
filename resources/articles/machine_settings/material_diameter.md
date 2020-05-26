Diameter
====
This setting describes the diameter of the filament that will be fed into the nozzle. It is important for Cura to calculate the extrusion rate correctly and to limit the number of retractions correctly.

Most printers expect the g-code to specify how far the extrusion wheel has to turn in order to extrude enough to print a line. This filament diameter is necessary to get the correct amount of material to flow. If the printer's firmware interprets extrusion amounts to be listed volumetrically, that is unnecessary, but it will still use the filament diameter to limit the number of retractions over a certain length of filament.

Most printers nowadays use filament with a diameter of 1.75mm. Another common diameter is 2.85mm.

**A material will only appear in the list of materials available to the printer, if the diameter of the filament is compatible with the extruder. Look into the Machine Settings panel of your printer (in the extruder's tab) to know which filaments your extruder train accepts.**