支撑顶板挤出机
====
如果您的打印机有多个挤出机，则支撑顶面（模型在支撑上）可以使用不同于支撑底面（支撑在模型上）的挤出机来打印。此设置允许您选择用于支撑顶板的挤出机。

<!--screenshot {
"image_path": "support_roof_extruder_nr.png",
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
"support_roof_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![支撑顶板以红色打印，而支撑底板以白色打印](../images/support_roof_extruder_nr.png)

当用于支撑时，一些材料提供比其它材料更好的悬垂特性。例如，因为它们不与表面化学键合，或者可溶于水。所以也许它们能够打印的更接近表面。然而，这样的材料通常是昂贵的并且需要更长的时间来印刷。此设置允许您使用与支撑底板不同的挤出机打印支撑顶板。这样，虽然节省了昂贵或缓慢材料的使用，但仍能有效地建立良好的悬垂。

对于悬垂的质量，支撑顶板比支撑底板更重要，因此，如果要节约昂贵的材料，至少在支撑顶板上使用它。
