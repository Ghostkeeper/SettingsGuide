填充走线方向
====
填充走线通常尽可能指向45度角。在这个角度下，当使用具有XY坐标的龙门架打印机时，X轴和Y轴电机一起工作可使打印头获得最大加速度。

使用此设置，您可以调整这个角度。您可以高度定制化，让特定型号打印机实现更大强度；或是让特定机架系统（如三角洲结构）实现更大的加速度。

<!--screenshot {
"image_path": "infill_pattern_lines.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "lines"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "infill_angles_0_30.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "lines",
"infill_angles": [0, 30]
},
"colours": 32
}-->
![使用默认45度和135度填充线](../images/infill_pattern_lines.png)
![使用0度和30度的自定义角度填充线](../images/infill_angles_0_30.png)

此设置的值需要是一个逗号分隔的角度列表，并在其周围加上括号。角度为0度将产生一条与Y轴平行的直线。角度列表将在各层上交替显示。
* 最终成品在填充线的方向上强度最高。如果需要打印件在水平方向上承载特定的力，则让填充线的指向环绕该方向是有益的。
* 将列表设置为空以使用默认值。
* 默认值取决于填充图案：
* 对于“交叉”和“交叉3D”填充图案，预设为[22]。这会将尽可能多的填充线定向为靠近对角线。
* 对于“直线”和“锯齿状”填充图案，预设为[45，135]。这导致填充线逐层交替的定向在两个对角线之间。
* 所有其他图案使用默认值[45]。这会将尽可能多的填充线定向为靠近对角线。
