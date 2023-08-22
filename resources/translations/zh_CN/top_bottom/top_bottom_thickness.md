顶层/底层厚度
====
通过“顶层/底层厚度”设置，您可以调节顶面和底面实体皮肤的厚度。

<!--screenshot {
"image_path": "top_bottom_thickness_0.8.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 203, 30],
"settings": {
"wall_line_count": 0,
"top_bottom_thickness": 0.8
},
"colours": 64
}-->
<!--screenshot {
"image_path": "top_bottom_thickness_3.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 203, 30],
"settings": {
"wall_line_count": 0,
"top_bottom_thickness": 3
},
"colours": 64
}-->
![普通顶层/底层厚度](../images/top_bottom_thickness_0.8.png)
![更厚的顶部和底部](../images/top_bottom_thickness_3.png)

该设置同时影响打印的顶面和底面。也可以通过[顶层厚度](top_thickness.md) 和 [底层厚度](bottom_thickness.md)对顶、底进行单独配置。

如果此设置不是层高的倍数，将四舍五入到最接近的倍数。仅用来确定顶部层数和底部层数的生成数量。

更大的顶层和底层厚度将产生广泛影响，对整体质量有利，对生产效率不利。
* 部件的强度更好。更大的顶层和底层厚度意味着模型需要被稀疏的填充图案填充的部分变小。这反而使它完全坚固。
* 部件的表面更光滑。顶层皮肤的任何枕形效应和下沉都会在上层得到平滑。
* 模型更具防水性。更多的层可以阻挡水及其他液体的侵入，还能恢复沉降的悬垂。
* 更多的层被完全填充，打印将消耗更多材料。
* 更多的材料需要被打印，且这些层的速度比填充慢得多，打印更费时。
