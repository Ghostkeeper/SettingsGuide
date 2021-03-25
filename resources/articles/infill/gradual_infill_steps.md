Gradual Infill Steps
====
Gradual infill reduces the amount of infill used, by reducing the infill density in the lower layers. This saves on printing time and material, while not reducing surface quality much. The primary purpose of infill when printing for visual quality is to support the top surface. This feature focuses the infill to that purpose only.

This setting indicates in how many steps the infill density gets reduced. At every step, the infill density is halved. For example, starting with an infill percentage of 20% and two gradual infill steps, the infill density of the lower parts will be 10% and 5%, respectively.

<!--screenshot {
"image_path": "gradual_infill_disabled.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
    "wall_line_count": 0,
    "bottom_layers": 0,
    "gradual_infill_steps": 0
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
![Normal infill](../images/gradual_infill_disabled.png)
![3 gradual infill steps](../images/gradual_infill_step_height_large.png)

**The "Gradual Infill" checkmark in Recommended Mode sets this setting to 5 steps and increases infill density to 90%. This causes a very high density at the top (90%) and a very low density at the bottom of your print (2.8%).**