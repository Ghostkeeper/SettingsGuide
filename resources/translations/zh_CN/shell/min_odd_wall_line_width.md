最小奇数壁走线宽度
====
打印薄件时，Cura会调整壁缐的长度，以符合模型的精确长度。Cura也可以决定使用更少的壁线。此设置是Cura将在中心添加一条线的阈值。它可以与[合并中心线阈值](min_even_wall_line_width.md)分开调整。

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
该设置允许调整移除线条的阈值，尤其是存在奇数条线的情。这是当中心有一条线而不是两条线时。决定何时移除中心线以便略微加宽它周围的线。

最小奇数壁走线宽度与最小偶数壁走线宽度可能不同，因为他们过渡的方式不同。移除奇数线后，它会在过渡之前停止，并让周围的墙闭合。过渡过程中由于两边的线还没有完全融合在一起，会有一点间隙。这与壁为偶数时不同： 中间的两条线缩在一起，略微重叠。降低“最小奇数壁走线宽度”的设置会减小奇数线到偶数线过渡时的空隙。降低本设置会减小偶数线到奇数线过渡时的挤出过度。

奇数线结束时留下的间隙在最终结果中比连接处的挤出过度更明显，因此将“最小奇数壁走线宽度”设置为略低于“最小偶数壁走线宽度”可能会有所帮助。

减小此设置将导致：
* 中心线结束时的间隙较小。
* 减少了一对偶数中心线的最大宽度。
* 较细的缐条，可能无法很好地挤出。
* 线数越多，打印时间越长。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
