启用锥形支撑
====
如果启用此设置，支撑结构的侧面将不再完全垂直。支撑将呈圆锥形，朝向底部变小或变大。

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
{
"script": "wide_overhang.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [91, -95, 19],
"settings": {
"support_enable": true,
"support_conical_enabled": true,
"support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_neg10.png",
"models": [
{
"script": "wide_overhang.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [91, -95, 19],
"settings": {
"support_enable": true,
"support_conical_enabled": true,
"support_conical_angle": -10
},
"colours": 64
}-->
![支撑向下收缩](../images/support_conical_enabled.png)
![支撑向下扩张](../images/support_conical_angle_neg10.png)

支撑面本身将以特定的倾斜[角度](support_conical_angle.md)。使用负角度时，支撑将朝底部变大，从而使支撑明显更稳定。如果角度为正，则越靠近底部，它将越小。这节省了大量的材料和打印时间。为了防止支撑变得不稳定，还可以为支撑定义[最小宽度](support_conical_min_width.md)。

锥形支撑是平衡打印时间和支撑稳定性的最有力的参数。锥形支撑有两种主要使用情况：
* 用来节省材料和打印时间。锥形支撑可以轻松地节省一半的支撑材料，并延长一半的打印时间。对于大而高的打印件，如果支持量很大，这一点尤其有效。
* 使用负角度使支撑面更稳定。如果您的打印有需要支撑的微小特征，它们通常会产生非常高的[塔](support_use_towers.md)，在打印过程中很容易翻倒。通过锥形支撑，这些高而薄的支撑结构可以在底部做得更宽。这给了它们一些额外的稳定性。但是，打印此支撑将需要更长的时间，因为它需要更多的材料。

当[支撑放置](support_type.md)设置为“支撑打印平台”，锥形支撑允许在模型周围延伸，以便在模型其他部分上方的位置仍然支撑模型。支撑件仍将只停留在构造板上，但由于其形状，可以到达其他支撑不能达到的角落中的悬垂区域。

它类似于一个简单且不太极端的版本：<!--if cura_version >= 4.7-->[树形支撑](support_structure.md)<!--endif--><!--if cura_version < 4.7:[树形支撑](../experimental/support_tree_enable.md)-->。树形支撑具有许多与锥形支撑相同的优点。然而，树形支撑使用完全不同的算法，并允许以更自由的方法生成支撑。而圆锥支撑则更符合常规的支撑算法。这意味着，普通支撑在与锥形支撑一起使用时往往效果更好。树形支撑则需要进行更大的调整。树形支撑结构有助于节省更多的材料和打印时间，同时保持打印可靠性。
