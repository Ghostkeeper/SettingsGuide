走线宽度（支撑接触面）
====
该设置定义支撑接触面的线宽，可与支撑的其他部分的线宽不同。（

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
![支撑接触面的线宽比其他支撑更宽](../images/support_roof_line_width.png)

仅通过稍细的线宽打印支撑接触面，使其具有平滑的顶面，对提高被支撑的悬垂表面质量常常是有利的。且支撑和模型的粘附力不是必然增大的，所以支撑不一定难拆。

同理，支撑的底层接触面将更均匀地粘附，保持强度的同时减少留在模型上的痕迹。

然而，过细的线条会导致挤出不均匀，降低支撑效果和稳定性，以及悬垂部分的质量。还可能导致喷嘴处的流量速率变化巨大，支撑开始打印时出现挤出过度，支撑过后的部分挤出不足。
