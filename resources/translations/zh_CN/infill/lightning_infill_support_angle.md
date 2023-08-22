闪电形填充支撑角
====
闪电状填充图案仅用于从内部支撑打印件。此设置确定悬垂的最大角度，不仅是它将支撑的曲面的悬垂角度，还包括内嵌本身内部的悬垂角度。降低此设置会导致生成更多填充。增加该值将减少填充量。

图案从内部支撑打印的顶面，但仅支撑显著超过该角度的悬垂。该图案还具有以一定角度悬垂以创建分支树结构的端点，并且该分支结构的侧面具有内角以进一步到达特定区域。也可以分别使用[闪电形填充悬垂角](lightning_infill_overhang_angle.md)、[闪电形填充修剪角](lightning_infill_prune_angle.md)和[闪电形填充矫直角](lightning_infill_straightening_angle.md)设置单独控制悬垂的这三个方面。

<!--screenshot {
"image_path": "lightning_infill_support_angle_30.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
"infill_pattern": "lightning",
"wall_line_count": 0,
"top_layers": 0,
"lightning_infill_support_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "lightning_infill_support_angle_60.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
"infill_pattern": "lightning",
"wall_line_count": 0,
"top_layers": 0,
"lightning_infill_support_angle": 60
},
"colours": 64
}-->
![低悬垂角度，需要更多支撑](../images/lightning_infill_support_angle_30.png)
![高悬挑角度，允许陡峭的悬垂](../images/lightning_infill_support_angle_60.png)

增加此设置将大大减少所需的材料量，并缩短打印时间。但它也会导致下垂。这种下垂是在模型的内部，因此不能立即看到。但是，如果[顶层厚度](../top_bottom/top_thickness.md)不足，则可能会导致[枕形效应](../troubleshooting/pillowing.md)。因为填充物中的内角也被允许更多地悬垂，所以填充物很可能将沿着墙壁更高的地方开始。
