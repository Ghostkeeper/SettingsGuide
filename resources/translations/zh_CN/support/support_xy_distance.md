支撑X/Y距离
====
这表示支撑与模型之间必须保持的水平距离。

<!--screenshot {
"image_path": "support_xy_distance.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 185, 42],
"settings": {
"support_enable": true,
"support_xy_overrides_z": true,
"support_xy_distance": 2
},
"colours": 64
}-->
![支持和模型之间的水平间隙](../images/support_xy_distance.png)

水平距离是为了防止支撑撞击模型，否则会在曲面上留下伤痕。但是，这也会在模型和悬垂所在的支撑结构之间创建较大的距离，从而使较小的悬垂不受支撑。

X/Y与Z距离
----
X/Y距离和Z距离均应精确观测，确保不多也不少。这是过度约束，因此两者之间必须存在偏好。这由[支撑距离优先级](support_xy_overrides_z.md)指定。该设置将更改此"支撑X/Y距离"设置的行为。

![X/Y覆盖Z](../images/support_xy_overrides_z.svg)

如果X/Y覆盖Z，则会保留X/Y距离，即使这表示Z距离太大。Z距离仍保持为最小值。

![Z覆盖X/Y](../images/support_z_overrides_xy.svg)

如果Z覆盖X/Y，则会保留Z距离，即使这表示X/Y距离过小。这样，X/Y距离仅对远离支撑顶部的位置产生影响，而Z距离对该位置没有任何影响。
