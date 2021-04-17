Prime Tower Line Width
====
This setting determines the width of the lines with which the prime tower is drawn.

<!--screenshot {
"image_path": "prime_tower_line_width.png",
"models": [
    {"script": "cube.scad"},
    {
        "script": "cube.scad",
        "object_settings": {"extruder_nr": 1},
        "transformation": ["translateX(40)"]
    }
],
"camera_position": [475, -419, 131],
"camera_lookat": [475, -465, 20],
"settings": {
    "prime_tower_enable": true,
    "[1]prime_tower_line_width": 0.8
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![The blue material has a larger line width than the yellow material](../images/prime_tower_line_width.png)

Choosing a thicker line width causes the prime tower to sometimes print faster. If the volume extruded by one contour is sufficiently big, increasing the line width makes another loop unnecessary. However increasing the line width too much can make the prime tower weaker because not enough material can be extruded fast enough.