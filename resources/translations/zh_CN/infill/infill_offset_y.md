填充 Y 轴偏移量
====
通常，填充图案会以3D模型的中心为中心。此设置与[填充 X 轴偏移量](infill_offset_x.md) 一起允许移动图案的中心。此设置可调整中心的Y坐标。

<!--screenshot {
"image_path": "infill_offset_xy_0.png",
"models": [
{
"script": "hexagonal_prism.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 0, 90],
"settings": {
"top_layers": 0,
"infill_pattern": "triangles",
"infill_offset_x": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_offset_y_2.png",
"models": [
{
"script": "hexagonal_prism.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 0, 90],
"settings": {
"top_layers": 0,
"infill_pattern": "triangles",
"infill_offset_y": 2
},
"colours": 64
}-->
![填充居中](../images/infill_offset_xy_0.png)
![上移2mm](../images/infill_offset_y_2.png)

当以较低填充密度打印时，您可以通过此设置非常精确地定位填充，以便将各条填充线放置在最需要增强的位置上。
