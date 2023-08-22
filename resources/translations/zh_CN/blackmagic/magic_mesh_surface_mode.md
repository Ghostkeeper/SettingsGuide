表面模式
====
通常，Cura会创建网格中所有三角形的横截面。这些线段缝合在一起形成环。任何未闭合的循环都将被丢弃。

此设置控制将对这些未闭合回路执行的操作。如果设置为“正常”，则会丢弃它们。如果设置为“表面”，则所有横截面都将打印为轮廓。如果设置为“两者都”，则闭合的轮廓将正常打印，但未闭合的轮廓将作为额外的墙单独打印。

<!--screenshot {
"image_path": "magic_mesh_surface_mode_normal.png",
"models": [{"script": "extra_surface.py"}],
"camera_position": [66, 129, 124],
"settings": {
"magic_mesh_surface_mode": "normal"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "magic_mesh_surface_mode_surface.png",
"models": [{"script": "extra_surface.py"}],
"camera_position": [66, 129, 124],
"settings": {
"magic_mesh_surface_mode": "surface"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "magic_mesh_surface_mode_both.png",
"models": [{"script": "extra_surface.py"}],
"camera_position": [66, 129, 124],
"settings": {
"magic_mesh_surface_mode": "both"
},
"colours": 32
}-->
![正常模式忽略右侧的单个未闭合曲面](../images/magic_mesh_surface_mode_normal.png)
![表面模式仅打印表面，而不将其视为闭合体积](../images/magic_mesh_surface_mode_surface.png)
![在右侧打印体积和额外的未闭合曲面](../images/magic_mesh_surface_mode_both.png)

被打印的额外表面将仅包括作为单线的垂直表面。没有用于水平曲面的填充技术，因为表面不是闭合的多边形。因为没有内部，所以不能填充。不能有顶部、底部、填充物或支撑物。只有单行线。

额外的表面将被打印，就像它们是外墙一样，因此它们将受到外壁打印速度，走线宽度等的影响。它还将使用精确位于表面中心的线来打印这些曲面，而不是沿着模型的内部对齐线。这意味着它在表面的两侧以半个走线宽度延伸。这是因为表面的哪一侧是模型的内部是不明确的。您的打印尺寸将不准确。如果像上面的截图一样，额外的表面与正常的实心表面对齐，并且您正在使用“两者都”选项来完成任何缺失的墙壁，那么层将无法正确对齐。

**如果打印正常体积和额外表面，请记住，外壁将完全在打印的体积内。额外的表面被打印成以表面为中心的线，两边各占线宽的一半。如果一个额外的表面与一个封闭体积的表面对齐，如上图所示，该表面将移动半个走线宽度。毕竟，额外的表面没有内部可以移动。**
