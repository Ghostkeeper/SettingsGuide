If [Spiralize](magic_spiralize.md) is enabled, this setting enables or disables the most distinguishing feature of Spiralize mode: Instead of printing each layer one after the other at intervals of height, the height is gradually increased over the course of the layer.

Since the Spiralize mode causes only the walls to be printed for most of the layers with a single contour, this single contour will take the form of a spiral, lending the name to the Spiralize feature. The first and last layers of the print get their flow rate gradually reduced in order to prevent overextrusion and achieve the correct height.

Because the nozzle is gradually moved up to the next layer height throughout the layer, there will no longer be any seam where the nozzle moves to the next layer. Effectively this removes the Z seam.

On the other hand, the layer is moved up or down by half a layer height. This is less accurate. It can have a blurring effect on fine details in the print.

This setting is not effective at removing the seams if there is more than one contour to print on a layer. It'll still have to stop extruding after the contour to move to the next printed piece. This leaves a seam anyway.

**This effect is not visible in layer view due to rendering limitations.**