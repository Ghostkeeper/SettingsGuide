仅在外部打印 Brim
====
如果模型在构造板上的起始层中有孔，则此设置将阻止沿孔的内侧打印Brim。

<!--screenshot {
"image_path": "brim_outside_only_original.png",
"models": [{"script": "holes_in_panel.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"adhesion_type": "brim",
"brim_line_count": 10,
"brim_outside_only": false
},
"layer": 1,
"colours": 32
}-->
<!--screenshot {
"image_path": "brim_outside_only_enabled.png",
"models": [{"script": "holes_in_panel.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"adhesion_type": "brim",
"brim_line_count": 10,
"brim_outside_only": true
},
"layer": 1,
"colours": 32
}-->
![Brim在所有位置打印](../images/brim_outside_only_original.png)
![Brim仅在外部](../images/brim_outside_only_enabled.png)

内侧的Brim通常在打印件和构造板之间增加非常少的额外粘合强度，并且对防止收缩没有效果。在打印完成后，移除内侧的Brim可能会节省一些时间，因为您不需要从内侧孔移除Brim。

**如果孔内有其他物体，则由于技术限制，无法移除Brim。**
