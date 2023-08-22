Z间隙内无表层
====
如果您的模型有一个小于顶/底层厚度的水平裂缝，该设置可以使其在上下方免于填充皮肤。这样可以节省切片和打印时间，但可能会让填充暴露在空气中。

<!--screenshot {
"image_path": "skin_no_small_gaps_heuristic_disabled.png",
"models": [
{
"script": "small_z_gap.scad",
"scad_params": ["gap_size=0.06"]
}
],
"camera_position": [-21, -62, 25],
"settings": {
"wall_line_count": 0,
"skin_no_small_gaps_heuristic": false
},
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_no_small_gaps_heuristic_enabled.png",
"models": [
{
"script": "small_z_gap.scad",
"scad_params": ["gap_size=0.06"]
}
],
"camera_position": [-21, -62, 25],
"settings": {
"wall_line_count": 0,
"skin_no_small_gaps_heuristic": true
},
"colours": 32
}-->
![通常水平的裂缝之间会生成皮肤](../images/skin_no_small_gaps_heuristic_disabled.png)
![启用本设置后，无法真正的闭合皮肤。](../images/skin_no_small_gaps_heuristic_enabled.png)

该设置的主要目的是节省切片时间。它有效降低了Cura在必须放置皮肤处的采样精度。取决于模型的形状，可节约5%到30%的切片时间。如果有小间隙也可以节约打印时间，因为皮肤会被填充替代。

如果模型没有小于皮肤厚度的水平裂缝，则只有减少切片时间的效果。

如果有这种裂缝，将会暴露其中的填充。然而当缝隙足够小时，悬垂导致的墙壁下降会使缝隙无法被看到。
