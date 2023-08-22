启用连桥设置
====
当您的模型有一些两侧支撑的悬垂时，Cura将检测到这一点，并修改悬垂的皮肤区域以更好地打印。如果启用了此设置，则可以调整对这些连桥区域的检测和结果行为，以便更好地桥接。

<!--screenshot {
"image_path": "bridge_settings_enabled_default.png",
"models": [
{
"script": "rack_straight.scad",
"scad_params": ["length=40"]
}
],
"camera_position": [0, 74, -137],
"colours": 32
}-->
<!--screenshot {
"image_path": "bridge_settings_enabled_enabled.png",
"models": [
{
"script": "stairwell.scad",
"scad_params": ["steps=4", "width=10", "height=20"]
}
],
"layer": 275,
"settings": {
"bridge_settings_enabled": true
},
"camera_position": [-12, 28, 63],
"colours": 64
}-->
![检测到桥接时，皮肤线将被定向为尽可能桥接间隙](../images/bridge_settings_enabled_default.png)
![启用桥接后，将使用不同的设定打印桥接线](../images/bridge_settings_enabled_enabled.png)

通常情况下，Cura会使用相当基本的桥接技术。Cura将检测具有多面支撑的皮肤悬垂区域。调整[调整这些皮肤线的方向](../top_bottom/skin_angles.md) ，以自动桥接这些区域。这确保了最大可能的悬垂区域在多个侧面上得到支撑，并提高了打印质量。

启用此设置后，您可以根据自己的要求更精确地调整该行为。可供调整：
* 打印速度
* 流量
* 密度（类似于填充密度，但具有皮肤线）
* 风扇速度
* 调整桥壁滑行

可以分别为桥接间隙的皮肤与壁调整这些设置。如果启用了[连桥有多层](bridge_enable_more_layers.md)，还可以分别调整桥接间隙上方的第二层和第三层。它还允许调整打印的哪些部分被视为桥接区域，方法是调整[连桥表面支撑阈值](bridge_skin_support_threshold.md)和[最小桥臂长度](bridge_wall_min_length.md)。

通过启用桥接设置，您可以更好地控制在打印中如何处理桥接。通过很好地调整桥接参数，可以显著提高悬垂的质量，并提高垂直方向的精度。唯一的缺点是，如果你不对打印机的连桥设置进行调整，打印可能会变得更糟。
