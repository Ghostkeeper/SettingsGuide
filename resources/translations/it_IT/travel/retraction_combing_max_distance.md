Max Comb Distance with No Retract
====
Normally, retractions are unnecessary if the nozzle only travels through the inside of the model. Any stringing that the nozzle leaves in its wake will be on the inside anyway, where they are invisible. However if travel moves are very large, the lost material from the stringing may manifest itself as underextrusion in whatever is printed afterwards.

For that reason, this setting allows you to choose a distance of travel moves, beyond which the travel move will be retracted anyway, even if no walls are being crossed. This causes more retractions which can wear down the filament and slow down the print, but it may prevent some underextrusion in places.