水平扩展
====
该设置引起整个模型的轻微扩大或收缩，是对打印中尺寸误差的补偿措施。

<!--screenshot {
"image_path": "xy_offset_neutral.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": 0},
"colours": 32
}-->
<!--screenshot {
"image_path": "xy_offset_wider.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": 1},
"colours": 32
}-->
<!--screenshot {
"image_path": "xy_offset_slimmer.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": -1},
"colours": 32
}-->
![原始模型](../images/xy_offset_neutral.png)
![水平扩展后，螺孔变小了](../images/xy_offset_wider.png)
![负值收缩模型，导致螺孔变宽了](../images/xy_offset_slimmer.png)

正值会使打印件更胖，相应减小了内部空腔。负值会使打印件更瘦，

 内部空腔更大。如果非常看重打印的公差，则这个设置相当好用。由于塑料的轻微变形，实际打印出的尺寸可能与设计尺寸不完全一致。构造板上模型的缩放误差可简单利用缩放工具进行调整，但由于打印方法造成的偏移误差则可以通过此设置补偿。

如果您很清楚打印机存在因挤出过度或不精准而会打印过宽的问题。该设置也可以对其进行补偿。
