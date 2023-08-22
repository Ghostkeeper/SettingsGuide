分割中线阈值
====
打印薄件时，Cura会调整壁线的宽度，以符合模型的精确宽度。Cura也可以决定使用更少的壁线。此设置是Cura在部件宽度增加时将中心的一条线拆分为两条线的阈值。它可以与[添加中线阈值](wall_add_middle_threshold.md)分开调整。

此设置与[最小偶数壁线宽度](min_even_wall_line_width.md)相同，但使用不同的单位。此设置的单位是线宽的分数，零件的宽度需要增加以将中心线一分为二。由于分割后宽度的差异会在中间的两条线上进行分割，因此较小的"最小偶数墙线宽"相当于比删除奇数墙时小得多的"分割中线阈值"。

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
"image_path": "min_wall_line_width_even_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_even_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![中心线加宽以适合](../images/min_wall_line_width_0_34.png)
![减少此设置，将使用两行](../images/min_wall_line_width_even_0_1.png)

线条的奇偶
----
此设置允许调整添加行数的阈值，特别是当行数变为偶数时。这是指在中心有两条线而不是一条线的情况。它决定了中心线何时拆分为两条线。

分割中线的阈值可能与添加中线的阈值不同，这是因为它们连接在一起的方式不同。偶数线通过使端点更靠近在一起而在其端点处连接。这些线在那里有一些重叠，导致挤出过度。这与壁的数目为奇数时的情况不同：减小"分割中线阈值"可减少从偶数线到奇数线过渡处的过度挤出。减小"添加中间行阈值"会减小从奇数行到偶数行的过渡处的间隙大小。

在最终结果中，添加中心线时留下的间隙比关节处的一点过度拉伸更明显，因此将"分割中线阈值"设定为稍高于"添加中线阈值"可能会有所帮助。

减小此设置将导致：
* 两条线连接在一起合并为一条线的重叠区域减少。
* 减少单中心线的最大宽度。
* 较细的缐条，可能无法很好地挤出。
* 行数越多，打印时间越长。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
