填充支撑
====
启用时，此选项会将填充视为支撑。然后，将仅在需要的位置生成填充，以支持顶面。它的行为就像模型是空心的，并在模型内部生成支撑，但此支撑是使用填充设置生成的。

<!--screenshot {
"image_path": "infill_support_enabled_disabled.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
"wall_line_count": 0,
"infill_support_enabled": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_support_angle_low.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
"wall_line_count": 0,
"infill_support_enabled": true,
"infill_support_angle": 40
},
"colours": 64
}-->
![普通填充](../images/infill_support_enabled_disabled.png)
![已启用填充支撑](../images/infill_support_angle_low.png)

* 这样可以在填充时节省大量材料，而视觉效果却损失非常小。
* 启用此选项后，顶面可能会下垂多一些。
* 但是，填充物的水平强度可能大幅降低。在许多情况下，如果壁是陡坡的一部分，则壁后不会有填充。
