支撑墙行数
====
此设置将在支撑周长周围添加许多壁。

<!--screenshot {
"image_path": "support_wall_count_0.png",
"models": [{"script": "plug.scad"}],
"camera_position": [0, 66, 169],
"settings": {
"support_enable": true,
"support_pattern": "lines",
"support_offset": 0.2,
"support_wall_count": 0
},
"layer": 236,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_wall_count_3.png",
"models": [{"script": "plug.scad"}],
"camera_position": [0, 66, 169],
"settings": {
"support_enable": true,
"support_pattern": "lines",
"support_offset": 0.2,
"support_wall_count": 3
},
"layer": 236,
"colours": 64
}-->
![没有额外的壁](../images/support_wall_count_0.png)
![3条额外的壁](../images/support_wall_count_3.png)

额外的墙壁增加了支撑的强度，减少了它们倒塌的机会。它还允许支撑更好地支撑悬垂区域的边缘。对于具有尖角的模型，这些边往往会出现问题，因为直线在此处的半空中结束。此设置可以使它们在支撑线上结束。

然而，额外的墙壁也需要更多的时间来打印，使用更多的材料，之后也让支撑更难去除。当使用可溶性支撑材料时，额外的壁导致支撑需要更长的时间来溶解，因为溶剂不能再从侧面进入支撑结构。
