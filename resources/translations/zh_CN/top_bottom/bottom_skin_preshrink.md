底部皮肤移除宽度
====
删除完全填充的底层的较薄部分，改为使用内嵌打印它们。这样可以节省打印时间和材料。

在陡峭的表面上，底层通常会变得非常薄。它们不是必需的，因为如果表面几乎完全垂直，墙壁的水平强度就足够了。

<!--screenshot {
"image_path": "skin_preshrink_original.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"bottom_skin_preshrink": 0,
"top_skin_preshrink": 0,
"max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_preshrink_shrunk.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"bottom_skin_preshrink": 1,
"top_skin_preshrink": 1,
"max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
![移除前](../images/skin_preshrink_original.png)
![移除后](../images/skin_preshrink_shrunk.png)

如果模型底部的斜率非常陡峭，皮肤就会变得非常薄。在这一点上，水平[壁厚](../shell/wall_thickness.md)是外壳强度的最大贡献者。由于壁厚应该已经设置好以使强度足够，因此在那里添加更多材料是不值得的。去掉这种皮肤材料可以节省大量的打印时间。

过度增加此设置可能会导致小碎片的底部被打开，因为里面装满的是填充物而不是皮肤。
