支撑底板挤出机
====
如果您的打印机有多个挤出机，则可以使用不同的挤出机来打印支撑底面（支撑位于模型上）和支撑的顶面（模型位于支撑上）。此设置允许您选择用于支撑底板的挤出机。

<!--screenshot {
"image_path": "support_bottom_extruder_nr.png",
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
"support_bottom_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![支撑底板以红色打印，而支撑顶板以白色打印](../images/support_bottom_extruder_nr.png)

当用于支撑时，一些材料提供比其它材料更好的悬垂特性。例如，因为它们不与表面化学键合，或者可溶于水。所以也许它们能够打印的更接近表面。然而，这样的材料通常是昂贵的并且需要更长的时间来印刷。此设置允许您使用不同的挤出机打印支撑底部。这样可以节省一些昂贵或印刷速度慢的材料。

对于悬垂的质量，支撑底板的重要性低于支撑顶板。如果要节约使用昂贵的材料，则用较便宜的材料打印支撑底板是一个良好的候选。
