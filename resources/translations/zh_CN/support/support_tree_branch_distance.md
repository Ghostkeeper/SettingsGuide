树形支撑分支间距
====
此设置确定两个相邻分支之间的距离，其中分支接触构造板。

<!--screenshot {
"image_path": "support_tree_branch_distance_1_4.png",
"models": [
{
"script": "gutter_lift.scad",
"transformation": ["scale(0.5)", "rotateZ(-90)"]
}
],
"camera_position": [0, 0, 180],
"settings": {
"support_enable": true,
"support_structure": "tree",
"support_tree_branch_distance": 1.4
},
"minimum_layer": 1310,
"layer": 1311,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_tree_branch_distance_5.png",
"models": [
{
"script": "gutter_lift.scad",
"transformation": ["scale(0.5)", "rotateZ(-90)"]
}
],
"camera_position": [0, 0, 180],
"settings": {
"support_enable": true,
"support_structure": "tree",
"support_tree_branch_distance": 5
},
"minimum_layer": 1310,
"layer": 1311,
"colours": 64
}-->
![树枝间隔1.4mm](../images/support_tree_branch_distance_1_4.png)
![树枝间隔5mm](../images/support_tree_branch_distance_5.png)

为了支撑模型，树形支撑将以交错网格模式在模型下方放置接触点。此设置基本上决定了栅格的大小，从而决定了分支之间的距离。由于分支相对于皮肤线的（默认）方向对齐，因此皮肤线需要桥接的距离很可能大于此距离。

通过减少分支距离，可以实现更好的悬垂质量，因为位于支架顶部的线不需要桥接那么远。由于更多的材料将用于支撑件的顶部，因此支撑件也将更硬，从而使打印更可靠。

然而，减少分支距离也会导致支撑占用更多的材料和印刷时间。

将分支距离减小到[分支直径](support_tree_branch_diameter.md)以下将导致分支在正确形成之前合并。因此，大悬垂区域的中心可能无法得到适当的支撑。
