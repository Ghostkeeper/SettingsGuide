渐进填充步阶
====
渐进填充通过降低下层中的填充密度来减少填充量。这节省了打印时间和材料，同时不会降低表面质量。为了视觉品质而打印时，填充的主要目的是支撑顶层皮肤。此功能将填充仅聚焦在该用途上。

此设置用来指定填充密度减少的步长。在每一步中，填充密度减半。例如，以20%的填充比例和两个渐进填充步阶开始，下面的填充密度将分别为10%和5%。

<!--screenshot {
"image_path": "gradual_infill_disabled.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
"wall_line_count": 0,
"bottom_layers": 0,
"gradual_infill_steps": 0
},
"colours": 16
}-->
<!--screenshot {
"image_path": "gradual_infill_step_height_large.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
"wall_line_count": 0,
"bottom_layers": 0,
"gradual_infill_steps": 3,
"gradual_infill_step_height": 5
},
"colours": 16
}-->
![普通填充](../images/gradual_infill_disabled.png)
![3个渐进填充步阶](../images/gradual_infill_step_height_large.png)

**在推荐模式中选中"渐进填充"复选框，设置为5步，并将填充密度增加到90%。这会使打印件获得一个密度非常高（90%）的顶部和一个密度非常低（2.8%）的底部。**
