交叉3D气槽大小
====
制作交叉3D[填充图案](../infill/infill_pattern.md)是为了打印方便灵活。该模式包含四路非常严格的交叉。此设定会使图案避免交叉，以避免在某些位置过于僵硬。它会使图案在交叉处留下一个气穴。此设置确定气穴的大小。

<!--screenshot {
"image_path": "infill_pattern_cross_3d.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "cross_3d",
"cross_infill_pocket_size": 2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "cross_infill_pocket_size_0_5.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "cross_3d",
"cross_infill_pocket_size": 0.5
},
"colours": 32
}-->
![默认气穴大小为2毫米](../images/infill_pattern_cross_3d.png)
![气穴大小为0.5毫米](../images/cross_infill_pocket_size_0_5.png)

该模式改变了四向交叉口周围的距离。此设置确定线条完全接触时图层中气穴的大小。气穴最大尺寸由填充密度确定。绘制的气穴大小不会大于填充走线距离的平方根的2倍。如果输入的值较大，则不会产生任何效果，但在使用[渐变填充](../infill/gradual_infill_steps.md)或者[可变填充密度](cross_infill_density_image.md)的情况下，仍可以输入较大的值，以便于使用较大的气穴尺寸。

增加此设定的值会使填充在垂直方向上较弱，并在强度在周围更好地展开，以建立更均匀的强度分布。
