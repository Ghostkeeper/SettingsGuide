壁过渡筛选边距
====
有些模型薄壁的尺寸会在线宽调整阈值附近徘徊。虽然壁的实际宽度变化并不大，但反复出现的壁调整会造成壁数量前后交替。这破坏打印质量，允许更多的流量变化，同时也造成较多的空驶。使用该功能，可以移除这些反复的调整。

当一个过渡被移除时，一些线条可能会暂时变得太宽或太细。此设置通过限制线条的宽窄来控制哪些过渡被过滤。

<!--screenshot {
"image_path": "wall_transition_filter_off.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 0,
	"wall_transition_filter_margin": 0,
	"wall_line_count": 3
},
"colours": 64
}-->
<!--screenshot {
"image_path": "wall_transition_filter_on.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 100,
	"wall_transition_filter_margin": 0.2,
	"wall_line_count": 3
},
"colours": 64
}-->
![设置较小的边距时，圆环部分在2个壁和3个壁间反复](../images/wall_transition_filter_off.png)
![设置较大的边距时，壁数量不再反复](../images/wall_transition_filter_on.png)

确切的说，为了防止反复调整壁宽，线宽允许小于 [最小壁走线宽度](min_wall_line_width.md)的设置。同样，线也可以被设置的稍宽些，即使最小壁走线宽度的额外壁也可以匹配进去。

该筛选器旨在解决低分辨率三维网格下薄零件的常见问题。平面三角形组成的三维模型不能精确的表示曲线，只能近似。曲线会有边，它们之间存在面。当对具有恒定宽度的弯曲零件建模时，内外两条边的对齐很重要。如果不对齐，环的宽度会略有变化，导致上面提到的效果。所以，过渡筛选器应该防止产生太大的影响。

在某些情况下，增加边距会避免创建小线段。这样打印速度更快，可以使表面看起来更光滑。然而，也会导致打印中存在可能出现挤出不良的极端走线宽度。当用薄层打印低分辨率模型时，增加边距可能有助于提高质量。对于难以打印的材料，还是保守一些好。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
