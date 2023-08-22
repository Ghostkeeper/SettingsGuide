闪电填充修剪角
====
闪电状填充图案在打印内部产生一个树状结构，开始很小，但分支延伸到需要从内部支撑的打印顶部的所有部分。此设置指示树的分支在端点处可以悬垂的距离。

<!--screenshot {
"image_path": "lightning_infill_prune_angle_40.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [112, 15, 9],
"settings": {
"infill_pattern": "lightning",
"wall_line_count": 0,
"top_layers": 0,
"lightning_infill_support_angle": 40,
"lightning_infill_prune_angle": 40
},
"colours": 32
}-->
<!--screenshot {
"image_path": "lightning_infill_prune_angle_70.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [112, 15, 9],
"settings": {
"infill_pattern": "lightning",
"wall_line_count": 0,
"top_layers": 0,
"lightning_infill_support_angle": 40,
"lightning_infill_prune_angle": 70
},
"colours": 32
}-->
![在40°时，闪电填充非常稳定](../images/lightning_infill_prune_angle_40.png)
![在70°时，树状悬垂相当陡峭](../images/lightning_infill_prune_angle_70.png)

增加修剪角度意味着填充将能够在底部开始较小，同时仍然到达所有顶部曲面。在许多情况下，它甚至不需要从底部开始，而是可以简单地挂在两侧。增加该角度的显著效果是：

* 减少打印时间和材料使用。
* 更平滑的墙壁，因为不会有太多的填充物从内部接触墙壁。
* 强度略有下降。
* 打印失败的可能性更大。如果悬垂太陡，则每条线的末端将有明显的悬垂，它们将下垂并可能松动。

实际上，修剪角度可以高于正常悬垂角度或其他闪电形填充悬挑角。由于线条在下面的层上得到了很好的支持，所以有更多的悬垂并不是一个真正的问题。
