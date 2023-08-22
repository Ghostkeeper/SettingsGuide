最小壁走线宽度
====
打印薄件时，Cura会调整壁线的宽度，以符合模型的精确宽度。Cura也可以决定使用更少的壁线。Cura据此阈值判断是移除壁线，还是缩小原有壁线的宽度。

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
"image_path": "min_wall_line_width_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_wall_line_width": 0.1,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![通常线条会变宽来匹配](../images/min_wall_line_width_0_34.png)
![减小该设置，Cura选择使用更多线条](../images/min_wall_line_width_0_1.png)

不同数量的壁
----
如果有一条单一中心线并且 [壁分派次数](wall_distribution_count.md) 设为 1, 该设置的功能即入以上所述。如果位于中间的线薄于一个确定的宽度，则偏向于去除这条线，加宽其他线条。其他情况下有着更为复杂的计算。

虽然精确的计算很复杂，但实际上可以更直观的理解下：你可以将模型的总宽度除以 [走线宽度（壁）](../resolution/wall_line_width.md) 的值来获得壁的一个确定数量。不过可能是一个分数 (比如走线宽度为5.3)。“最小壁走线宽度”使用小数部分 (0.3线宽)，并在超过它的时候添加额外壁。在已知壁数量的条件下，将根据“壁分派次数”决定每条线的宽度。

![“最小壁走线宽度”向左或向右调整添加新线的阈值](../images/min_wall_line_width.svg)

这意味着，如果更多的线被调整了宽度，那么走线宽度永远不会像“最小壁走线宽度”所允许的那样极端。比如，中间两条线调整了线宽，线宽不会低于普通走线宽度和最小壁走线宽度的平均值。

设置可以分别对[最小偶数壁走线宽度](min_even_wall_line_width.md) 和[最小奇数壁走线宽度](min_odd_wall_line_width.md) 进行调整。壁为0个这种单独的情况可以使用[最小特征尺寸](min_feature_size.md) 调节。

调节
----
理论上，将其设置为走线宽度的50%可以确保与普通走线宽度接近。然而实际上高一点儿比较好。打印略宽于喷嘴的线条比打印小于喷嘴的线条容易，而且更少的线条意味着更快的打印速度。

打印粘稠的材料或高速打印时，需要降低“最小壁走线宽度”以免把线打印的太宽。 如果材料没有足够的时间向侧面流动就会非常难打印；如果“最小壁走线宽度”设置的太高，壁之间就不能很好地粘附，最终导致成品脆弱。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
