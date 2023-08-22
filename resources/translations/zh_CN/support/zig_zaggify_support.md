连接支撑线
====
对于某些支撑图案，当需要细条的支撑时，支撑可能变得非常不稳定。此设置将使支撑线的端点连接在一起。这使它们更加稳定。它还使打印支撑具有更连续的流量。所需的空驶将更少。

<!--screenshot {
"image_path": "zig_zaggify_support_disabled.png",
"models": [{"script": "plug.scad"}],
"camera_position": [71, 71, 147],
"settings": {
"support_enable": true,
"support_pattern": "triangles",
"support_wall_count": 0,
"support_offset": 0.2,
"zig_zaggify_support": false
},
"layer": 236,
"colours": 64
}-->
<!--screenshot {
"image_path": "zig_zaggify_support_enabled.png",
"models": [{"script": "plug.scad"}],
"camera_position": [71, 71, 147],
"settings": {
"support_enable": true,
"support_pattern": "triangles",
"support_wall_count": 0,
"support_offset": 0.2,
"zig_zaggify_support": true
},
"layer": 236,
"colours": 64
}-->
![支撑线已断开](../images/zig_zaggify_support_disabled.png)
![支撑线已连接](../images/zig_zaggify_support_enabled.png)

绘制支撑线时，不是空驶到下一条线，而是将沿支撑区域的边界绘制一条线连向下一条线，这会将整个支撑图案转换为一条线或很少的线。将其转换为单行并不总是可行的。这条线的起点是任意的，所以经常会有悬在半空中的线，因为在一层中，两条线可能在一个端点连接，而在下一层中，它们在另一端连接。这使得支撑稍微变弱，但仍然稳定，并且仍然防止流量中断。此设置的行为与[连接填充走线](../infill/zig_zaggify_infill.md)的行为相同。

连接支撑线有几个好处，但也有一些缺点：
* 支撑将更加稳定，在打印过程中不太可能翻倒。
* 流量将保持更恒定，使您能够以更快的速度打印支撑，而不会出现流量问题。这对于难以适当挤出的支撑材料尤其重要。
* 如果在支撑期间发生回抽，在打印支撑期间的回抽将显著减少，这防止了材料被磨损。
* 打印支撑需要更多的材料。
* 通常，打印支撑需要更多的时间，因为移动速度通常快于打印支撑线。

锯齿形支撑图案始终是连接的（使用的方法略有不同）。此设定不适用于锯齿形图案。
