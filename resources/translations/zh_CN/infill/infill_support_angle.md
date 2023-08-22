填充悬垂角
====
使用填充支撑时，此设定可确定需要获得支撑的表面的最小悬垂角度。这与普通支撑的[悬垂角度](../support/support_angle.md)设置类似。

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
<!--screenshot {
"image_path": "infill_support_angle_high.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
"wall_line_count": 0,
"infill_support_enabled": true,
"infill_support_angle": 60
},
"colours": 64
}-->
![低角度可产生更多支撑](../images/infill_support_angle_low.png)
![高角度会产生较少的支撑](../images/infill_support_angle_high.png)

增加此角度将导致填充支撑较少的顶面。这节省了打印时间和材料，但会导致顶部皮肤下垂多一点。
* 此值为0 °时，其作用类似于正常填充。它支撑所有部分。
* 值为90 °时将移除所有填充材料。
