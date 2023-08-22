壁厚
====
该设置定义壁的厚度。并随之调整内壁的数量。

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
![壁厚 0.8mm](../images/wall_thickness_0.8.png)
![壁厚 1.6mm](../images/wall_thickness_1.6.png)

壁厚必须是壁走线宽度的倍数。否则将四舍五入为精确倍数。请注意：壁由一条外壁和若干内壁组成，它们可以有不同的线宽。

壁厚是决定打印强度的一个主要因素。各壁紧邻、彼此加固，整体更强。打印大尺寸零件时，与根据形状调整填充相比，可能获得更坚固的结果。

增加壁厚会：
* 大幅提高打印强度。
* 减少内部填充图案的穿透到外部的效果。
* 改善悬垂，这是由于壁线往往有向最近静止点靠近的倾向。
* 模型更容易防水。
* 大幅增加打印时间和材料消耗。
