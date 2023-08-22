支撑底板走线宽度
====
该设置单独定义支撑底板的线宽。

<!--screenshot {
"image_path": "support_bottom_line_width.png",
"models": [
{
"script": "gutter_lift.scad",
"transformation": ["mirrorZ", "scale(0.5)"]
}
],
"camera_position": [-45, 0, 104],
"camera_lookat": [0, 0, 3],
"settings": {
"support_enable": true,
"support_bottom_enable": true,
"support_bottom_line_width": 0.8
},
"layer": 65,
"colours": 64
}-->
![支撑底板（深蓝色）打印的比其他支撑宽](../images/support_bottom_line_width.png)

打印较细的线条虽然会降低支撑在模型上的附着力。然而他可以使粘合稳定可靠的多。一般来说，支撑更容易被移除，模型上留下的伤痕更少。代价是打印需要更多的时间。
