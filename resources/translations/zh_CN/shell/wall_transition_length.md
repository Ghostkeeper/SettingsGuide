壁过渡长度
====
在较薄的部分，不是所有的壁都能匹配形状内部。如果某处比其他处更薄，Cura需要在这里使用不同数量的壁，即过渡区。此设置控制过渡区的宽度，在此宽度内添加或移除一个壁。

<!--screenshot {
"image_path": "wall_transition_length_0_2.png",
"models": [{"script": "wedge.scad"}],
"camera_position": [-7, 0, 75],
"settings": {"wall_transition_length": 0.2},
"colours": 64
}-->
<!--screenshot {
"image_path": "wall_transition_length_1_5.png",
"models": [{"script": "wedge.scad"}],
"camera_position": [-7, 0, 75],
"settings": {"wall_transition_length": 1.5},
"colours": 64
}-->
![很短的过渡区](../images/wall_transition_length_0_2.png)
![长一些的过渡区](../images/wall_transition_length_1_5.png)

在不同数量壁之间的过渡区总有一些小问题。当中心的一条线结束，周围的两个壁需要填补缺口时，这一点最为明显。空间不会立即被填满，而会留下一个缺口，这会在零件顶部和底部产生小孔。当两个壁合为一体时，情况正相反：两个壁会重叠一小段时间，直到完成合并。重叠的部分挤出过度，影响了尺寸的精确性，外壁尤其明显。这个问题通过设置尽可能短的过度区来纠正。

然而，较短的过渡区内，喷嘴为了快速填充间隙，会发生一些非常急剧的转弯，结果就是更多的振纹，尤其在外壁打印时。较长的过渡区会降低喷嘴中的加速度， 甚至将加速度降低至 [打印抖动速度](../speed/jerk_print.md)限制以下。

将过渡区设置为线宽的一到两倍是一个合理的开始，框架较弱或者打印头较重的打印机可能需要调高一点儿。加速很快又没有振纹的打印机则可以通过较小的过渡区改善视觉质量。

** 此设置不仅适用于普通壁，还适用于额外皮肤壁，支撑壁，填充壁与同心填充图案。**
