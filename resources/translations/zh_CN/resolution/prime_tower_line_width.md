装填塔走线宽度
====
该设置定义已打印的装填塔的线宽。

<!--screenshot {
"image_path": "prime_tower_line_width.png",
"models": [
{"script": "cube.scad"},
{
"script": "cube.scad",
"object_settings": {"extruder_nr": 1},
"transformation": ["translateX(40)"]
}
],
"camera_position": [475, -419, 131],
"camera_lookat": [475, -465, 20],
"settings": {
"prime_tower_enable": true,
"[1]prime_tower_line_width": 0.8
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![蓝色材料的线宽比黄色材料的大](../images/prime_tower_line_width.png)

较宽的走线有时会加快装填塔的打印速度。如果挤出的轮廓足够大，增加线宽会使另一次走线不再必要。但是，过大的线宽会导致挤出不足，使装填塔变弱。
