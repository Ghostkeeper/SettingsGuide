最大偏移量
====
虽然高分辨率的输入一开始看起来更好，但打印机通常不能很好地处理高分辨率的g代码。因此，Cura将在切片过程中降低其输入的分辨率。此设置决定了缩小后的路径可以偏离原始路径多远，以降低分辨率。

<!--screenshot {
"image_path": "meshfix_maximum_resolution_0.05.png",
"models": [{"script": "cylinder.scad"}],
"camera_position": [40, -20, 116],
"settings": {
"meshfix_maximum_resolution": 0.05
},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_maximum_resolution_1.png",
"models": [{"script": "cylinder.scad"}],
"camera_position": [40, -20, 116],
"settings": {
"meshfix_maximum_resolution": 4,
"meshfix_maximum_deviation": 0.5
},
"colours": 64
}-->
![降低分辨率之前](../images/meshfix_maximum_resolution_0.05.png)
![降低分辨率（最大值）后](../images/meshfix_maximum_resolution_1.png)

打印机需要在执行G代码时对其进行处理。如果g代码包含许多微小的线段，则打印头的移动速度可能过快，使得3D打印机的处理器无法跟上。这具有打印头将偶尔减慢以允许CPU赶上或简单地等待下一个运动命令的效果。这会导致表面变得非常粗糙，甚至出现小的斑点，因为流出喷嘴的流量速率与喷嘴的零星运动不完全匹配。有时，较低的分辨率会产生较好的打印品质。

此设置指示允许新的分辨率降低路径偏离原始高分辨率路径的距离。如果直线比[最大分辨率](meshfix_maximum_resolution.md)短，则认为它们将与其他线段连接，但如果此快捷方式导致路径偏离的距离超过此设置所指示的距离，则不会连接这些直线。

请注意，如果顶点恰好对齐，则无法保证从每个层中删除相同的顶点。降低分辨率是通过在2D中移除层中形状的顶点而不是通过在3D中移除网格的顶点而执行的。因此，过多地降低分辨率通常会导致不规则的表面，而不是有角度的表面。

为确保结构完整性，强烈建议路径的偏差不得超过线宽的一半。但是，如果曲面需要平滑或美观，则此设置基本上指示曲面上允许的不规则深度。最大偏移量需要非常低，以便不被肉眼看到。

但是，如果将最大偏移量减小得太多，则会大大限制分辨率的降低。由于CPU无法跟上短移动命令，因此生成的g代码可能无法很好地打印。
