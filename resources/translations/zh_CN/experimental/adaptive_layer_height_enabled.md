使用自适应图层
====
自适应图层将根据模型的表面特征局部调整打印图层的厚度，以优化打印时间和质量。在坡度较浅的地方，图层会做得较薄；在壁较陡的地方，图层会做得较厚。这样做的目的是尽可能快速地打印，但仍在需要时精细打印。

<!--screenshot {
"image_path": "adaptive_layer_height_enabled.png",
"models": [{"script": "barn.scad"}],
"camera_position": [-108, -229, 118],
"settings": {
"adaptive_layer_height_enabled": true,
"layer_height": 0.2
},
"colour_scheme": "layer_thickness",
"colours": 128
}-->
![使用 "层厚度" 颜色方案，可以看到较薄的层为蓝色，而较厚的层为黄色](../images/adaptive_layer_height_enabled.png)

图层高度调整后，将使图层边缘之间的水平距离保持不变。平缓的表面具有较大的水平位移和较小的垂直位移，因此进行小的垂直位移来保持水平位移恒定。陡峭的表面具有较小的水平位移和较大的垂直位移，因此进行大的垂直位移来保持水平位移恒定。因此，层的地貌效应保持恒定。两个相邻层之间的最大距离保持在[自适应图层地形尺寸](adaptive_layer_height_threshold.md)设置的恒定距离。

如果模型在同一高度上同时具有平缓面面与陡曲面，则层厚度取两者中较小的一个。这有时会使图层高度变得不必要的小，因为它旁边有一个水平曲面。这可以在上面的截图中以及在左侧筒仓高度的一半看到。

为了提高打印质量，"自适应图层"受到了严格的限制。不允许层高度与原始[层高](../resolution/layer_height.md) 设置的偏差超过指定的[自适应图层最大变化](adaptive_layer_height_variation.md)。两个相邻层之间的层高度差不能超过特定的 [自适应图层变化步长](adaptive_layer_height_variation_step.md)。这会使层厚度逐渐过渡，而不是突然一分为二的从一层到下一层。

"自适应图层"可以显著缩短打印时间，而不会降低打印质量，甚至在某些情况下还可以提高质量。调整层厚度的效果是巨大的。在大多数情况下，由于在模型垂直的地方使用较厚的层，打印时间将大大减少。[地貌效应](../troubleshooting/topography.md) 也会降低，因为图层在水平方向上的间距更近。

然而，该特征也会引入许多问题。
* 随着层高度的改变，通常还需要调整一些其它设置，例如喷嘴温度。"自适应图层"也不会自动调整这些设置。这可能会使打印效果欠佳，例如：悬垂在较低的打印温度下打印更好。
* 如果在整个图层上更改了图层的一小部分中某个小要素的图层高度，则在图层的其余部分中将显示条带。
* 垂直距离也会无意之中跟随调整。这可能会对打印质量产生负面影响。例如， [顶层/底层厚度](../top_bottom/top_bottom_thickness.md) 通常会变小，因为Cura会将[顶部层数](../top_bottom/top_layers.md) 设置保持为真，并且图层会变薄。这可能会导致枕形效应。受影响可能不再正确的设置包括：
  * [顶层厚度](../top_bottom/top_thickness.md)
  * [底层厚度](../top_bottom/bottom_thickness.md)
  * [最大扩展皮肤角度](../top_bottom/max_skin_angle_for_expansion.md)
  * [渐进填充步阶高度](../infill/gradual_infill_step_height.md)
  * [渐进支撑填充步阶高度](../support/gradual_support_infill_step_height.md)
  * [填充层厚度](../infill/infill_sparse_thickness.md)
  * [支撑填充层厚度](../support/support_infill_sparse_thickness.md)
  * [支撑Z距离](../support/support_z_distance.md)
  * [支撑顶板厚度](../support/support_roof_height.md)
  * [支撑底板厚度](../support/support_bottom_height.md)
  * [支撑悬垂角度](../support/support_angle.md)
  * [支撑梯步阶高度](../support/support_bottom_stair_step_height.md)
  * [塔顶板角度](../support/support_tower_roof_angle.md)
  * [渗出罩角度](../dual/ooze_shield_angle.md)
  * [最大模型角度](../experimental/conical_overhang_angle.md)
