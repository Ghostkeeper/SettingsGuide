桥壁滑行
====
与壁线桥接时，在打印桥接之前，进料会暂停片刻。在此期间，允许喷嘴室内的剩余材料流出，以降低喷嘴室内的压力。此技术称为[滑行](coasting_enable.md)。通过此设置，可以控制滑行量。从本质上讲，这控制了材料在桥梁前方停止流动的距离。

完成桥接后，未挤出的材料将被擦去。材料挤出的总量将保持不变。这将恢复喷嘴上的压力，从而防止挤出不足。

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
"bridge_settings_enabled": true,
"bridge_skin_density": 100,
"bridge_skin_material_flow": 100,
"bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![桥的一侧没有突出，另一侧有额外的突出](../images/bridge_skin_density_100.png)

此设置的单位并不直观。材料在桥前停止流动的距离取决于多种因素：
* 目前为止的壁长度，直到桥边。壁越长，它就越能滑行。
* 正常壁期间流出喷嘴的流速，取决于这些壁的 [速度](../speed/speed_wall.md), [走线宽度](../resolution/wall_line_width.md), [流量](../material/wall_material_flow.md) 和 [层高](../resolution/layer_height.md)。正常壁中的流量速率越大，滑行距离越长。
* 桥接壁期间流出喷嘴的流量，取决于这些壁的 [速度](bridge_wall_speed.md) 和 [流量](bridge_wall_material_flow.md) 。桥壁中的流量速率越大，滑行距离就越*短*。

此设置是最终长度的倍数。

这种滑行的目的是降低喷嘴腔内的压力。这是必要的，因为一旦反压消失，喷嘴室中的任何剩余压力就会立刻使材料固化之前向下喷射相当长的距离。这种向下喷射的材料导致下垂。基本上，悬垂线被仍在喷嘴内的其余材料向下推。如果喷嘴室内的压力减小，则该力也将减小，并且将存在较少的下垂。

增加滑行量将在需要打印桥时降低喷嘴室内的压力，这将减少下垂量。打印会更准确。但是，过度增加滑行量将导致在打印桥之前出现一段挤出不足的时间。由于这种挤出不足是在壁上，因此在打印件的侧面上非常明显。
