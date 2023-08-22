壁过渡筛选距离
====
有些模型薄壁的尺寸会在线宽调整阈值附近徘徊。虽然壁的实际宽度变化并不大，但反复出现的壁调整会造成壁数量前后交替。这破坏打印质量，允许更多的流量变化，同时也造成较多的空驶。通过该设置，可以在一定距离内移除这些调整。

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
![不设置筛选时，圆环部分在2个壁和3个壁间反复](../images/wall_transition_filter_off.png)
![设置了筛选后，壁数量不再反复](../images/wall_transition_filter_on.png)

当一个过渡被移除时，一些线条会暂时变得过宽或过窄，超过[最小壁走线宽度](min_wall_line_width.md)。毕竟，过渡的存在可以更好的适应零件的宽度，如果没有这些过渡，将使用比理想数量更少或更多的壁，并相应调整其宽度，调整范围在[壁过渡筛选边距](wall_transition_filter_deviation.md)内都是允许的。如果壁宽度变化太大，那么将不会移除过渡。

该筛选器旨在解决低分辨率三维网格下薄零件的常见问题。平面三角形组成的三维模型不能精确的表示曲线，只能近似。曲线会有边，它们之间存在面。当对具有恒定宽度的弯曲零件建模时，内外两条边的对齐很重要。如果不对齐，环的宽度会略有变化，导致上面提到的效果。所以，过渡筛选器应该防止产生太大的影响。

在某些情况下，增加距离会避免创建小线段。这样打印速度更快，可以使表面看起来更光滑。然而，也会导致打印中存在可能出现挤出不良的极端走线宽度。当用薄层打印低分辨率模型时，增加距离可能有助于提高质量。对于难以打印的材料，还是保守一些好。

**该设置当前对用户不可见。只能通过[壁过渡筛选边距](wall_transition_filter_deviation.md)调整。该设置不仅仅适用于普通壁，还适用于额外皮肤壁、支撑壁、填充壁和同心图案。**
