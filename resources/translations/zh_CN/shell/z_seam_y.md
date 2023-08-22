Z缝Y
====
如果在[z缝对齐](z_seam_type.md) 中设置为”用户指定“，那么接缝将放在靠近[z 缝 x](z_seam_x.md) 和“z 缝 y”设置的地方。

<!--screenshot {
"image_path": "z_seam_y_back.png",
"models": [
{
"script": "rod_holder.scad",
"transformation": ["rotateZ(-90)"]
}
],
"camera_position": [0, -77, 130],
"settings": {
"z_seam_type": "back",
"z_seam_position": "back"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_y_front.png",
"models": [
{
"script": "rod_holder.scad",
"transformation": ["rotateZ(-90)"]
}
],
"camera_position": [0, 77, 130],
"settings": {
"z_seam_type": "back",
"z_seam_position": "front"
},
"colours": 64
}-->
![接缝位于模型前面](../images/z_seam_y_front.png)
![接缝位于模型背面](../images/z_seam_y_back.png)

 [Z缝相对](z_seam_relative.md)关闭时，该设置指定构造板上的一个绝对坐标。“Z缝相对”开启时则指定相对于模型中心的位置。使用绝对引用时，坐标采用g-code坐标系，这不同于Cura中放置对象采用的坐标。

选择打印过程中难以看到的位置放置接缝为好。如果没有这种位置或者可以进行必要的打印后处理，也可以选择一个打印后方便用刀切除的位置。
