Infill Line Width
====
The width of every line of infill being drawn. The width of a line can be different from the nozzle size simply by extruding more or less material than needed. If more material is extruded, the plastic will flow towards the sides, making the line thicker. If less material is extruded, the surface tension of the material tends to pull the material towards the centre line of the nozzle's path.

<!--screenshot {
"image_path": "infill_line_width.png",
"models": [{"script": "material_calibration.scad"}],
"camera_position": [35, 92, 122],
"settings": {"infill_line_width": 1},
"layer": 111,
"colours": 64
}-->
![The infill lines are significantly wider than the rest](../images/infill_line_width.png)

Making the infill lines wider can make your print stronger and reduce printing time as well. However, increasing it too much can cause great extrusion fluctuations. This will cause underextrusion when printing the infill and overextrusion when printing whatever comes after infill, because the flow through the nozzle cannot adjust fast enough.

**The actual infill lines may come out wider than what this setting says, if you've adjusted the [Infill Layer Thickness](../infill/infill_sparse_thickness.md) setting.**