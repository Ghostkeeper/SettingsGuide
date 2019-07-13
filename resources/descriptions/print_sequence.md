When multiple models are placed on the build plate, this determines the order in which the layers for these objects are printed. There are two options.

All at Once
----
All objects will be printed at the same time, meaning that the layers will be printed from bottom to top for all objects at the same time. It will print one layer of each object before moving on to the next layer.

This has two major advantages:
* The previous layer gets more time to cool down, leading to better quality when printing small objects.
* The full build volume can be used for your print.

One at a Time
----
Objects will be printed one by one, meaning that it'll print all layers of one object and then move back down to the build plate to print the next object.

The major advantages of this mode are:
* If the print fails for whatever reason, all objects that were completed before the failure are completely fine to use.
* Fewer travel moves are required to move back and forth between the models. This saves some printing time and reduces the number of scars on the surface where the nozzle exited and entered the object.

This mode comes with a few constraints though, in order to prevent colliding the head and gantry with the model.
* You cannot print any objects taller than the gantry height of your printer. The gantry height can be adjusted in the printer's Machine Settings dialogue. This gantry height indicates how much vertical distance there is between the nozzle's tip and the system that carries the print head. The reason for this limitation is that the print head will have to move down to the build plate to print the second object. This means that the first object may get hit by the gantry as the second object is printed. In theory the last printed object may be allowed to be higher than the gantry, but for simplicity Cura won't allow it anyway.
* The objects must be spaced farther away from each other, in order to prevent the print head from hitting the previously printed models on the side.
* The order in which the objects are printed is fixed and optimised in order to allow objects to be printed more closely together. If your print head is not symmetrical, this can save a lot of space on the build plate.

**One at a Time is only available in single extrusion. If you're using a multi-extrusion printer, you must deactivate all but one extruder for this setting to appear.**