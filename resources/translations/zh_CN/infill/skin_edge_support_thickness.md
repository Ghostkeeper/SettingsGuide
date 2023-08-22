皮肤边缘支撑厚度
====
当打印凹面形状时，将有一些顶部皮肤在填充的中途结束。此设置会通过填充添加一条额外的线，以支撑皮肤的边缘，从而使其下垂程度有所降低。

<!--screenshot {
"image_path": "skin_edge_support_thickness_0.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.4)", "translateZ(-2.5)"]
}
],
"camera_position": [-29, 29, -50],
"settings": {
"infill_sparse_density": 10,
"bottom_thickness": 0,
"skin_edge_support_thickness": 0
},
"colours": 128
}-->
<!--screenshot {
"image_path": "skin_edge_support_thickness.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.4)", "translateZ(-2.5)"]
}
],
"camera_position": [-29, 29, -50],
"settings": {
"infill_sparse_density": 10,
"bottom_thickness": 0,
"skin_edge_support_thickness": 1
},
"colours": 128
}-->
![填充对皮肤边缘的支持不好](../images/skin_edge_support_thickness_0.png)
![为皮肤边缘下面的填充添加一个轮廓](../images/skin_edge_support_thickness.png)

穿过填充物中的间隙的单条线仍将下垂，因此可以在需要支撑的皮肤边缘下方的多个层上绘制该线。此设置配置皮肤边缘下方的线的垂直厚度。或者，您可以直接调整将绘制此线的皮肤边缘下方的[支撑层数](skin_edge_support_layers.md)。

增加此厚度通常会对打印产生以下影响：
* 皮肤的边缘将得到更好的支持，导致更光滑的顶侧，因为皮肤可以完全从一侧桥接到另一侧。
* 打印时间稍长，会使用更多的材料。

如果填充率很高，此设置几乎不会对顶面产生任何影响，并可能导致填充出现[挤出过度](../troubleshooting/overextrusion.md)。此时最好保持在0mm。
