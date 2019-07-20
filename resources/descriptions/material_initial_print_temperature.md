After being on stand-by while different extruders have been printing, the nozzle will start at a slightly lower temperature. It then immediately heats up to the ordinary printing temperature once the printing has started.

![The extruder switch happens at a slightly lower temperature than the normal printing temperature](temperature_regulation.svg)

Restarting the print at a slightly lower temperature reduces the amount of oozing while the nozzle is standing by. After all, most of the oozing happens while the nozzle is at its highest temperature. Lowering this temperature effectively causes it to start printing at a slightly lower temperature so that this oozing would occur during printing when it's actually desired.