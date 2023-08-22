支撑底板走线方向
====
通常，支撑底板的方向应尽可能垂直于其上方的支撑和下方的模型。如果已经定制了顶部表面或支撑的走线方向，支撑底板的走线方向也最好这样做。此设置允许您自定义支撑底板的走线方向。

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
![屋顶和地板的角度均为0°和90°](../images/support_interface_angles_0.png)
![屋顶和地板的角度均为45°和135°]](../images/support_interface_angles_45.png)

可以为此设置填充多个角度，以逗号分隔。Cura将在各层之间交替使用这些角度。

理想情况下，支撑底板走线方向应垂直于其所在的模型以及其上的支撑的走线方向。将它们垂直定向减少了这些线必须桥接的距离，因此减少了下垂并提高了支撑件的稳定性。
