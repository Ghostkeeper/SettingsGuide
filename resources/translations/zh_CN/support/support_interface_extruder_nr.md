支撑接触面挤出机
====
如果打印机有多个挤出机，则可以使用与支撑主体不同的挤出机打印支持面与模型的接触面。此设置允许您选择用于支撑接触面的挤出机。

<!--screenshot {
"image_path": "support_interface_extruder_nr.png",
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
"support_interface_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![支持接触面为红色，主体为白色](../images/support_interface_extruder_nr.png)

某些材料比其他材料更适合用作打印支撑。例如，它们可能不会化学附着在构建材料上，然后更容易脱落，或者它们可能会溶于水或酒精。然而，这样的材料通常是昂贵的并且需要更长的时间来印刷。此设置允许您使用与主体不同的挤出机打印支撑接触面，以便大多数支撑仍然可以快速打印和/或使用更便宜的材料打印，但仍保留了专业化支撑材料的优势。

如果您使用可溶性材料来打印支撑接触面，但使用不可溶性材料来打印支撑主体，请记住，如果无法将支撑主体从小孔中移出，则支撑主体可能无法取出。通常情况下，可溶性物质可以通过溶液中的空腔流出，而不溶性物质可能无法通过。
