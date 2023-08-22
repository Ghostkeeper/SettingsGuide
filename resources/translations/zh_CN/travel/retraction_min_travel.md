回抽最小空驶
====
此设置可防止材料在极短的空驶中回抽。在这些空驶中，无论如何，材料从喷嘴中渗出的时间很少，因此回抽将弊大于利。

<!--screenshot {
"image_path": "retraction_min_travel.png",
"models": [{"script": "spike_curve.scad"}],
"camera_position": [0, -31, 79],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_min_travel": 12},
"minimum_layer": 303,
"layer": 550,
"line": 334,
"colours": 64
}-->
![中间的最短空驶未回抽](../images/retraction_min_travel.png)

回抽材料是为了防止拉丝。非常短的行程移动不会产生拉丝，因为材料尚未来得及流出喷嘴。一个走线宽度左右的极短行程甚至会完全重叠线，因此没有任何拉丝的空间。另一方面，当材料在移动时，回抽会使喷嘴静止一小段时间。这允许一些材料流动并在那里产生一个斑点。由于这些原因，在短距离移动时，最好不要回抽，即使这些轨迹位于模型的可见部分。

将此设置增加过多将导致模型的细节部分或部分靠近的地方出现拉丝。
