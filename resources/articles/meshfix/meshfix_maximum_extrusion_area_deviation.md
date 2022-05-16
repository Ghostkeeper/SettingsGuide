Maximum Extrusion Area Deviation
====
When printing lines with varying widths, it is common to have a line that should gradually get thinner towards one of its endpoints. This setting determines the step size at which these lines get thinner or wider, by controlling how close the lines must stay to the area they should ideally cover.

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
![Lower resolution when allowing high deviation](../images/meshfix_maximum_extrusion_area_deviation_high.png)
![Smooth line width when requiring low deviation](../images/meshfix_maximum_extrusion_area_deviation_low.png)

G-code commands can't instruct the printer to print a line with a variable width. It must print lines with a fixed width. Cura can break up a line into multiple segments with gradually changing width. However, this adds a lot of line segments to the print. The CPU in the printer may not be able to keep up with all of these instructions while printing. With this setting, the level of detail of variable-width line segments is chosen. A greater resolution (reduced deviation) results in more accurate lines in theory, but also increase the amount of instructions greatly.

While it looks nice in layer view if the width of a line changes gradually, this has virtually no effect on the actual print. Physical 3D printers don't adjust their flow rate accurately enough to see any improvement when increasing the resolution here. Under normal circumstances this setting should be high enough that it is never a limiting factor on the resolution of the g-code. That way, the chance of getting buffer underruns is minimised.