锥形支撑最小宽度
====
如果启用了锥形支撑并将其设置为收缩支撑结构，则此设置将确定锥形支撑将收缩到的最小宽度。除非需要支撑的悬垂区域已经变薄，否则支撑不会变薄。

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
{
"script": "wide_overhang.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [91, -95, 19],
"settings": {
"support_enable": true,
"support_conical_enabled": true,
"support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_min_width_20.png",
"models": [
{
"script": "wide_overhang.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [91, -95, 19],
"settings": {
"support_enable": true,
"support_conical_enabled": true,
"support_conical_angle": 30,
"support_conical_min_width": 15
},
"colours": 64
}-->
![最小宽度5mm](../images/support_conical_enabled.png)
![最小宽度15mm](../images/support_conical_min_width_20.png)

如果一个很大体积的支撑物被搁置在一个很小的支撑柱上，这个支撑物将非常容易翻倒。增加最小宽度会增加圆锥体将被吸引到的支撑基柱的宽度。这增加了打印的可靠性，但将花费额外的材料。总而言之，锥形支撑件在减少打印时间方面的效果较差。
