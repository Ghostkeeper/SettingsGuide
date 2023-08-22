第一层支撑挤出机
====
如果您的打印机有多个挤出机，则可以使用与支撑的其余部分不同的挤出机来打印位于构造板上的支撑。此设置允许您选择用于首层支撑的挤出机。

<!--screenshot {
"image_path": "support_extruder_nr_layer_0.png",
"models": [
{
"script": "question_stick_clip.scad",
"transformation": ["rotateY(90)"],
"object_settings": {"extruder_nr": 1}
}
],
"camera_position": [134, 134, 113],
"settings": {
"support_enable": true,
"support_interface_enable": true,
"support_use_towers": false,
"support_extruder_nr": 3,
"support_extruder_nr_layer_0": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![第一层支撑使用红色打印，其余为白色](../images/support_extruder_nr_layer_0.png)

某些材料比其他材料更适合用作打印支撑。这些通常是惰性材料，不能很好地粘附在其他材料上，因此可以更容易地去除。然而，这种特性不适合粘在构造板上。对构造板（玻璃或铝）有更好粘附性的材料可以用于第一层，在这里普通材料粘性略差，更适合打印其他层。
