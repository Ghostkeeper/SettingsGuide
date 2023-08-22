启用滑行
====
如果启用此设置，则喷嘴将在闭合壁轮廓之前稍微停止挤出材料。它的思路是，喷嘴室可以在线的最后一点上清空自己，这减少了喷嘴的压力，并允许它被轮廓的开始所阻挡。然后，在轮廓开始处产生较少的接缝，并减少后续行空驶中的拉丝。

<!--screenshot {
"image_path": "coasting_enable.png",
"models": [{"script": "phone_holder.scad"}],
"camera_position": [0, -215, 117],
"minimum_layer": 1,
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
"coasting_enable": true,
"coasting_volume": 0.06,
"z_seam_position": "backright"
},
"colours": 32
}-->
![在图层视图中，如果启用了滑行，则可以很容易地看到接缝，因为在那里会有一个空驶](../images/coasting_enable.png)

启用滑行的目的是降低壁中接缝的可见性。如果您通常有粗大的接缝，启用该选项可以减少这种影响。它基本上与[外壁擦嘴长度](../shell/wall_0_wipe_dist.md)的作用相反，因此最好在尝试滑行之前先尝试减少擦拭。

理论上，滑行总是产生挤出不足。在实际打印中是否可见取决于具体情况。对于使用直接驱动的打印机，滑行在某种程度上更为有效。如果您的打印机有直接驱动器，则您需要将[滑行体积](coasting_volume.md) 的值减小到比使用Bowden管或柔性驱动轴时更低的值，因为那里流量速率的反应会快得多。使用Bowden型送料系统，也将更难控制滑行量以有效降低接缝的可见度。
