支撑接触面水平扩展
====
此设置将使支撑界面在所有方向上水平展开到支撑的其余部分中。

<!--screenshot {
"image_path": "support_interface_offset.png",
"models": [{"script": "f.scad"}],
"camera_position": [45, 45, 133],
"settings": {
"support_enable": true,
"support_interface_enable": true,
"support_offset": 2,
"support_interface_offset": 1
},
"colours": 64
}-->
![支持接触面扩展为支撑](../images/support_interface_offset.png)

此机制有两种使用情形。
* 如果支撑界面直接终止于需要支撑的悬垂的边缘处，则构建材料可下垂到边缘。使接触面进一步扩展一点可以防止这种情况。
* 一些通常用于打印支撑的材料在低流量速率下挤出效果不佳，或者需要一些时间才能使用。小面积的支持界面不能很好地与这些材料配合。此设置可以使区域变大，以便有更多空间来拉伸这些材质。

由于技术限制，支撑接触面无法扩展到支撑本身之外。
