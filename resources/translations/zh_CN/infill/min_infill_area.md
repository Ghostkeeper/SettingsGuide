最小填充区域
====
此设置会导致填充非常小的碎片时使用皮肤图案而不是填充图案，从而使它们完全实心。

<!--screenshot {
"image_path": "min_infill_area_disabled.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-64, 224, 82],
"settings": {
"wall_line_count": 0,
"min_infill_area": 0
},
"colours": 32
}-->
<!--screenshot {
"image_path": "min_infill_area_150.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-64, 224, 82],
"settings": {
"wall_line_count": 0,
"min_infill_area": 150
},
"colours": 32
}-->
![设置为0，模型的底座将由填充图案填充](../images/min_infill_area_disabled.png)
![设置为150，底座将由皮肤填充](../images/min_infill_area_150.png)

有时，非常小的中空区域不能被填充物适当地填充，因为填充线将是如此之短，以至于材料没有时间适当地流动。此设置会使填充区域由皮肤填充，从而使填充区域更坚固，并防止皮肤和填充区域之间出现边界。

将此设置设置为0可有效禁用此功能。
