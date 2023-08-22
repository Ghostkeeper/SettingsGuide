优化壁打印顺序
====
启用此功能后，Cura将花费一些额外的切片时间来优化壁打印顺序围绕同一位置的所有壁打完后再进行到下个位置打印。目的旨在减少移动和回抽的次数。

<!--screenshot {
"image_path": "optimize_wall_printing_order_disabled.gif",
"models": [
{
"script": "plate_with_indent.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 0, 120],
"settings": {
"skin_outline_count": 0,
"optimize_wall_printing_order": false
},
"layer": 37,
"line": [0, 5, 9, 13, 17, 25, 29, 33, 37, 47, 54, 61, 71, 89, 106, 122, 142, 156, 160, 164, 169, 176, 183, 188, 194, 225, 241, 262, 282, 293, 297, 302, 309, 319, 326, 332, 343, 353, 358, 363, 368],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "optimize_wall_printing_order_enabled.gif",
"models": [
{
"script": "plate_with_indent.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 0, 120],
"settings": {
"skin_outline_count": 0,
"optimize_wall_printing_order": true
},
"layer": 37,
"line": [0, 4, 7, 11, 17, 25, 31, 36, 41, 47, 51, 55, 60, 67, 71, 76, 83, 92, 99, 106, 114, 123, 130, 136, 147, 165, 181, 197, 217, 239, 256, 278, 299, 312, 316, 320, 325, 331, 336, 343, 350],
"delay": 125,
"colours": 32
}-->
![没有优化时](../images/optimize_wall_printing_order_disabled.gif)
![优化后](../images/optimize_wall_printing_order_enabled.gif)

启动该优化后，喷嘴会把一个位置的壁打好，然后再去别处。而不是先把所有内壁打完再打印外壁。优化通常是积极的，但对某些零件因为前一个壁尚未固化就打印下一个壁，会影响尺寸精度。

如果内外壁的流量不同，该优化会加剧这种不同。先出现明显的[接缝](../troubleshooting/seam.md) 或[斑点](../troubleshooting/blobs.md)。走线宽度比此设置更具影响力，所以您的打印机如果有此问题请关闭优化。
