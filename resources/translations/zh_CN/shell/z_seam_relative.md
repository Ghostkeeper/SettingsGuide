Z缝相对
====
当根据[z 缝对齐](z_seam_type.md) 的设置指定了缝隙的位置，则可以输入缝隙必须被放置的坐标。一般时指定构造板上的某个位置，比如打印机背面。 如果开启本选项，会依据与模型的相对位置选择这些坐标。

<!--screenshot {
"image_path": "z_seam_relative_disabled.png",
"models": [
{
"script": "rod_holder.scad",
"transformation": ["translateX(-30)", "translateY(-20)"]
},
{
"script": "rod_holder.scad",
"transformation": ["translateX(30)", "translateY(-20)"]
},
{
"script": "rod_holder.scad",
"transformation": ["translateX(30)", "translateY(20)"]
},
{
"script": "rod_holder.scad",
"transformation": ["translateX(-30)", "translateY(20)"]
},
{
"script": "cylinder.scad",
"transformation": ["scale(0.25)"]
}
],
"camera_position": [0, 0, 250],
"settings": {
"z_seam_type": "back",
"z_seam_x": 500,
"z_seam_y": 500,
"z_seam_relative": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_relative_enabled.png",
"models": [
{
"script": "rod_holder.scad",
"transformation": ["translateX(-30)", "translateY(-20)"]
},
{
"script": "rod_holder.scad",
"transformation": ["translateX(30)", "translateY(-20)"]
},
{
"script": "rod_holder.scad",
"transformation": ["translateX(30)", "translateY(20)"]
},
{
"script": "rod_holder.scad",
"transformation": ["translateX(-30)", "translateY(20)"]
},
{
"script": "cylinder.scad",
"transformation": ["scale(0.25)"]
}
],
"camera_position": [0, 0, 250],
"settings": {
"z_seam_type": "back",
"z_seam_x": 500,
"z_seam_y": 500,
"z_seam_relative": true
},
"colours": 64
}-->
![禁用时：坐标指向构造板中心的绝对位置，所有模型的白色条纹都指向中间。](../images/z_seam_relative_disabled.png)
![开启时： 坐标相对于模型，所有模型的白色条纹都处于相同的位置。](../images/z_seam_relative_enabled.png)

当在构造板上复制网格时，无论该复制品被放在哪里，此设置都会使它们的接缝位置完全相同，而不是指向同一个点。这允许您用完全一致方式的打印每个副本，而不管它在构造板上的位置。
