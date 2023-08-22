底部皮肤扩展距离
====
决定底层的实体层在水平方向上的宽或窄（薄）。通常只有接触空气的部分会生成为实体层，该设置可让它在水平方向上略作扩展，这会使皮肤与相邻的壁结合的更牢，还会填充皮肤的缝隙，部件的强度得到了改善。

<!--screenshot {
"image_path": "skin_preshrink_original.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"bottom_skin_preshrink": 0,
"top_skin_preshrink": 0,
"bottom_skin_expand_distance": 0,
"top_skin_expand_distance": 0,
"max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
<!--screenshot {
"image_path": "expand_skins_expand_distance_1mm.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"bottom_skin_expand_distance": 1,
"top_skin_expand_distance": 1,
"max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
![皮肤 (黄色部分) 的一般外观](../images/skin_preshrink_original.png)
![皮肤扩展1mm后](../images/expand_skins_expand_distance_1mm.png)

* 如果在皮肤的底层存在小洞（其被填充图案填充），稍微调高此值可以将它们关闭。这允许打印机持续打印底部线条，大大提高强度。
* 如果有一个底面没有直接和构造板接触，那么皮肤层下面将会有墙壁。这将增强底层与附近墙壁之间的附着力，因为底层将直接印在墙壁的顶部。
* 该值调为负值则会减少底层的宽度，由填充层取而代之。即以强度损失为代价节约打印时间。

**技术所限，您不能将该值负向调整的比[底部皮肤移除宽度](bottom_skin_preshrink.md)还低。增加底部皮肤移除宽度的设置来去除更多的皮肤。**
