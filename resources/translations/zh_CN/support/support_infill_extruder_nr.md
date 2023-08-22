支撑填充挤出机
====
如果您的打印机有多个挤出机，则可以使用与支撑接触面不同的挤出机打印支持的主体。此设置允许您选择用于支撑主体的挤出机。

<!--screenshot {
"image_path": "support_infill_extruder_nr.png",
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
"support_infill_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![支撑主体以红色打印，但接触面以白色打印](../images/support_infill_extruder_nr.png)

某些材料比其他材料更适合打印支撑，但这些材料可能更贵或打印速度也更慢。只在接触面使用昂贵材料，大多数支撑主体则使用较便宜的材料，可以节省大量的时间和金钱。这样打印接触面，可以让它的观感更好或更容易拆除，其余大部分的支撑仍会使用更便宜的材料打印。

如果您使用可溶性材料来打印支撑接触面，但使用不可溶性材料来打印支撑主体，请记住，如果无法将支撑主体从小孔中移出，则支撑主体可能无法取出。通常情况下，可溶性物质可以通过溶液中的空腔流出，而不溶性物质可能无法通过。
