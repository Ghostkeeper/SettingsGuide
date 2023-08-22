渐进支撑填充步阶
====
渐进支撑通过降低下层中的支撑密度来减少填充量。这节省了打印时间和材料，同时悬垂质量不会降低很多。支撑的主要目的是支撑悬垂区域。此功能将支撑仅聚焦在该用途上。

此设置用来指定支撑密度减少的步长。在每一步中，支撑密度减半。例如，以20%的密度比例和2个支撑步阶开始，下面的支撑密度将分别为10%和5%。

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
![支撑分3步降低到较低的密度](../images/gradual_support_infill_step_height_1mm.png)

增加步阶数会导致越来越多的密度减半，从而使支撑的密度更低。这节省了大量的材料和打印时间，但会使支撑较弱。

有些支撑物会浮在半空中。然而，在实践中，对于大多数支撑图案，这将快速地自我修复，因为即使在弱化的下层上，层也可以适当地建立。[渐进支撑填充步阶高度](gradual_support_infill_step_height.md)的目的是在下一个步阶支撑堆积到（已打印的）顶部之前，为层提供足够的时间进行自我修复。

此设置最好至少与一个[支撑强行数](support_wall_count.md)结合使用。这使得支撑线有东西可以抓，而不是悬在半空中。
