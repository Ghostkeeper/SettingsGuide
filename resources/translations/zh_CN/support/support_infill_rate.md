支撑密度
====
此设置定义了材料填充支撑结构的速率。在较大的填充率下，支撑线将非常靠近。在较低的填充率下，支撑线之间的距离将更远。

<!--screenshot {
"image_path": "support_infill_rate_low.png",
"models": [{"script": "spiral_stair.scad"}],
"camera_position": [-95, 18, 116],
"settings": {
"support_enable": true,
"support_infill_rate": 10
},
"layer": 256,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_rate_high.png",
"models": [{"script": "spiral_stair.scad"}],
"camera_position": [-95, 18, 116],
"settings": {
"support_enable": true,
"support_infill_rate": 20
},
"layer": 256,
"colours": 64
}-->
![低支撑密度](../images/support_infill_rate_low.png)
![高支撑密度](../images/support_infill_rate_high.png)

增加支撑的密度有一些积极和消极的影响。以下是一些需要权衡的影响：
* 由于支撑线之间的距离较小，因此放置在此支撑顶部的表面将不会下垂。
* 支撑力会更强，提高打印的可靠性。
* 由于粘附表面增加，因此更难移除支撑。
* 打印支持将需要更多的材料。
* 打印将需要较长时间才能完成。
