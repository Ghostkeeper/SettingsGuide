顶层厚度
====
该设置决定实心顶层的厚度。这个实体层将取代填充被打印。以封闭顶部。

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
"image_path": "top_thickness.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 203, 30],
"settings": {
"wall_line_count": 0,
"top_thickness": 3
},
"colours": 64
}-->
![普通顶层厚度](../images/top_bottom_thickness_0.8.png)
![厚度大幅增加后](../images/top_thickness.png)

一个厚实的顶部有诸多效果，对顶面质量有利，对生产效率不利。
* 部件的强度更好。拥有更厚的顶部意味着模型需要被稀疏的填充图案填充的部分变小。这反而使它完全坚固。
* 部件的表面更光滑。顶层皮肤任何的枕形效应和下沉都会在额外的层中得到平滑。
* 模型更具防水性。厚实的顶部具有更多完全填充的层来阻挡水或其他液体的渗入。
* 更多的层被完全填充，打印将消耗更多材料。
* 更多的材料需要被打印，且这些层的速度比填充慢得多，打印更费时。
