支撑顶板走线宽度
====
该设置单独定义支撑顶板的线宽。

<!--screenshot {
"image_path": "support_roof_line_width.png",
"models": [
{
"script": "trash_bin_lid.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [-47, 79, 110],
"settings": {
"support_enable": true,
"support_roof_enable": true,
"support_roof_line_width": 0.8
},
"layer": 192,
"colours": 64
}-->
![支撑顶板走线宽度大于其他走线](../images/support_roof_line_width.png)

使用稍细的线宽打印支撑顶板，有利于被支撑部分形成光滑的表面。且支撑和模型的粘附力不是必然增大的，所以支撑不一定难拆。且支撑和模型的粘附力不是必然增大的，所以支撑不一定难拆。

然而，过细的线条会导致挤出不均匀，降低支撑效果和悬垂部分的质量。还可能导致喷嘴处的流量速率变化巨大，支撑顶板开始打印时出现挤出过度，而过后的部分挤出不足。
