移除所有孔洞
====
一些模型，特别是那些为注塑成型等制造技术制造的模型，往往带有不可见的内腔。如果启用此设定，Cura会移除这些内部空腔。

<!--screenshot {
"image_path": "meshfix_union_all_remove_holes_disabled.png",
"models": [{"script": "foothold.scad"}],
"camera_position": [-68, 40, 46],
"settings": {"meshfix_union_all_remove_holes": false},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_union_all_remove_holes_enabled.png",
"models": [{"script": "foothold.scad"}],
"camera_position": [-68, 40, 46],
"settings": {"meshfix_union_all_remove_holes": true},
"colours": 64
}-->
![This model has a hole in the centre](../images/meshfix_union_all_remove_holes_disabled.png)
![启用此设置后，将删除孔](../images/meshfix_union_all_remove_holes_enabled.png)

内部的空腔可能是为了节省材料而设计的，但在3D打印中，有一些限制会导致这些模型打印效果更差。例如，3D打印机无法很好地处理不是走线宽度的倍数的薄壁，并且如果不受填充的支撑，顶部皮肤往往会下垂。通常，最好制作一个实体网格，然后让切片器决定如何填充它。通过该网格修复设置，无需编辑网格即可执行此操作。

Cura只会在水平方向上查看空腔是否完全封闭。它不会查看型腔是可从顶部还是底部进入。从顶部或底部可能仍然可以看到差异。
