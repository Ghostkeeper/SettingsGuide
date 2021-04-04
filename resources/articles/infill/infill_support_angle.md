Infill Overhang Angle
====
When using infill support, this setting determines the minimum overhang angle of the surface that needs to get supported. This is similar to the [Overhang Angle](../support/support_angle.md) setting for ordinary support.

<!--screenshot {
"image_path": "infill_support_angle_low.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_support_enabled": true,
    "infill_support_angle": 40
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_support_angle_high.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_support_enabled": true,
    "infill_support_angle": 60
},
"colours": 64
}-->
![A low angle results in more support](../images/infill_support_angle_low.png)
![A high angle results in less support](../images/infill_support_angle_high.png)

Increasing this angle will cause the infill to support less of the top surface. This saves on printing time and material, but will cause the top skin to sag a bit more.
* A value of 0° will act like normal infill. It supports everything.
* A value of 90° will remove all infill material.