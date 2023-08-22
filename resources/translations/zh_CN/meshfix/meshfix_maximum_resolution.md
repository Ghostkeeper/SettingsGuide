最大分辨率
====
虽然高分辨率的输入一开始看起来更好，但打印机通常不能很好地处理高分辨率的g代码。因此，Cura将在切片过程中降低其输入的分辨率。此设置确定Cura将保持的最大分辨率。

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

此设置指示线段的最小长度。短于指定长度的线段将被视为与其他线段连接。如果新路径与原路径的偏移量不超过[最大偏移量](meshfix_maximum_deviation.md)<!--if cura_version>5.0-->并且其覆盖的区域不超过 [最大挤出面积偏移量](meshfix_maximum_extrusion_area_deviation.md)<!--endif-->，则它们将被合并。

请注意，如果顶点恰好对齐，则无法保证从每个层中删除相同的顶点。降低分辨率是通过在2D中移除层中形状的顶点而不是通过在3D中移除网格的顶点而执行的。因此，过多地降低分辨率通常会导致不规则的表面，而不是有角度的表面。

建议降低模型的分辨率，这样打印头的速度就不会为了等待CPU跟上而明显减慢。如果分辨率降低得不够，则在继续挤出的同时，打印头会降低其速度，从而使表面变得粗糙。如果分辨率降低太多，表面也会因为壁没有完全堆叠而变得粗糙。
