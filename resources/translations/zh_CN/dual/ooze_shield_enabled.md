启用渗出罩
====
使用多个挤出机打印时，非运转中的挤出机中有时仍有一些材料。如果喷嘴仍然是热的，这种材料往往会渗出。这就是渗出罩要防止的问题。渗出防护罩是物体周围的边框，可挡住喷嘴下方的任何渗出液。

<!--screenshot {
"image_path": "ooze_shield.png",
"models": [
{
"script": "rocket_dual.scad",
"scad_params": ["extruder=0"],
"object_settings": {
"extruder_nr": 0
},
"transformation": ["scale(0.5)"]
},
{
"script": "rocket_dual.scad",
"scad_params": ["extruder=1"],
"object_settings": {
"extruder_nr": 1
},
"transformation": ["scale(0.5)"]
}
],
"camera_position": [-62, 102, 87],
"settings": {
"ooze_shield_enabled": true,
"layer_height": 0.2,
"line_width": 0.6
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![渗出罩由层中的第一个挤出机打印,如果用两个挤出机打印，会造成图案交替](../images/ooze_shield.png)
![一些参数可以对渗出罩进行调整](../images/ooze_shield.svg)

渗出罩将打印到最高挤出机开关的高度。在该高度以上，处于待机模式后，没有喷嘴会移动到打印机中，因此无需打印渗出罩。在一层上开始的挤出机将打印出渗出罩。该挤出机将在每一层交替，对于使用两种粘贴不良的材料来说是危险的。然而，打印它以后，当另一个挤出机激活时，很大程度上破坏了渗出罩的效果。

渗出罩足够薄，很容易折断或切割，并与您的模型保持一定距离，以便可以在不对表面造成疤痕的情况下将其移除。
