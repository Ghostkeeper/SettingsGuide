树形支撑分支直径角度
====
树形支撑的树枝底部比顶部宽。这样可以确保无论支撑有多高，分支都保持稳定。使用此设置，可以控制支持面变宽的速率。

<!--screenshot {
"image_path": "support_tree_branch_diameter_1_4mm_5.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
"support_enable": true,
"support_structure": "tree",
"support_tree_branch_diameter": 1.4,
"support_tree_branch_diameter_angle": 5,
"support_angle": 80
},
"structures": ["helpers"],
"colours": 16
}-->
<!--screenshot {
"image_path": "support_tree_branch_diameter_angle_10.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
"support_enable": true,
"support_structure": "tree",
"support_tree_branch_diameter": 1.4,
"support_tree_branch_diameter_angle": 10,
"support_angle": 80
},
"structures": ["helpers"],
"colours": 16
}-->
![树枝直径角为5°](../images/support_tree_branch_diameter_1_4mm_5.png)
![树枝直径角为10°](../images/support_tree_branch_diameter_angle_10.png)

角度越大，树形支撑的底部将变得越宽，尤其是对于高模型。这有几个影响：
* 较宽的底部确保了支撑更难倾倒。这增加了树形支撑的可靠性。
* 较宽的底部需要更多的材料和时间来打印。
* 支撑角度的总和等于最大[角度](support_tree_angle.md) ，在该值下，树枝可以悬垂，因此在某些情况下，非常高的值可能会导致树形支撑不够坚固。
* 较宽的分支较难在网格周围导航，从而更难从构造板到达悬垂的某些部分。因此，支撑可能需要放置在模型上而不是构造板上，从而增加了疤痕的数量。
* 对于Cura，树的冲突避免更难计算，从而导致切片时间增加。这可以通过增加[树形支撑碰撞分辨率](support_tree_collision_resolution.md)设置来抵消，但这也会降低树形支撑的结构完整性。

通常，您希望树形支撑的角度足够宽，以在任何高度支撑自身，而不会变得过于摇晃。
