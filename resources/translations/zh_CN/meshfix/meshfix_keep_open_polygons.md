保留断开连接的面
====
Cura需要知道模型内部的位置，以便用材料填充体积块。如果模型没有正确地无缝连接，则这是不明确的。通常情况下，Cura不会打印未正确闭合的零件。

启用此设置后，将保留周边未正确闭合的图层。周边将用直线人工封闭。这可能会修复某些曲面中有小间隙的模型。但是，它也可能误解模型的内部结构。

<!--screenshot {
"image_path": "meshfix_keep_open_polygons_shell.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"layer": -1
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_disabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
"meshfix_keep_open_polygons": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_enabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
"meshfix_keep_open_polygons": true
},
"colours": 64
}-->
![此立方体缺少一个角](../images/meshfix_keep_open_polygons_shell.png)
![通常不会打印未闭合的图层](../images/meshfix_keep_open_polygons_disabled.png)
![启用此设置后，形状将被人工闭合](../images/meshfix_keep_open_polygons_enabled.png)

X射线视图将以红色显示可使用此设置闭合的间隙。
