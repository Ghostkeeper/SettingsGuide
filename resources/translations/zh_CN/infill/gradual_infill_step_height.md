渐进填充步阶高度
====
当使用渐进式填充时，填充的密度将从顶部到底部分几个步阶减小。在每一步中，填充密度减半。此设置指定这些步阶的高度，即填充减半的两个位置之间的距离。

<!--screenshot {
"image_path": "gradual_infill_step_height_small.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
"wall_line_count": 0,
"bottom_layers": 0,
"gradual_infill_steps": 3,
"gradual_infill_step_height": 1.5
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
![填充步阶高度为1.5mm](../images/gradual_infill_step_height_small.png)
![渐进填充步阶高度为5mm](../images/gradual_infill_step_height_large.png)

渐进填充的性质将使一些填充悬浮在半空中。但是，这通常会自动修复。第一层填充物将悬挂在半空中，仅正确附着在印刷品的两侧。放在它上面的层可以在两端稍微停留在前一层上，但仍然会在中间下垂。这种情况一层一层地逐渐好转。

* 减小渐进填充步阶以快速降低到较低的填充密度。这节省了打印时间和材料的使用。
* 如果当前的填充密度会导致下一个步阶没有足够的空间来修复自身，请增加渐进填充步阶。增加该设置的数值可使打印更可靠。
