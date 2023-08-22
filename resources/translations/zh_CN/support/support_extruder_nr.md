支撑用挤出机
====
如果打印机具有多个挤出机，则此设定可让您选择哪一个挤出机来打印支撑结构。

<!--screenshot {
"image_path": "support_extruder_nr.png",
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
"support_extruder_nr": 3
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![支撑采用白色材料打印，而模型采用蓝色材料](../images/support_extruder_nr.png)

使用不同类型的材料倾向于使支撑件更容易移除而不损害支撑件的强度。不同的材料类型不会很好地相互粘附，尤其是在它们具有不同的收缩率时。

此外，某些材料还被设计成适于打印支撑。例如，它们可以故意做得极脆，这样它们就更容易折断。有些材料会溶于水或乙醇，因此，即使印刷在离模型很近的地方，您也可以移除支撑。

使用不同挤出机打印支撑需要打印机在每一层都切换材料，这可能增加打印时间。如果支撑材料的颜色与构建材料不同，则打印件上的支撑残留物可能非常明显。
