支撑顶板走线方向
====
通常，支撑顶板的方向应尽可能垂直于其上方的模型和下方的支撑体。如果底部线或支撑线的方向已定制，则最好也定制支撑顶部走线的方向。此设定可让您自订该方向。

<!--screenshot {
"image_path": "support_interface_angles_0.png",
"models": [
{
"script": "plug.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 36, 92],
"settings": {
"support_enable": true,
"support_interface_enable": true,
"support_interface_pattern": "lines",
"support_interface_angles": [0, 90]
},
"layer": 118,
"colours": 128
}-->
<!--screenshot {
"image_path": "support_interface_angles_45.png",
"models": [
{
"script": "plug.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 36, 92],
"settings": {
"support_enable": true,
"support_interface_enable": true,
"support_interface_pattern": "lines",
"support_interface_angles": [45, 135]
},
"layer": 118,
"colours": 128
}-->
![屋顶和地板的角度均为0 °和90 °](../images/support_interface_angles_0.png)
![屋顶和地板的角度均为45°和135°](../images/support_interface_angles_45.png)

可以为此设置填充多个角度，以逗号分隔。Cura将在各层之间交替使用这些角度。

理想情况下，支撑顶板走线的方向应垂直于顶板所在的支撑线以及顶板所支撑的模型线。将其垂直定向可减少这些线必须桥接的距离，从而减少下垂并提高悬垂的质量。这在使用不是完全密集的支撑时尤其重要。
