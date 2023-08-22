壁分派次数
====
Cura可以调整线宽更好的适应打印的形状， 但不必对每个壁都做相同的调整。它倾向进一步朝模型内部改变线宽。该设置定义从内向外共有多少壁会根据可用空间进行调整。

<!--screenshot {
"image_path": "wall_distribution_count_1.png",
"models": [
	{
		"script": "misaligned_ring.scad",
		"transformation": ["scale(2)"]
	}
],
"camera_position": [-11, 0, 111],
"settings": {
	"wall_line_count": 5,
	"wall_distribution_count": 1
},
"colour_scheme": "line_width",
"colours": 128
}-->
<!--screenshot {
"image_path": "wall_distribution_count_5.png",
"models": [
	{
		"script": "misaligned_ring.scad",
		"transformation": ["scale(2)"]
	}
],
"camera_position": [-11, 0, 111],
"settings": {
	"wall_line_count": 5,
	"wall_distribution_count": 5
},
"colour_scheme": "line_width",
"colours": 128
}-->
![集中在中间，线宽变化很大](../images/wall_distribution_count_1.png)
![分布在许多壁上](../images/wall_distribution_count_5.png)

宽度不一的壁相比宽度统一的壁更难打印。调整喷嘴流速需要时间，过渡区也需要产生一些锐角，这会带来振纹。所以最好离外部越远越好，以免透过表面。Cura会专注于在最内侧的壁上调整线宽。

另一方面，集中变化也意味着中间的线具有广泛的发散宽度。扩展到更多线上意味着变化幅度可以更小，从而减少可变线宽的影响，而不是单纯隐藏它。

该设置从内部选择一定数量的壁进行调整，以便更好的填充空间。壁的计数是双向的，如果设置为2，那么最多可以在中心调整4个壁。调整亦不是均匀分布在每条壁上，中心的壁会调整的稍微多一些。

外壁会尽可能的保持标称线宽，这样才能确保表面足够光滑，提高质量。只有在极端情况下，零件薄的只有外壁组成时，这些壁才会被调整。

在实践中，将缺陷隐藏在中心比分散在多个壁上是更好的策略。因此，该设置应尽可能低。使用难以挤出的或者流量变化的材料（如柔性材料）时，增加此值有助于减少流量变化，但流量改变永远不能完全避免。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
