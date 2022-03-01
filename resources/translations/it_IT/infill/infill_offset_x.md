Infill X Offset
====
Normally the infill patterns are centred on the 3D model's centre. This setting, together with the [Infill Y Offset](infill_offset_y.md) allows shifting the centre of the pattern. This setting adjusts the X coordinate of the centre.

<!--screenshot {
"image_path": "infill_offset_xy_0.png",
"models": [
    {
        "script": "hexagonal_prism.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 90],
"settings": {
    "top_layers": 0,
    "infill_pattern": "triangles",
    "infill_offset_x": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_offset_x_2.png",
"models": [
    {
        "script": "hexagonal_prism.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 90],
"settings": {
    "top_layers": 0,
    "infill_pattern": "triangles",
    "infill_offset_x": 2
},
"colours": 64
}-->
![Infill is centred](../images/infill_offset_xy_0.png)
![Shifted 2mm to the right](../images/infill_offset_x_2.png)

When printing with low infill density, you can use this to position the infill very precisely such that the individual infill lines are positioned where the strength is most needed.