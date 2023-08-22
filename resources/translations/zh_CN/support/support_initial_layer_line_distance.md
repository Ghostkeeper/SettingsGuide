起始层支撑走线距离
====
起始层支撑图案的密度可以与支撑其余部分的密度分开调节。此设置配置两条相邻线之间的距离，其中支撑位于构造板上。

<!--screenshot {
"image_path": "support_initial_layer_line_distance.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 64, 125],
"settings": {
"support_enable": true,
"support_initial_layer_line_distance": 1.333
},
"layer": 160,
"colours": 64
}-->
![起始层支撑密度是其余支撑的两倍](../images/support_initial_layer_line_distance.png)

此设置有助于提高支撑物和构造板之间的粘附力。使起始层支撑图案更致密将增加支撑和构造板之间的接触面积，使其更好地粘附。随后的层可以更好地粘附在材料上。

由于该设置仅影响第一层，因此不会显著影响支撑的强度，也不会显著影响时间和材料成本。同时也不会影响悬垂的质量。要调整悬垂附近支撑的密度，请查看[支撑顶板走线距离](support_roof_line_distance.md)设置。

此设置最好设置为支撑主体的直线距离的倍数。这样，支撑线将与第一层上的线匹配，从而使它们停留在第一层上，而不是漂浮在空中。
