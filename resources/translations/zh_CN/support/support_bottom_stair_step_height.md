支撑梯步阶高度
====
如果[支撑放置](support_type.md)设置为"全部支撑"，则支撑面可以放置在模型上。但它不会完全遵循模型的轮廓。相反，支撑的底部会指定楼梯步阶样式。这样，支撑仅在少数位置与模型建立连接。

此设置决定了这些台阶的高度。

<!--screenshot {
"image_path": "support_bottom_stair_step_height.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"settings": {
"support_enable": true,
"support_bottom_stair_step_height": 1
},
"colours": 64
}-->
![在支撑底部形成的楼梯步阶](../images/support_bottom_stair_step_height.png)

楼梯步阶高度按与模型表面的距离计算。这意味着，如果在[支撑底部距离](support_bottom_distance.md)中设置了垂直距离，则会从高度中减去该垂直距离，模型与支撑之间的连接将更大。同样，[启用支撑底板](support_bottom_enable.md)也会导致楼梯步阶的效果降低。

[支撑梯步阶最大宽度](support_bottom_stair_step_width.md)设定可限制楼梯的宽度。如果模型的表面很浅，一个小的台阶高度会导致一个巨大的台阶宽度，则支撑将在剩余的台阶高度上跟随模型的表面。

减小此设置将使支撑底部更平滑。这增加了支撑件和模型之间的粘附力，使得更难移除支撑件，但也使得支撑件更稳定。
