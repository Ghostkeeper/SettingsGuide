支撑顶部距离
====
此设定规划支撑顶部与模型的悬垂曲面之间保持的距离。

<!--screenshot {
"image_path": "support_z_distance.png",
"models": [{"script": "rack.scad"}],
"camera_position": [0, 129, 11],
"settings": {
"support_enable": true,
"support_z_distance": 1
},
"colours": 32
}-->
![深蓝色模型与浅蓝色支撑之间的顶部距离](../images/support_top_bottom_distance.svg)
![模型与支撑面之间保持垂直距离](../images/support_z_distance.png)

支撑顶部距离是影响支撑附着到模型（模型位于支撑上）的程度的最大因素。增加距离可使支撑物在打印后更容易被取下，因为它不能很好地附着在打印件上。然而，它也会使悬垂看起来更糟，因为它被允许在支撑之前再下垂几层。
