The "topography" effect is when a sloped top or bottom side is printed with a small amount of layers, such that the boundaries between layers are spaced far enough apart that they become easy to see. It is named after [topographic maps](https://en.wikipedia.org/wiki/Topographic_maps) where the elevation differences are typically indicated with contour lines.

![You can see the edges of the layers clearly](../images/topography.jpg)

This effect is ubiquitous in 3D printing, and one of the easiest ways in which you can recognise that an object was 3D printed. It can be prevented, but preventing it typically reduces productivity significantly.

Layer height
----
Since the topography effect occurs when the borders between layers are spaced apart very far, the effect can be prevented by reducing the [layer height](../resolution/layer_height.md). When the layer height is reduced, the smaller vertical increments between layers will also result in smaller horizontal steps, which reduces the topography effect. Reducing the layer height greatly increases the printing time though.

Instead of reducing the layer height for the entire print, you can also reduce the layer height only for the shallow slopes of the print by using [Adaptive Layer Height](../experimental/adaptive_layer_height_enabled.md). This greatly reduces the topography effect while having a minimal impact on the printing time. However it is more difficult to tune the print for other qualities then since the tuning usually depends on the layer height.

Model adjustments
----
You can also consider rotating the model such that there are no more shallow slopes in the print. This usually involves printing a lot more support for your model though, which reduces productivity too, and the overhangs might not look as good.