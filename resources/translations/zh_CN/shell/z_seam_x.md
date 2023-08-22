Z缝X
====
如果在[z缝对齐](z_seam_type.md) 中设置为”用户指定“，那么接缝将放在靠近“z 缝 x”和[z 缝 y](z_seam_y.md) 设置的地方。

<!--screenshot {
"image_path": "z_seam_x_left.png",
"models": [
{
"script": "rod_holder.scad",
"transformation": ["rotateZ(-90)"]
}
],
"camera_position": [-55, 128, 40],
"settings": {
"z_seam_type": "back",
"z_seam_position": "left"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_x_right.png",
"models": [
{
"script": "rod_holder.scad",
"transformation": ["rotateZ(-90)"]
}
],
"camera_position": [55, 128, 40],
"settings": {
"z_seam_type": "back",
"z_seam_position": "right"
},
"colours": 64
}-->
![接缝位于模型左侧](../images/z_seam_x_left.png)
![接缝位于模型右侧](../images/z_seam_x_right.png)

[Z缝相对](z_seam_relative.md)关闭时，该设置指定构造板上的一个绝对坐标。“Z缝相对”开启时则指定相对于模型中心的位置。使用绝对引用时，坐标采用g-code坐标系，这不同于Cura中放置对象采用的坐标。

选择打印过程中难以看到的位置放置接缝为好。如果没有这种位置或者可以进行必要的打印后处理，也可以选择一个打印后方便用刀切除的位置。
