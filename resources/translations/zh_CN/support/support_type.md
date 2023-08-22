支撑放置
====
此设置允许您选择可以放在什么支撑之上。

<!--screenshot {
"image_path": "support_type_everywhere.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
"support_enable": true,
"support_type": "everywhere"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "support_type_touching_buildplate.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
"support_enable": true,
"support_type": "buildplate"
},
"colours": 32
}-->
![为所有悬垂面生成支撑](../images/support_type_everywhere.png)
![仅在能够落脚在构造板上的位置生成支撑](../images/support_type_touching_buildplate.png)

将支撑放置在任何位置都可以使支撑更加可靠。所有可能下垂的悬垂都得到了适当的支撑。但是，支撑面也可能位于模型顶部，从而在接触的位置留下伤痕。这会降低移除支撑后模型表面的视觉品质和平滑度。

相反，仅当支撑接触到构造板时才放置支撑，可防止支撑停留在模型上。不过，这可能会使模型的某些部分不受支撑。

** 当只在构造板上使用支撑时，一个技巧是[启用锥形支撑](support_conical_enabled.md)并给与 [锥形支撑角度](support_conical_angle.md) 一个负值。这允许支撑面围绕模型增长，但仍支持大部分网格，而不停留在模型上。或者，尝试树形支撑。**
