皮肤重叠
====
该设置使皮肤与相邻结构稍微重叠一点儿。这使得皮肤更好地粘附到这些结构上。

<!--screenshot {
"image_path": "skin_overlap_none.png",
"models": [{"script": "mounting_plate.scad"}],
"camera_position": [0, 0, 84],
"settings": {
"skin_outline_count": 0,
"skin_overlap": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "skin_overlap_20.png",
"models": [{"script": "mounting_plate.scad"}],
"camera_position": [0, 0, 84],
"settings": {
"skin_outline_count": 0,
"skin_overlap": 40
},
"colours": 64
}-->
![没有重叠](../images/skin_overlap_none.png)
![部分重叠](../images/skin_overlap_20.png)

从技术上讲，这种重叠会产生挤出过度，但过度挤出的量很小，因此不会被看到。这将对强度有很大的影响，因为皮肤可以更好地附着在墙壁和填充物上。毕竟，这些结构只有在它们有东西可以抓住的情况下才能增加模型的强度。

有一点重叠也有助于减少皮肤中间隙的产生。
