启用支撑Brim
====
当启用了支撑brim, 将在首层的支撑区域内绘制一个额外的brim。

<!--screenshot {
"image_path": "support_brim_4mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
"support_enable": true,
"support_use_towers": false,
"support_brim_enable": true,
"support_brim_width": 4
},
"colours": 64
}-->
![支撑Brim](../images/support_brim_4mm.png)

与普通Brim不同，支撑Brim朝向 *内侧*。如果[构造板附着类型](../platform_adhesion/adhesion_type.md)设置为"Brim"，则还会在支撑 *周围* 绘制另一个brim。

该Brim的目的是为支撑提供更多的表面积，使其可以附着在构造板上。这也可以通过调整[起始层支撑走线距离](support_initial_layer_line_distance.md)来实现，但是使用此功能，附着力将集中在支持区域的边缘，在那里可以更有效地防止翘曲。

支撑Brim也会稍微增加印刷时间和材料成本，但由于它只在第一层，所以是极小的。这使得支撑明显增强，所以对于锯齿形支撑图案来说，它可能会变得更难折断。
