支撑距离优先级
====
应准确观察[支撑X/Y距离](support_xy_distance.md)和[支撑Z距离](support_z_distance.md) ，确保它们不多也不少。这是过度约束，因此两者之间必须存在偏好。此设置确定该首选项。

X/Y覆盖Z
----
![X/Y覆盖Z](../images/support_xy_overrides_z.svg)

如果X/Y距离取代Z距离，则X/Y距离将永远保持不变，即使这表示Z距离大于所需的距离。但是，Z距离仍保持为最小距离，因此，如果悬垂非常水平，则Z距离仍会起作用，从而使X/Y距离大于所需距离。

Z覆盖X/Y
----
![Z覆盖X/Y](../images/support_z_overrides_xy.svg)

如果Z距离覆盖X/Y距离，则Z距离始终保持不变，即使这意味着X/Y距离小于所需距离。然后，X/Y距离仅在Z距离不起作用的位置才对打印产生影响，因此不在支撑结构的顶部处而是仅在侧面。

尽管如此，仍然可以观察到最小的X/Y距离。如果悬垂非常垂直，则X/Y距离将变得非常小，以至于支撑可能会与模型的侧面融合。[最小X/Y距离](support_xy_distance_overhang.md)可防止这种情况。
