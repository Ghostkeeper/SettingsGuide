树形支撑分支角度
====
此设置确定允许树形支撑的分支形成的最大悬垂角度。如果角度增加，则可以更水平地打印分支，使其延伸得更远。

<!--screenshot {
"image_path": "support_tree_angle_20.png",
"models": [{"script": "over_t.scad"}],
"camera_position": [-23, 124, 45],
"settings": {
"support_enable": true,
"support_structure": "tree",
"support_tree_collision_resolution": 0.02,
"support_tree_angle": 20
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_tree_angle_40.png",
"models": [{"script": "over_t.scad"}],
"camera_position": [-23, 124, 45],
"settings": {
"support_enable": true,
"support_structure": "tree",
"support_tree_collision_resolution": 0.02,
"support_tree_angle": 40
},
"colours": 64
}-->
![分支角度 20°](../images/support_tree_angle_20.png)
![分支角度 40°](../images/support_tree_angle_40.png)

减小分支角度将使分支更加垂直。增加它将使它们更加水平。因为允许分支具有更大的悬垂角度，所以它们可以更远地绕过障碍物，从而使支撑更经常地位于构造板上，而不是模型上。它还将允许分支在稍后的时间点分裂。

增加树枝角度对树形支撑的最重要影响包括：
* 减少了疤痕，因为需要在模型上而不是在构造板上停留的支撑更少。如果[支撑放置](../support/support_type.md) 设置为"支撑打印平台"，则可以支持更多的模型。
* 由于树枝在更高的海拔处分叉，因此减少了打印时间和材料使用量。树枝被及时地分开，以便能够到达所有的悬垂物。
* 可靠性降低。如果悬垂角度变得太大，则支撑件将被大大削弱，从而增加支撑件断裂或翻倒的机会。

较大的分支角度最好与较低的[树形支撑碰撞分辨率](support_tree_collision_resolution.md) 设置值相结合。这将减少由于避免碰撞而造成的支撑树位置偏移。这样可以防止在调整碰撞距离时悬垂距离变得太大。
