支撑填充走线方向
====
通常，支撑图案的方向是使走线与其支撑的大多数物件垂直。这样，被支撑材料必须桥接的距离被最小化。通过此设置，可自定义支撑线的方向。

<!--screenshot {
"image_path": "support_infill_angle_0.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"support_enable": true,
"support_infill_angles": [0]
},
"layer": 160,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_angle_30.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"support_enable": true,
"support_infill_angles": [30]
},
"layer": 160,
"colours": 64
}-->
![角度为 0°](../images/support_infill_angle_0.png)
![角度为30°](../images/support_infill_angle_30.png)

如果已调整[顶层/底层走线方向](../top_bottom/skin_angles.md)，最好相应地调整支撑线的角度，使其仍垂直于打印底面的线条。这允许这些底线适当地靠在支撑上，而不是落在支撑线之间。这对于直线和锯齿形[支撑图案](support_pattern.md)尤为重要，因为在这些图案中，支撑线之间存在不提供任何支撑的长切线。

<!--if cura_version >= 4.3-->
**在Cura 4.3中，此设置已删除，取而代之的是[支撑图案](support_infill_angles.md)。**
<!--endif-->
