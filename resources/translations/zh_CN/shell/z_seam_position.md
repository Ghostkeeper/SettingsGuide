Z缝位置
====
如果在[z缝对齐](z_seam_type.md) 中设置为”用户指定“，那么接缝将按照此设置指定的方向放置。

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
![接缝位于模型左侧](../images/z_seam_x_left.png)
![接缝位于模型背面](../images/z_seam_y_back.png)
![接缝位于模型右侧](../images/z_seam_x_right.png)
![接缝位于模型前面](../images/z_seam_y_front.png)

接缝有八个可选择的方向。最好选择一个在打印完成后很难看到的位置，这与您的设计息息相关。通常最好将接缝选在内部转弯处，如果没有的话也可以选择一个打印后方便用刀切除的位置。

**接缝会尽可能精确的放在[z缝x](z_seam_x.md) 和[z缝y](z_seam_y.md) 设置的地方。在那里可以更直观的进行设置。**
