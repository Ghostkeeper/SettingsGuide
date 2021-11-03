Lightning Infill Overhang Angle
====
Lightning infill will only support the top side of the model from the inside where it overhangs. This setting determines the angle of overhang that gets supported by lightning inside from the inside of the model.

<!--screenshot {
"image_path": "lightning_infill_support_angle_30.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "lightning_infill_overhang_angle_70.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 30,
    "lightning_infill_overhang_angle": 70
},
"colours": 64
}-->
![Overhang of up to 30° is left unsupported](../images/lightning_infill_support_angle_30.png)
![Up to 70° is unsupported, leaving only the very top of the sphere supported](../images/lightning_infill_overhang_angle_70.png)

Increasing this angle will reduce the amount of infill generated. Less of the top surface will get supported, if it's not a very steep overhang. This saves time and material, but may also cause the top surface to sag in places. The result could be [pillowing](../troubleshooting/pillowing.md) or generally a rougher surface.

Contrary to the parent setting [Lightning Infill Support Angle](lightning_infill_support_angle.md), this setting doesn't influence the overhang in the infill pattern itself.