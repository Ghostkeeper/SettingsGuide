壁走线次数
====
该设置确定壁轮廓在每层打印多少次

<!--screenshot {
"image_path": "wall_thickness_0.8.png",
"models": [
{
"script": "rotary_tumbler_lid.scad",
"transformation": ["scale(0.4)"]
}
],
"camera_position": [50, 50, 124],
"settings": {
"skin_outline_count": 0,
"wall_line_count": 2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "wall_thickness_1.6.png",
"models": [
{
"script": "rotary_tumbler_lid.scad",
"transformation": ["scale(0.4)"]
}
],
"camera_position": [50, 50, 124],
"settings": {
"skin_outline_count": 0,
"wall_line_count": 4
},
"colours": 32
}-->
![打印两次壁线](../images/wall_thickness_0.8.png)
![打印四次壁线](../images/wall_thickness_1.6.png)

只有一个壁依照外壁的设置打印。其余壁将使用内壁设置进行打印。

壁的数量是决定打印强度的一个主要因素。各壁紧邻、彼此加固，整体更强。打印大尺寸零件时，与根据形状调整填充相比，可能获得更坚固的结果。

增加壁走线次数将会:
* 大幅提高打印强度。
* 减少内部填充图案的穿透到外部的效果。
* 改善悬垂，这是由于壁线往往有向最近静止点靠近的倾向。
* 模型更容易防水。
* 大幅增加打印时间和材料消耗。
