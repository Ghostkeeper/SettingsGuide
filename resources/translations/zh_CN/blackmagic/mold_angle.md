模具角度
====
类似于[使悬垂可打印](../experimental/conical_overhang_enabled.md)功能，此设置修改模具的形状，使其可以在没有支撑的情况下打印。只有模具的外部形状被修改，所以你的铸件的形状不会受到影响。

<!--screenshot {
"image_path": "mold_angle.png",
"models": [
{
"script": "star_podium.scad",
"transformation": ["mirrorZ"]
}
],
"camera_position": [81, 129, 45],
"settings": {
"mold_enabled": "True"
},
"colours": 48
}-->
![40度的角度允许该模具的底部打印而不需要任何支撑](../images/mold_angle.png)

减小该角度将减小悬垂的末端。这将使打印更可靠。然而，它也会使打印的基础更宽，这大大增加了打印的持续时间，并增加了它将使用的材料量。

对于某些形状，修改模具的外部形状不足以使其正确打印。它仍然需要支撑。您可以通过启用[圆锥支撑](../support/support_conical_enabled.md)来实现类似的效果。

<!--screenshot {
"image_path": "mold_needs_support.png",
"models": [{"script": "basic_overhang.scad"}],
"camera_position": [20, 183, 97],
"settings": {
"mold_enabled": "True"
},
"colours": 32
}-->
![此模具仍需要支撑](../images/mold_needs_support.png)
