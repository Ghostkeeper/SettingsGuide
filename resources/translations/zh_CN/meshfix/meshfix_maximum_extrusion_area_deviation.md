最大挤出面积偏移量
====
当打印具有不同宽度的线条时，通常会有一条线条应朝着其端点之一逐渐变细。此设置通过控制线条必须与其理想覆盖区域保持的距离来确定这些线条变细或变宽的步长。

<!--screenshot {
"image_path": "meshfix_maximum_extrusion_area_deviation_high.png",
"models": [{"script": "twisted_triangular_hole.scad"}],
"camera_position": [0, 0, 60],
"settings": {
	"meshfix_maximum_resolution": 0.5,
	"meshfix_maximum_extrusion_area_deviation": 2000
},
"colour_scheme": "line_width",
"colours": 128
}-->
<!--screenshot {
"image_path": "meshfix_maximum_extrusion_area_deviation_low.png",
"models": [{"script": "twisted_triangular_hole.scad"}],
"camera_position": [0, 0, 60],
"settings": {
	"meshfix_maximum_resolution": 0.05,
	"meshfix_maximum_extrusion_area_deviation": 20
},
"colour_scheme": "line_width",
"colours": 128
}-->
![允许高偏差时的分辨率较低](../images/meshfix_maximum_extrusion_area_deviation_high.png)
![要求低偏差时的平滑走线宽度](../images/meshfix_maximum_extrusion_area_deviation_low.png)

G代码命令不能指示打印机打印宽度可变的线。它必须以固定宽度打印。Cura可以将一条线分解为多个宽度逐渐变化的线段。但是，这会在打印中添加大量线段。打印时，打印机中的CPU可能无法跟上所有这些指令。使用此设置，可以选择可变宽度线段的细节级别。更高的分辨率（减小偏差）在理论上导致更精确的线，但也大大增加了指令量。

虽然它看起来不错，在层视图中，如果一条线的宽度逐渐变化，这几乎没有影响实际打印。物理3D打印机在提高分辨率时，无法足够精确地调整其流量速率，因此无法看到任何改进。在正常情况下，该设置应足够高，以使其不会成为g代码分辨率的限制因素。这样，得到缓冲器欠载的可能性被最小化。
