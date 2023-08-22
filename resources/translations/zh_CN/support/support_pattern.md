支撑图案
====
使用此设定，您可以选择填充支撑结构体积的模式。不同的模式有不同的优缺点。

<!--screenshot {
"image_path": "support_pattern_lines.png",
"models": [
{
"script": "calendar_holder.scad",
"transformation": ["rotateX(90)"]
}
],
"camera_position": [0, 0, 135],
"settings": {
"support_enable": true,
"support_pattern": "lines"
},
"structures": ["helpers"],
"colours": 16
}-->
直线
----
![直线（走线）](../images/support_pattern_lines.png)

直线模式会绘制直线。这些线的方向是这样的，即它们永远不会垂直于它需要支撑的皮肤线（默认情况下）。
* 是所有模式中最容易从模型拆除的。如果有一个悬垂区域靠近构造板，这将非常有用。如有必要，可使用小刀切去残留物。
* 与锯齿形合用是所有模式中悬垂质量最好的。这些线非常靠近，并且定向为不垂直于皮肤。
* 倾向于不稳定，因为支撑线易于倾倒。

<!--screenshot {
"image_path": "support_pattern_grid.png",
"models": [
{
"script": "calendar_holder.scad",
"transformation": ["rotateX(90)"]
}
],
"camera_position": [0, 0, 135],
"settings": {
"support_enable": true,
"support_pattern": "grid"
},
"structures": ["helpers"],
"colours": 16
}-->
网格
----
![网格](../images/support_pattern_grid.png)

网格图案绘制两组相互垂直的直线。它们重叠在一起，形成一个正方形的图案。依预设，会围绕此样式绘制一个轮廓。
* 非常坚固，增加可靠度。
* 由于线之间的距离相当远，因此可提供中等的悬垂质量。
* 由于支架不会弯曲太多，因此很难拆卸。

<!--screenshot {
"image_path": "support_pattern_triangles.png",
"models": [
{
"script": "calendar_holder.scad",
"transformation": ["rotateX(90)"]
}
],
"camera_position": [0, 0, 135],
"settings": {
"support_enable": true,
"support_pattern": "triangles"
},
"structures": ["helpers"],
"colours": 16
}-->
三角形
----
![三角形](../images/support_pattern_triangles.png)

三角形图案绘制三组彼此成60度角的直线，形成等边三角形的图案。依预设，会围绕此样式绘制一个轮廓。
* 所有支撑图案中最坚固的一种。
* 由于线之间的距离很远，因此悬垂质量较差。
* 可能很难移除，因为支架在任何方向都不会弯曲。

<!--screenshot {
"image_path": "support_pattern_concentric.png",
"models": [
{
"script": "calendar_holder.scad",
"transformation": ["rotateX(90)"]
}
],
"camera_position": [0, 0, 135],
"settings": {
"support_enable": true,
"support_pattern": "concentric"
},
"structures": ["helpers"],
"colours": 16
}-->
同心圆
----
![同心](../images/support_pattern_concentric.png)

同心图案让支撑件由从外到内均匀间隔的同心环组成。
* 如果线的方向恰好垂直，则线靠得很近，为平滑曲面的悬垂区域提供了良好的支撑。
* 相当坚固，因为每个圆环都有很大的宽度可供站立。
* 易于拆卸，因为支撑结构易于向内弯曲。
* 通常与需要支撑的墙壁平行。这会导致悬垂质量变差，因为有些墙根本得不到支撑。
* 有时会导致支撑被悬在半空中。

<!--screenshot {
"image_path": "support_pattern_zigzag.png",
"models": [
{
"script": "calendar_holder.scad",
"transformation": ["rotateX(90)"]
}
],
"camera_position": [0, 0, 135],
"settings": {
"support_enable": true,
"support_pattern": "zigzag"
},
"structures": ["helpers"],
"colours": 16
}-->
锯齿形
----
![锯齿形](../images/support_pattern_zigzag.png)

锯齿形图案与线条图案类似，但线条在末端连接。
* 相当坚固，大大提高了可靠性。
* 与直线一起提供所有样式中的最佳悬垂品质。这些线非常靠近，并且定向为不垂直于皮肤。
* 易于拆卸。支撑结构向内弯曲，在上面拉的时候，支撑就会成条状拉掉。
* 几乎总是在一条直线上画出支撑，最大限度地减少了回抽或空驶的需要。

<!--screenshot {
"image_path": "support_pattern_cross.png",
"models": [
{
"script": "calendar_holder.scad",
"transformation": ["rotateX(90)"]
}
],
"camera_position": [0, 0, 135],
"settings": {
"support_enable": true,
"support_pattern": "cross"
},
"structures": ["helpers"],
"colours": 16
}-->
交叉
----
![交叉](../images/support_pattern_cross.png)

交叉图案在整个体积中绘制分形图案，其中具有十字形状。
* 在所有图案中最容易弯曲，因为此图案中没有长直线。
* 几乎总是在一条直线上画出支撑，最大限度地减少了回抽或空驶的需要。

<!--screenshot {
"image_path": "support_pattern_gyroid.png",
"models": [
{
"script": "calendar_holder.scad",
"transformation": ["rotateX(90)"]
}
],
"camera_position": [0, 0, 135],
"settings": {
"support_enable": true,
"support_pattern": "gyroid"
},
"structures": ["helpers"],
"colours": 16
}-->
<!--if cura_version >= 4.1-->
螺旋二十四面体
----
![螺旋二十四面体](../images/support_pattern_gyroid.png)

螺旋二十四面体是波浪形的，沿曲线来回摆动。曲线在各层之间变化。
* 相当坚固的图案，增加了可靠性。
* 支撑间的空气是一个整体。当用可溶性支撑材料打印时，这允许溶剂（水、乙醇或其它）突出到支撑结构的所有内部，即使在下面存在边缘。这使其能够更快地溶解支持物。
* 均匀支持悬垂中的所有线，而不考虑其方向。
<!--endif-->
