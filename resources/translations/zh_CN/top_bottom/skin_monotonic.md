单调顶部/底部顺序
====
通常，Cura会对顶部/底部线条进行排序，使它们之间的移动距离变小。如果开启本设置，则会对顶部/底部线条进行排序，使相邻的线条总是在同一方向上重叠打印。

由于线条的形状不是完美的矩形，所以在打印顶部/底部表面时，它与旁边的线通常会有一点重叠。这种重叠赋予了线条微小的坡度，造成它们在不同方向上的光线反射不一致。如果相邻的线条重叠方式不同，反射就会发生改变。可以在成品上看到这一点。它赋予表面不同区域以不同的光泽。按照单调顺序进行打印可以确保整个表面的重叠相同，使表面对光线的反射一致。这使得表面看起来更加平滑和一致。

<!--screenshot {
"image_path": "skin_monotonic_disabled.gif",
"models": [
{
"script": "yen.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 0, 130],
"settings": {
"wall_line_count": 1,
"skin_outline_count": 0,
"travel_compensate_overlapping_walls_enabled": false,
"skin_monotonic": false
},
"layer": 1,
"line": [48, 68, 88, 108, 128, 148, 168, 180, 200, 220, 232, 276, 302, 334, 354, 374, 394, 422, 442, 472, 492, 521, 541, 556],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_monotonic_enabled.gif",
"models": [
{
"script": "yen.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 0, 130],
"settings": {
"wall_line_count": 1,
"skin_outline_count": 0,
"travel_compensate_overlapping_walls_enabled": false,
"skin_monotonic": true
},
"layer": 1,
"line": [51, 71, 100, 120, 141, 161, 192, 212, 233, 253, 281, 309, 339, 367, 386, 406, 426, 446, 466, 486, 506, 526, 546, 557],
"delay": 125,
"colours": 32
}-->
![非单调顺序](../images/skin_monotonic_disabled.gif)
![单调顺序，总是从右下角开始](../images/skin_monotonic_enabled.gif)

单调顺序会略微增加移动的距离，但影响非常小。仅对成品的观感产生影响。单调顺序没有力学上的优势。

将[梳理模式](../travel/retraction_combing.md) 设置为“除了皮肤”，同时开启[Z抬升](../travel/retraction_hop.md)，可配合本设置实现光滑的表面。也许还可以启用 [熨平](ironing_enabled.md), 但它会完全覆盖本设置的实用性。熨平有着自己独立的[单调选项](ironing_monotonic.md)。

![线条打印顺序不一致时反光有差别](../images/skin_monotonic_disabled.jpg)
![按照单调顺序打印后，反光整体一致](../images/skin_monotonic_enabled.jpg)
