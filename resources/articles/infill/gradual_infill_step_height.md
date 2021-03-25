Gradual Infill Step Height
====
When using gradual infill, the density of the infill will be reduced from top to bottom in several steps. At each step, the infill density is halved. This setting indicates the height of these steps, the distance between two places where infill is halved.

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
![Gradual Infill Step Height of 1.5mm](../images/gradual_infill_step_height_small.png)
![Gradual Infill Step Height of 5mm](../images/gradual_infill_step_height_large.png)

Gradual Infill by its nature will suspend some of the infill in mid-air. However this normally repairs itself automatically. The first layer of infill will hang in mid-air and only attach to the sides of the print properly. The layers put on top of it can rest on the previous layer a bit on the ends, but will still sag in the middle. This gradually gets better, layer by layer.

* Reduce the Gradual Infill Step Size in order to quickly descend to a low infill density. This saves on printing time and material use.
* Increase the Gradual Infill Step Size if the infill will not get enough room to repair itself by the time the next step in infill density occurs. Increasing the value of this setting makes the print more reliable.