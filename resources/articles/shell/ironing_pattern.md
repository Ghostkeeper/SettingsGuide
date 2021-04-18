Ironing Pattern
====
Ironing covers the top surface with a path pattern. This setting determines which pattern is used to iron the top surface.

The goal of the pattern is to create a smooth, continuous surface. If there is an interruption in the pattern, this will create a visible border on the top surface. There are two patterns available.

Zigzag
----
<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true
},
"colours": 64
}-->
![Zigzag ironing pattern](../images/ironing_enabled_enabled.png)

This will make the nozzle go back and forth over the surface. It works fine and reliably for most surfaces, but will cause somewhat more borders than necessary.

Concentric
----
<!--screenshot {
"image_path": "ironing_pattern.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true,
    "ironing_pattern": "concentric"
},
"colours": 64
}-->
![Concentric ironing pattern](../images/ironing_pattern.png)

This will cause the nozzle to make circles from inside to outside. This will reduce the borders to a minimum, but if the concentric rings become very small in the centre, the material will degrade due to the nozzle lingering too long around the same spot. This leaves a visible spot on the surface. As a result, this works best for surfaces that are long and thin rather than surfaces that are equally wide as they are tall.