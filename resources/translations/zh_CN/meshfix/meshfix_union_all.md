联合覆盖体积
====
如果模型包含多个相交的体积块，则通常不会填充它们内部的体积块。该设置将导致Cura忽略内部结构，仅将它们整个填充，而不管体积周围有多少壳。

<!--screenshot {
"image_path": "meshfix_union_all_shell.png",
"models": [{"script": "intersecting_cubes.py"}],
"camera_position": [34, 86, 132],
"layer": -1,
"colours": 128
}-->
<!--screenshot {
"image_path": "meshfix_union_all_disabled.png",
"models": [{"script": "intersecting_cubes.py"}],
"camera_position": [34, 86, 132],
"settings": {"meshfix_union_all": false},
"layer": 300,
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_union_all_enabled.png",
"models": [{"script": "intersecting_cubes.py"}],
"camera_position": [34, 86, 132],
"settings": {"meshfix_union_all": true},
"layer": 300,
"colours": 64
}-->
![两个立方体相交的网格](../images/meshfix_union_all_shell.png)
![未联合所有体积](../images/meshfix_union_all_disabled.png)
![联合删除了孔洞](../images/meshfix_union_all_enabled.png)

在技术方面，此设置可有效地将缠绕规则从[偶数-奇数](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule) 更改为 [非零](https://en.wikipedia.org/wiki/Nonzero-rule)。通常，如果体积块被奇数个壳包围，则体积块会被填充。启用该设置后，如果它被非零数量的壳包围，则会填充该区域。

** 此操作仅适用于同一模型中的体积。如果加载了多个文件并使它们在Cura中相交，则此设置将不起作用。请参见移除网格交叉设置以修复多个单独网格重叠的问题。**
