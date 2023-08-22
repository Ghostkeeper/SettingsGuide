启用熨平
====
熨平会引发打印机在顶层表面进行一次额外的扫略，以使它更加平滑。额外的扫略使用非常小的走线宽度，打印速度也非常慢。

<!--screenshot {
"image_path": "ironing_enabled_disabled.png",
"models": [
{
"script": "dial_brace.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 14, 83],
"settings": {
"layer_height": 0.2,
"ironing_enabled": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
{
"script": "dial_brace.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 14, 83],
"settings": {
"layer_height": 0.2,
"ironing_enabled": true
},
"colours": 64
}-->
![普通打印，顶部视图](../images/ironing_enabled_disabled.png)
![启用熨平后，注意顶层的细线。](../images/ironing_enabled_enabled.png)

熨平使用直线图案在顶部表面进行打印。两个主要好处是：
* 通过热喷嘴的多次经过，顶部表面再次融化。即“熨平”的由来。由于速度很慢且走线宽度很小，喷嘴会显著的加热表面。喷嘴的扁平部分将其“抚平”。
* 填补顶部表面的空隙熨平动作发生在与本层相同的高度。流量虽然不如完整层多，毕竟还是有一些的。理论上这些流量无处可去，但实际上它起到保持喷嘴压力的作用。每当喷嘴流经不平整的表面，喷嘴中的材料会流入缝隙。

相应的，熨平也有一些缺点：
* 显著增加打印时长
* 如果熨平图案中断了（因为不得不移动到不同的部分），会在先后两次熨平的部位之间留下可见的线条。这种情况有时可以通过改变[熨平图案](ironing_pattern.md)解决，比如换为同心图案。
* 倾斜的表面，或者有很多细节的顶部表面，也可能会被熨平，这会增加地貌效应。层之间的边界变得更加明显。可以通过开启[仅熨平最高层](ironing_only_highest_layer.md)改善。
