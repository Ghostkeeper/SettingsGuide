Cura assumes that multi-extruder printers have separate nozzles that can have separate temperatures. While one extruder is busy printing, the rest of the nozzles must be held at a lower temperature in order to prevent the material in the nozzle chamber from degrading and to prevent oozing. This lower temperature is the stand-by temperature.

![While the blue extruder is printing, the red extruder cools down to the stand-by temperature](images/temperature_regulation.svg)

A good stand-by temperature is low enough to protect the filament from degrading, which might clog the nozzle. It is low enough to prevent the material from oozing out of the nozzle. But it is also high enough to quickly continue printing when the other extruders are done.