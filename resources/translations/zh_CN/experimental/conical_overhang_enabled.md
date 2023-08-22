使悬垂可打印
====
此设置将转换模型，使其不再有任何悬垂。它将在任何悬垂下放置额外的材料，并将其打印为模型的一部分。

<!--screenshot {
"image_path": "conical_overhang_enabled_disabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
"conical_overhang_enabled": false
},
"colours": 8
}-->
<!--screenshot {
"image_path": "conical_overhang_enabled_enabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
"conical_overhang_enabled": true,
"conical_overhang_angle": 50
},
"colours": 8
}-->
![具有一些悬垂的塔](../images/conical_overhang_enabled_disabled.png)
![悬垂已变为可打印](../images/conical_overhang_enabled_enabled.png)

在所有悬垂件的下面，放置了一些材料，这些材料逐渐向下变小。在许多情况下，悬垂将向对象本身倾斜。使悬垂向对象增长的坡度由 [模型角度](conical_overhang_angle.md)确定。

此设置是一种避免需要任何支撑的简单方法。当打印表面有些粗糙或侧面有浮凸的模型时，此功能特别有效。这些小块的悬垂物通常会下垂，并产生松散的塑料线。它们可能会得到一些支撑，但这可能会花费大量的打印时间，而且仍然会留下一些伤痕。如果启用此设定，悬垂将向下平滑化至模型。看起来就像是原本想打印的样子。

如果悬垂从主体突出的距离大于其宽度，则仍可能会以直线的形式产生一些悬垂。这种情况的发生是因为突起被无限缩小，导致它消失。如果发生这种情况，您可以考虑是否仍有必要打印支撑。在上面的图片中，这种情况发生在塔的一侧的小块上，它小到使用简单的桥接就可以另其很好的悬垂。