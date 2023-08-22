闪电形填充悬垂角
====
闪电型填充将仅从内部支撑模型的顶侧，即模型悬垂的位置。此设置确定模型内部的闪电所支持的悬垂角度。

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
"image_path": "lightning_infill_overhang_angle_70.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
"infill_pattern": "lightning",
"wall_line_count": 0,
"top_layers": 0,
"lightning_infill_support_angle": 30,
"lightning_infill_overhang_angle": 70
},
"colours": 64
}-->
![30度以内的悬垂未被支撑](../images/lightning_infill_support_angle_30.png)
![70度时, 只留下了球体非常顶部的支撑。](../images/lightning_infill_overhang_angle_70.png)

增大此角度将减少生成的填充量。如果不是一个非常陡峭的悬垂，那么顶部表面将得到较少的支撑。这节省了时间和材料，但也可能导致顶表面在某些地方下垂。结果可能导致[枕形效应](../troubleshooting/pillowing.md) 或者粗糙的表面。

与父设置[闪电形填充支撑角](lightning_infill_support_angle.md)相反，该设置并不影响填充图案自身的悬垂。
