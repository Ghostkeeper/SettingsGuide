连接顶部/底部多边形
====
当使用同心图案（由闭合轮廓组成的图案，也称为多边形）打印顶部/底部走线图案时，将所有轮廓连在一起形成一条单一路径。

<!--screenshot {
"image_path": "connect_skin_polygons_original.png",
"models": [
{
"script": "web.scad",
"scad_params": ["stakes=1", "line_width=4"]
}
],
"camera_position": [10, 5, 111],
"settings": {
"top_bottom_pattern": "concentric",
"connect_skin_polygons": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "connect_skin_polygons_enabled.png",
"models": [
{
"script": "web.scad",
"scad_params": ["stakes=1", "line_width=4"]
}
],
"camera_position": [10, 5, 111],
"settings": {
"top_bottom_pattern": "concentric",
"connect_skin_polygons": true
},
"colours": 64
}-->
![同心图案生成彼此独立的轮廓](../images/connect_skin_polygons_original.png)
![所有轮廓连在一起成为一条曲线](../images/connect_skin_polygons_enabled.png)

这防止了大多数的空驶，但是也会在喷嘴大幅加速减速的地方形成锐角，这反而抵消了时间上的优势。在外面也可以看到弯弯曲曲的图案，这倒提供了有趣的表面效果。

由[额外皮肤壁计数](skin_outline_count.md) 生成的轮廓不会被连接。
