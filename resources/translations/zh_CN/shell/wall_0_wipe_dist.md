外壁擦嘴长度
====
通过此设置，在每个外壁的末端，喷嘴将在停止挤出后再移动一小段距离，擦拭轮廓使其封闭。

<!--screenshot {
"image_path": "wall_0_wipe_dist.png",
"models": [
{
"script": "thin_cylinder.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 0, 50],
"settings": {
"wall_0_wipe_dist": 4
},
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"minimum_layer": 2,
"layer": 2,
"colours": 16
}-->
![外壁完成后再移动一小段行程](../images/wall_0_wipe_dist.png)

此设置旨在降低接缝的可见性。当壁正常完成时，材料液滴仍略微的在喷嘴后面。这一小段行程会将液滴和壁的起点连起来，从而闭合了接缝。

接缝仍是可见的，但擦嘴长度较小时效果好一些。设置的太高效果不会更好，因为喷嘴已经离开了缝隙，而且随后由于喷嘴室材料渗出易造成挤出不足。

该效果基本上与 [启用滑行](../experimental/coasting_enable.md)相反，后者将在轮廓完成前稍微停止挤出。
