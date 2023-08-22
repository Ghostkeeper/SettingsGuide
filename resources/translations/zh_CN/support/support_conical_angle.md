锥形支撑角度
====
此设置确定打印锥形支撑面的倾斜角度。

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
{
"script": "wide_overhang.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [91, -95, 19],
"settings": {
"support_enable": true,
"support_conical_enabled": true,
"support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_10.png",
"models": [
{
"script": "wide_overhang.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [91, -95, 19],
"settings": {
"support_enable": true,
"support_conical_enabled": true,
"support_conical_angle": 10
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_neg10.png",
"models": [
{
"script": "wide_overhang.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [91, -95, 19],
"settings": {
"support_enable": true,
"support_conical_enabled": true,
"support_conical_angle": -10
},
"colours": 64
}-->
![30°角](../images/support_conical_enabled.png)
![10°角](../images/support_conical_angle_10.png)
![-10°角，使底部变宽](../images/support_conical_angle_neg10.png)

锥形支撑角度是支撑稳定性和产生的支撑量之间最主要的权衡因素。

使用大角度将使支撑在其高度的大部分上非常薄。这样可以节省大量的支撑材料和打印时间。当需要大量的支撑材料时，这可以节省大量的时间和材料，因为可以省去一半以上的支撑。然而，由于支撑件在底部变得非常薄，支撑件也可能变得不太稳定，从而增加了打印失败的机会。您可以增加[最小宽度](support_conical_min_width.md)来防止这种情况的发生。

使用负角度将使支撑朝向底部变宽，形状像火山。如果您的打印有需要支撑的微小特征，它们通常会产生非常高的[塔](support_use_towers.md)，在打印过程中很容易翻倒。在负角的情况下，这些高而薄的支撑结构将在底部被制造得更宽。这给了它们一些额外的稳定性。但是，打印此支撑将需要更长的时间，因为它需要更多的材料。大约-5 °的角度通常足以使最高、最薄的支撑结构具有足够的稳定性。如果您的材料在移动过程中渗出很多，则需要更大的负角度，因为支撑上的斑点会使结构受到更多的推动。
