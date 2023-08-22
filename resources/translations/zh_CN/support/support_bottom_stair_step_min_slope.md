支撑阶梯最小坡度角
====
使用此设定，您可以停用支撑最底部的楼梯步阶，直到模型的斜度具有特定角度为止。

<!--screenshot {
"image_path": "support_bottom_stair_step_min_slope_10.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 82, 10],
"camera_lookat": [0, 0, 10],
"settings": {
"support_enable": true,
"support_bottom_stair_step_height": 1,
"support_bottom_stair_step_min_slope": 10
},
"layer": 250,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_bottom_stair_step_min_slope_30.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 82, 10],
"camera_lookat": [0, 0, 10],
"settings": {
"support_enable": true,
"support_bottom_stair_step_height": 1,
"support_bottom_stair_step_min_slope": 30
},
"layer": 250,
"colours": 64
}-->
![在坡度达到10°之前，楼梯步阶处于禁用状态](../images/support_bottom_stair_step_min_slope_10.png)
![在坡度达到30°之前，楼梯步阶处于禁用状态](../images/support_bottom_stair_step_min_slope_30.png)

在浅坡度处，底部的楼梯台阶可能非常宽。它们的宽度永远不能超过[最大宽度](support_bottom_stair_step_width.md)指示的宽度，但是由于从所有边都保持该距离，因此楼梯步阶可能会变得很宽，以至于支撑需要跨越相当大的距离。如果支撑位于一个小山谷内，它甚至可以导致整个底部的边被跳过，使整个支撑只停留在楼梯步阶的角落。

在这些情况下，您可以将楼梯步阶限制为仅出现在较陡的坡度上。此设置决定了什么是陡坡。

增加此设置将阻止Cura在浅表面上生成楼梯步阶。这将使支撑更坚固，但更难拆卸。支撑会在表面上留下更多的伤痕。减少它将使支撑更容易删除，并在支撑所在处留下一个更好的表面。但在某些情况下，它可能会导致支撑不得不跨越很长的距离，甚至似乎完全挂在半空中。

为了获得一个漂亮的表面，最好将此设置保持在一个保守的低角度，5°或10°左右。如果支撑点位于较浅但不完全平坦的表面上，请检查层视图，如果发现支撑点看起来非常不稳定，请增加角度。
