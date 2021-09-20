Spiralize Outer Contour
====
Spiralize Outer Contour is a trick.

When printing layer by layer, the nozzle normally needs to move from one layer to the next. This movement causes the nozzle to stand almost still for a fraction of a second, which leaves a seam on the surface called the Z seam. This setting is meant to prevent that and more. It greatly simplifies the printing process by leaving out many aspects of it.

When spiralising the model, the model will not get any infill or any tops. It will only get one wall and a bottom. Crucially, if [Smooth Spiralized Contours](smooth_spiralized_contours.md) is enabled, height of the nozzle will gradually be increased over the coarse of a layer. This way a spiral is created following the contour of the model. There will be no movement moving from one layer to another, because the nozzle has already gradually moved towards the next layer.

Spiralize mode is common among many slicers. It is also known as "vase mode" sometimes, because it is a good way to print vases. Some other properties include:
* Prints extremely fast.
* The surface becomes very smooth. There is no [Z seam](../troubleshooting/seam.md) any more where it moved to the next layer if [Smooth Spiralized Contours](smooth_spiralized_contours.md) is enabled.
* It will not be very strong. If the model is too big, it tends to [split](../troubleshooting/layer_splitting.md) due to the thin wall.
* While removing the seam helps to make the print watertight, it is difficult to get the print to be water tight if it has any size. For that, it's advisable to have at least 2 walls. Spiralizing the outer contour is impossible then.

**Spiralize will not work well with prints with many horizontal surfaces. It doesn't handle overhangs at all, and doesn't print top surfaces so nothing will be able to lean on a horizontal surface. It also doesn't work well when there are multiple parts on a layer.**