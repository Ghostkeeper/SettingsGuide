树形支撑分支直径
====
此设置允许您调整树形支撑的分支宽度。此处指定的宽度将是树分支顶部的宽度。根据[树形支撑分支直径角度](support_tree_branch_diameter_angle.md) 设置，分支的最尖端将更细，并向底部逐渐变宽。

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
"image_path": "support_tree_branch_diameter_5mm.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
"support_enable": true,
"support_structure": "tree",
"support_tree_branch_diameter": 5,
"support_tree_branch_diameter_angle": 5,
"support_angle": 80
},
"structures": ["helpers"],
"colours": 16
}-->
![直径为1.4毫米的树枝的形状](../images/support_tree_branch_diameter_1_4mm_5.png)
![直径为5毫米的树枝形状](../images/support_tree_branch_diameter_5mm.png)

更宽的树枝更稳定，减少了树被喷嘴撞倒的机会，如果它需要穿过它。

更宽的分支也会更快地合并在一起。这将节省一些材料，但也可能会阻止模型的一些部分得到适当的支撑，实际上还有一些支撑本身。当分支合并在一起时，它们不再有轮廓。宽分支最好与宽[间距](support_tree_branch_distance.md) 或某些[填充](../support/support_infill_rate.md) 结合使用，以便正确支撑宽分支中间的零件。

更宽的分支也会更难在模型中导航。这可能会导致更多的支撑位于模型上，而不是构造板上。因此，移除支撑结构后，模型可能会有更多疤痕。
