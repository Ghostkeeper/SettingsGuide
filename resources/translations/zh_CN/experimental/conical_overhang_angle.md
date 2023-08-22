最大模型角度
====
使用此设置配置[使悬垂可打印](conical_overhang_enabled.md)的悬垂角度。增加此角度可增加悬垂，从而减少Cura对模型的修改。减小此角度后，对象几乎不再有任何悬垂。

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
<!--screenshot {
"image_path": "conical_overhang_angle_20.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
"conical_overhang_enabled": true,
"conical_overhang_angle": 20
},
"colours": 8
}-->
![最大模型角度为50°](../images/conical_overhang_enabled_enabled.png)
![最大模型角度为20°](../images/conical_overhang_angle_20.png)

90°的角度将使模型与其所有悬垂保持原样。模型将不会被更改。0°角将使所有斜面完全垂直。

减小此角度会减小模型中的悬垂。这样可以让模型打印得更好。它不会下垂那么多，因此底部两侧的表面会更光滑。但是，这也会使打印的对象相对原模型有一些失真。它也将需要稍微多一点的时间和材料来打印它。

该角度也可以是负值。这使得整个打印件呈圆锥形，底部较宽。这可以产生有趣的效果，但没有真正的实际用途。
