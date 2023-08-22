最小偶数壁走线宽度
====
当打印薄件时，Cura会调整线宽来准确适应模型的宽度。Cura也可以决定使用更少的壁线。该设置是Cura将中心两条线合并的阈值。可以通过[中心线移除阈值](min_odd_wall_line_width.md)分别调整。

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
该设置允许调整移除线条的阈值，尤其是存在偶数条线的情况。这是指在中心有两条线而不是一条线的情况。决定它们什么时候合二为一。

最小偶数壁走线宽度与最小奇数壁走线宽度可能不同，因为它们连接的方式不同。偶数线通过使端点更靠近在一起而在其端点处连接。这些线在那里有一些重叠，导致挤出过度。这与壁的数目为奇数时的情况不同：降低本设置会减小偶数线到奇数线过渡时的挤出过度。降低“最小奇数壁走线宽度”的设置会减小奇数线到偶数线过渡时的空隙。

奇数线结束时留下的间隙在最终结果中比连接处的挤出过度更明显，因此将“最小偶数壁走线宽度”设置为略高于“最小奇数壁走线宽度”可能会有所帮助。

减小此设置将导致：
* 两条线连接在一起合并为一条线的重叠区域减少。
* 减少单中心线的最大宽度。
* 较细的缐条，可能无法很好地挤出。
* 行数越多，打印时间越长。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
