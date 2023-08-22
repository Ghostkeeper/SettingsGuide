连接填充走线
====
此设置使用一条沿填充区域边缘的线连接填充图案的端点（填充与内壁或皮肤相交的位置）。

<!--screenshot {
"image_path": "infill_pattern_grid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "grid"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "zig_zaggify_infill_enabled.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "grid",
"zig_zaggify_infill": true
},
"colours": 64
}-->
![没有连接的填充线](../images/infill_pattern_grid.png)
![连接的填充线](../images/zig_zaggify_infill_enabled.png)

这会将整个填充图案转换为一条线或很少几条线。将其转换为单行并不总是可行的。这条线的起点是任意的，因此它可能对每个层都不相同，特别是如果包含填充的形状在层与层之间不同。

连接填充有几个好处，但也有一些缺点：
* 最终部件会更结实，因为实际上有一半的额外轮廓。
* 由于表面积增加，填充物将更好地粘附到墙壁上，这也使零件更坚固。
* 流速将保持更恒定，允许您以更快的速度打印填充，而不会出现流动问题。这对于难以正确挤出的材料尤其重要。
* 在填充的打印过程中显著减少回抽，这防止了材料的磨损。
* [填充重叠](infill_overlap.md)设置的效果被放大，因为填充线的大部分将与壁重叠。
* 这将需要更多的材料来打印填充。
* 通常，打印填充需要更多的时间，因为空驶行程通常比打印填充线快。
* 填充物通常将更多地穿过壁，因为它被推进壁中的比例更大。
