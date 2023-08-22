最小支撑面积
====
此设置规定作为支撑件允许的最小尺寸。如果某个支撑在某层上的面积小于此设置的值，则该支撑将被忽略。

<!--screenshot {
"image_path": "minimum_support_area_0.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 190, 47],
"settings": {
"support_enable": true,
"minimum_support_area": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "minimum_support_area_10.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 190, 47],
"settings": {
"support_enable": true,
"minimum_support_area": 10
},
"colours": 64
}-->
![不对区域进行过滤（最小区域为0）](../images/minimum_support_area_0.png)
![忽略掉一些小的支撑](../images/minimum_support_area_10.png)

这种设置的存在是因为支撑的细支柱很可能会倒塌。他们还倾向于支持那些不需要支撑也可能很好地打印的小特征。如果支架翻倒，打印件上会留下许多斑点。因此，最好还是把这些细柱子去掉。此设置提供了一种通过柱的横截面积过滤掉支撑的方法。

增加区域将减少打印的支撑面数量，从而略微减少时间和材料用量。更重要的是，它提高了打印的可靠性，因为支撑柱倾倒的可能性更小。但是，它也会移除对打印中小特征的支持，因此这些部分的悬垂质量可能会恶化。

对于某些形状，如果顶部落在阈值区域之下，而底部没有，则这可能会产生移除支撑顶部的不良副作用。这可能会使您通常期望得到支撑的部分不受支撑。

<!--screenshot {
"image_path": "minimum_support_area_problem.png",
"models": [{"script": "overhang_bridging_cooling.scad"}],
"camera_position": [117, 0, 15],
"settings": {
"support_enable": true,
"minimum_support_area": 50
},
"colours": 64
}-->
![圆弧的尖端没有得到支撑，因为图层上的这些区域太小了](../images/minimum_support_area_problem.png)
