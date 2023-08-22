Z缝对齐
====
该设置允许您选择每层轮廓接缝的位置。多个可用的选项确保将接缝的影响最小化或允许您在后处理过程更轻松的去除它们。

接缝出现在打印开始和结束的地方。即便喷嘴的路径是闭合的圆，但由于打印过程不是完全精确的，在挤出开始和结束的地方仍会留下接缝。通过本设置可以隐藏或分散这些接缝，让它们的观感尽量不明显。

<!--screenshot {
"image_path": "z_seam_type_user.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
"z_seam_corner": "z_seam_corner_outer",
"z_seam_position": "left",
"z_seam_type": "back"
},
"colours": 32
}-->
User specified
----
![用户指定](../images/z_seam_type_user.png)

该选项允许您手动选择位置。接缝会被放置在离所选位置最近的角落。这通常会让角落非常拥挤的排在一起，从而可以轻松的切除它们。它还允许对接缝位置进行精细的控制。

默认位置会选在打印机后面的一个位置上。它的逻辑是用户一般将模型的正面朝向打印机的正面，所以背面的位置可以更好的隐藏接缝。

<!--screenshot {
"image_path": "z_seam_type_shortest.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
"z_seam_corner": "z_seam_corner_outer",
"z_seam_type": "shortest"
},
"colours": 32
}-->
最短
----
![最短](../images/z_seam_type_shortest.png)

该选项不会在位置选择上花什么力气，只是简单的将通向接缝的行程最小化。由于行程缩短，会节省一小部分时间。由于材料在喷头停靠时的流出减少，接缝也稍小些。

期望的缝隙角偏好仍然通过挑选靠近喷嘴的角来保持。不是使用最近的角，而是利用加权偏好最小化行程，同时也会使用接近[缝隙角偏好设置](z_seam_corner.md) 的值。

<!--screenshot {
"image_path": "z_seam_type_random.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
"z_seam_corner": "z_seam_corner_outer",
"z_seam_type": "random"
},
"colours": 32
}-->
随机
----
![随机](../images/z_seam_type_random.png)

该选项将接缝随机放在的围绕周边的一个位置上。这个随机的位置在每一层都会变化，所以接缝彼此非常分散甚至围绕整个模型。因为这些不同层的接缝没有对齐，所以它们通常较难看被看到。然而，表面会看起来稍微乱些。

<!--screenshot {
"image_path": "z_seam_type_sharpest.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
"z_seam_corner": "z_seam_corner_outer",
"z_seam_type": "sharpest_corner"
},
"colours": 32
}-->
最尖角
----
![最尖角](../images/z_seam_type_sharpest.png)

接缝会根据[缝隙角偏好设置](z_seam_corner.md) 的值放置在整个轮廓最尖锐的角落上。虽然可能导致行程延长，但可以确保接缝根据设置得到最大程度的隐藏或暴露。
