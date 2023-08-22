空驶时避开已打印部分
====
通过启用此设置，打印头在构造体积内移动时将尽量避免碰撞其他物体。它将采取一个小的弯路代替（原路径）。如果绕行不会碰撞任何其他对象，则不会触发任何回抽，除非路径的长度超过[最大梳距，无收缩](retraction_combing_max_distance.md)的设置。

<!--screenshot {
"image_path": "travel_avoid_other_parts_disabled.png",
"models": [{"script": "spike_curve.scad"}],
"camera_position": [0, 0, 116],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
"retraction_enable": false,
"travel_avoid_other_parts": false
},
"minimum_layer": 549,
"layer": 550,
"colours": 64
}-->
<!--screenshot {
"image_path": "travel_avoid_other_parts_enabled.png",
"models": [{"script": "spike_curve.scad"}],
"camera_position": [0, 0, 116],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
"retraction_enable": false,
"travel_avoid_other_parts": true
},
"minimum_layer": 549,
"layer": 550,
"colours": 64
}-->
![禁用时，空驶过程可以穿过其他零件](../images/travel_avoid_other_parts_disabled.png)
![启用后，空驶过程将避开其他零件](../images/travel_avoid_other_parts_enabled.png)

除了避开其他部分，空驶也会尽可能短地停留在墙壁附近。这意味着当通过壁退出或进入零件时，将垂直于壁。

此设置有助于提高打印的表面质量，因为喷嘴不会经常穿过墙壁。穿过壁会在其上留下伤痕，所以应该避免。

但是，该设置确实会增加渗出量，因为在不回抽的情况下会进行更多的空驶，并且距离会更长。对于大量渗出的材料，最好禁用本选项。

由于行程较长，打印时间可能会略微增加，但通常回抽减节省的时间会与之完全抵消。
