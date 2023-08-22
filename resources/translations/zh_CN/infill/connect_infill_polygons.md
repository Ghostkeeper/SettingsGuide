连接填充多边形
====
当填充由封闭环路组成时，这些环路可以融合在一起以形成一个单一的环路。启用此选项将在多边形相邻的位置进行小幅连接。

此设置仅在连接相邻的封闭回路填充物时才有效。这意味着：
* [填充图案](infill_pattern.md)设置为交叉或交叉3D。
* 填充线[乘以](infill_multiplier.md) 一个偶数。
* 至少有2条[额外壁](infill_wall_line_count.md)环绕在填充周围。

<!--screenshot {
"image_path": "connect_infill_polygons_disabled.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "triangles",
"infill_multiplier": 2,
"zig_zaggify_infill": true,
"connect_infill_polygons": false
},
"colours": 32
}-->
<!--screenshot {
"image_path": "connect_infill_polygons_enabled.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "triangles",
"infill_multiplier": 2,
"zig_zaggify_infill": true,
"connect_infill_polygons": true
},
"colours": 32
}-->
![使用多重线条填充时，填充图案中存在大量的循环。](../images/connect_infill_polygons_disabled.png)
![开启此设置会将各循环“焊接”到一起](../images/connect_infill_polygons_enabled.png)

此功能是为了避免额外的空驶。最后的线条将组成一个连接所有填充部分的单一循环，因此不会有任何空驶。该设置更适用于柔性线材，因为这种材料较难回抽，且它们在持续通过喷嘴的情况下才表现的最好。

这些回路在内部彼此相连也可以增强填充的强度。然而，当多边形被连接时，喷头不得不经常在接头之前进行180度调转。这些转弯有时会妨碍接头的充分连接。在某些情况下，这也会使填充强度变弱。这完全取决于回路根据模型的形状进行网格化的方式。
