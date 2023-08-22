支撑结合部距离
====
薄的支撑件通常是不希望出现的。它们很容易翻倒，这会破坏打印。当多个支撑件彼此相邻时，它们可以连接在一起，形成一个更坚固的支撑件。

<!--screenshot {
"image_path": "support_join_distance_low.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 150, 75],
"settings": {
"support_enable": true,
"support_interface_enable": true,
"support_join_distance": 0.1
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_join_distance_high.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 150, 75],
"settings": {
"support_enable": true,
"support_interface_enable": true,
"support_join_distance": 2
},
"colours": 64
}-->
![两个支撑相互靠近](../images/support_join_distance_low.png)
![设置充足的结合距离使他们合并在一起](../images/support_join_distance_high.png)

将支撑件连接在一起使得支撑件更加坚固和可靠。根据图案的不同，它还可以缩短打印时间。许多图案需要在整个周边或周边的一部分周围印刷额外的壁，将两个支撑件连接在一起可以减少周长

将此设置增加太多可能会导致距离很远的支撑件连接在一起。这会增加打印时间和材料使用量。
