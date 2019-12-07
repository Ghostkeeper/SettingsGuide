This setting enables a completely different mode of printing called Wire Printing. When Wire Printing is used, the printer will not make a solid object, but only a triangular mesh of the outside shape out of thin wires.

This technique has a number of advantages:
* It prints much faster than a solid object.
* It uses but a fraction of the material that normal printing would use.
* It looks special, as if manually constructed with a 3D printing pen.

The resulting object is not functional however. It will have roughly the correct size, which makes it useful for prototyping the feel of scale of the print, though the size will not be very accurate either. The resulting object is extremely fragile, not only during printing but afterwards too. It is hard to take it off the build plate without damaging it. The model will also lose most of its detail.

Wire Printing works by laying down rings of material with a fairly wide vertical spacing of several millimetres. In between these rings it will draw a saw-tooth shape that will allow the next ring to rest on top of the previous one. Where the surface of the model goes horizontal, a similar technique is used to close the top. In the roof, there are concentric rings held together by a saw-tooth shape, carefully suspended in mid-air by building from outside (where it can rest on a wall) inwards.

Wire Printing only really works reliably with shapes that are almost completely vertical, similar to the type of model that would work well with [Spiralize Mode](../blackmagic/magic_spiralize.md). If the surface is horizontal over large areas, the roof closing technique has to bridge an extremely far distance. This will most likely fail then. If the model then continues upwards halfway across a horizontal surface, it will almost certainly be printed in mid-air.

**Cura's layer view will not display Wire Printing correctly directly after slicing. However the result can still be previewed by saving the g-code to disk and opening that g-code with Cura again.**