渐进支撑填充步阶高度
====
当使用渐进式填充时，填充的密度将从顶部到底部分几个步阶减小。在每一步中，支撑密度减半。此设置指定这些步阶的高度，即支撑密度减半的两个位置之间的距离。

<!--screenshot {
"image_path": "gradual_support_infill_step_height_1mm.png",
"models": [
{
"script": "stair.scad",
"transformation": ["rotateY(-90)", "scaleZ(0.5)"]
}
],
"camera_position": [49, 91, -38],
"settings": {
"support_enable": true,
"support_pattern": "grid",
"support_wall_count": 0,
"support_infill_rate": 50,
"gradual_support_infill_steps": 3,
"gradual_support_infill_step_height": 1
},
"colours": 64
}-->
<!--screenshot {
"image_path": "gradual_support_infill_step_height_3mm.png",
"models": [
{
"script": "stair.scad",
"transformation": ["rotateY(-90)", "scaleZ(0.5)"]
}
],
"camera_position": [49, 91, -38],
"settings": {
"support_enable": true,
"support_pattern": "grid",
"support_wall_count": 0,
"support_infill_rate": 50,
"gradual_support_infill_steps": 3,
"gradual_support_infill_step_height": 3
},
"colours": 64
}-->
![步阶高度1mm](../images/gradual_support_infill_step_height_1mm.png)
![步阶高度3mm](../images/gradual_support_infill_step_height_3mm.png)

渐进支撑的性质将使一些支撑悬浮在半空中。但是，这通常会自动修复。第一层支撑将悬挂在半空中，仅正确附着在印刷品的两侧。放在它上面的层可以在两端稍微停留在前一层上，但会在中间下垂。这种情况一层一层地逐渐好转。如果支撑步阶的高度足够大，则在下一密度台阶发生时，支撑是适当坚固的。

减小渐进支撑填充步阶高度以快速降低到较低的支撑密度。这节省了打印时间和材料的使用。如果当前的支撑密度会导致下一个步阶没有足够的空间来修复自身，请增加渐进支撑填充步阶高度。增加该设置的数值可使打印更可靠。
