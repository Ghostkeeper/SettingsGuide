填充层厚度
====
由于填充的层高度对于视觉品质并不重要，因此您可以使用较厚填充层来减少打印时间。此设置可使填充层组合在一起，只要有多个填充层位于彼此的正上方即可。然后，在某些层上不会打印任何填充，但在层间结合的最高层，将挤出更多材料进行补偿。

在分层视图中，看起来好像填充线变得更宽。在实际打印时，填充线将进一步沉降，而不是水平展开。

<!--screenshot {
"image_path": "infill_sparse_thickness.png",
"models": [{"script": "cooking_utensil_hook.scad"}],
"camera_position": [6, 51, 27],
"camera_lookat": [0, 0, 7],
"settings": {
"layer_height": 0.2,
"wall_line_count": 0,
"infill_pattern": "zigzag",
"infill_sparse_thickness": 0.6
},
"layer": 19,
"colours": 64
}-->
![填充层厚度设置为层高的3倍]（../images/infill_sparse_thickness.png）

填充层厚度必须是普通层高的倍数。如果不是，将四舍五入至最接近的层高。

* 请注意不要将此值增加太多。当切换到填充和从填充切换时，通过喷嘴的流量需要显著地加速和减速。这存在一些延迟，因此在填充开始时挤出的量太少，而在填充结束后挤出的量太多。
*在中间层中，在周围的层中没有填充的位置仍将使用较低的层厚度打印填充。这可能会导致在倾斜的壁旁边打印出小的填充线。
