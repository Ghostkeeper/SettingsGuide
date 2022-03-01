Layer Start X
====
If there are multiple parts to print to a layer, Cura will optimise the order in which these parts are printed. To allow the part to cool down before printing the next layer, it will print every layer in roughly the same order. The Layer Start X and [Layer Start Y](layer_start_y.md) settings determine which part will be printed first: The part that is closest to the specified coordinates. This setting determines the X coordinate of that.

This is a different setting than the Z seam. The Z seam alignment settings only determine where the printer will start printing the contour of a part, whereas this setting determines which part it will start with.

If your printer does something specific when starting with a new layer or when switching extruders, it's a good idea to set these coordinates to the location where the print head ends up when it is ready to continue printing. This minimises travel moves and oozing.

These coordinates are in the g-code coordinate system, which is different from the coordinate system that Cura uses to show the placement of objects.