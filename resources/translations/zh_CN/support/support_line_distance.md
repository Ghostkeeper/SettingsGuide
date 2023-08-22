支撑走线距离
====
此设置定义支撑图案中两条相邻线之间的距离。这种调整支撑密度的方式可能比调整支撑密度更直观，因为它直接调整了支撑线必须跨越的距离。

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
![线条间距大](../images/support_infill_rate_low.png)
![线条间距小](../images/support_infill_rate_high.png)

减小支撑线之间的距离有一些积极和消极的影响。以下是一些需要权衡的影响：
* 放置在此支撑顶部的表面将更少下垂，因为它必须在两条支撑线之间桥接更小的距离。
* 支撑力会更强，提高打印的可靠性。
* 由于粘附表面增加，因此更难移除支撑。
* 打印支持将需要更多的材料。
* 打印将需要较长时间才能完成。
