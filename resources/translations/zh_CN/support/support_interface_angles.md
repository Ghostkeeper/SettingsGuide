支撑接触面走线方向
====
通常，支撑接触面的方向应尽可能垂直于模型及其周围的支撑实体。如果已经自定义了顶/底线或支撑线的方向，最好也自定义支撑接触面的走线方向。此设置允许您自定义该方向。

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
![角度为 0° 和 90°](../images/support_interface_angles_0.png)
![角度为 45° 和 135°](../images/support_interface_angles_45.png)

可以为此设置填充多个角度，以逗号分隔。Cura将在各层之间交替使用这些角度。

理想情况下，支撑界接触面走线方向将被定向成垂直于它们所依赖的线以及依赖于它们的线。将其垂直定向可减少这些线必须桥接的距离，从而减少下垂并提高悬垂的质量。这在使用不是完全密集的支撑时尤其重要。
