添加中线阈值
====
打印薄件时，Cura会调整壁线的宽度，以符合模型的精确宽度。Cura也可以决定使用更少的壁线。此设置是Cura将在中心添加一条线的阈值。它可以与[合并中心线阈值](wall_split_middle_threshold.md)分开调整。

此设置与[最小奇数壁走线宽度](min_odd_wall_line_width.md)相同, 但使用不同的单位。此设置的单位是线宽的分数，零件的宽度需要增加以添加新的中间线。

<!--screenshot {
"image_path": "min_wall_line_width_0_34.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
<!--screenshot {
"image_path": "min_wall_line_width_odd_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_odd_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![当中心线过小时，它周围的两条线会变宽](../images/min_wall_line_width_0_34.png)
![减小此设置，中心线的起点和终点会更小](../images/min_wall_line_width_odd_0_1.png)

线条的奇偶
----
此设置允许调整添加行数的阈值，特别是当行数变为奇数时。这是当中心有一条线而不是两条线时。它确定何时在两条中心线之间添加新线。

添加中心线的阈值可能与将中间线一分为二的阈值不同，这是因为它们的过渡方式不同。当添加奇数行时，只有当周围的两行为它让路时，它才开始。在过渡过程中，周围的线条还没有留出足够的空间，这会有一点空隙。这与墙的数目为偶数时的情况不同：减小"添加中间行阈值"会减小从偶数行到奇数行的过渡处的间隙大小。减小"分割中线阈值"可减少从奇数线到偶数线过渡处的过度挤出。

在最终结果中，奇数行开始时留下的间隙比关节处的一点过度挤出更明显，因此将"添加中线阈值"设定为略低于"分割中线阈值"可能会有所帮助。

减小此设置将导致：
* 中心线结束时的间隙较小。
* 减少了一对偶数中心线的最大宽度。
* 较细的缐条，可能无法很好地挤出。
* 线数越多，打印时间越长。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
