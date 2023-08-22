移除Raft内侧角
====
启用此设置后，将完全移除Raft的所有内角，从而将Raft变为 [凸面形状](https://en.wikipedia.org/wiki/Convex_set)。Raft将只有外角。

<!--screenshot {
"image_path": "raft_remove_inside_corners.png",
"models": [{"script": "microwave_hook.scad"}],
"camera_position": [59, 59, 200],
"settings": {
	"adhesion_type": "raft",
	"raft_remove_inside_corners": true
},
"colours": 64
}-->
![raft不再遵循模型的形状](../images/raft_remove_inside_corners.png)

这实际上等同于具有非常高的[平滑度](../platform_adhesion/raft_smoothing.md)。从Raft中删除内角有许多影响：
* Raft的一小部分不再可能伸出Raft的其余部分很远。Raft的小部分更有可能从构造板上松动，尤其是使用高度翘曲的材料时。去除内角可减少这种影响，使打印更可靠。
* Raft更大，增加了对构造板的总附着力。
* Raft需要更长的时间来印刷，使用更多的材料。
