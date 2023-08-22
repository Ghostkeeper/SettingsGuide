立方体分区外壳
====
此设置使“立方体分区”填充图案开始向内部减少填充，以提高打印强度。

<!--screenshot {
"image_path": "sub_div_rad_add_small.png",
"models": [
{
"script": "cylinder.scad",
"transformation": ["scale(3)"]
}
],
"camera_position": [0, 0, 275],
"settings": {
"infill_sparse_density": 70,
"infill_pattern": "cubicsubdiv",
"sub_div_rad_add": 0
},
"layer": 500,
"colours": 32
}-->
<!--screenshot {
"image_path": "sub_div_rad_add_large.png",
"models": [
{
"script": "cylinder.scad",
"transformation": ["scale(3)"]
}
],
"camera_position": [0, 0, 275],
"settings": {
"infill_sparse_density": 70,
"infill_pattern": "cubicsubdiv",
"sub_div_rad_add": 5
},
"layer": 500,
"colours": 32
}-->
![没有附加的立方体分区](../images/sub_div_rad_add_small.png)
![附加5mm外壳后](../images/sub_div_rad_add_large.png)

“立方体分区”的工作原理是，如果没有任何立方体接触填充体积的边界，则删除八个相邻立方体之间的边界。此设置会将该边界进一步向内移动，从而防止删除立方体之间的边界。

实际上，这会使“立方体分区”图案更频繁按最大密度绘制。这增加了物体的强度，但也增加了打印物体所需的时间和材料。在极端情况下，将此设置增加到足够大的程度最终将导致“立方体分区”图案与简单的“立方体”图案相同。

您也可以将其设置为负数。这会导致立方体之间的边界更频繁地被移除，从而有效地减少边缘周围的填充量。
