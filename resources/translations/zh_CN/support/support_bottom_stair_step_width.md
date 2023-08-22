支撑梯步阶最大宽度
====
如果[支撑放置](support_type.md)设置为"全部支撑"，则支撑面可以放置在模型上。但它不会完全遵循模型的轮廓。相反，支撑的底部会指定楼梯步阶样式。这样，支撑仅在少数位置与模型建立连接。

此设置确定这些阶梯的最大宽度。通常，台阶的宽度与模型曲面的宽度相同，并具有给定的[支撑梯步阶高度](support_bottom_stair_step_height.md)值。但是，如果该宽度太宽，则宽度将被限制为"支撑梯步阶最大宽度"。然后，在步阶的其余部分中，它将跟随模型的曲面。

<!--screenshot {
"image_path": "support_bottom_stair_step_width.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"settings": {
"support_enable": true,
"support_bottom_stair_step_height": 1,
"support_bottom_stair_step_width": 0.7
},
"colours": 64
}-->
![楼梯台阶宽度受限，导致支撑跟随模型](../images/support_bottom_stair_step_width.png)

该设置通常应设置为材料可桥接的最大距离，而不影响其上支撑线的稳定性。降低该设置会使支撑更频繁地跟随模型，从而使支撑更稳定。增加该设置会使支撑更经常地遵循"支撑梯步阶高度"的设置值，从而使支撑更容易从模型中删除。
