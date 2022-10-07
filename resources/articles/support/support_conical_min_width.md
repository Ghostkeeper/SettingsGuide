Conical Support Minimum Width
====
If conical support is enabled and set to shrink the support structure, this setting determines the minimum width that the conical support will shrink the support to. The support will not get any thinner unless the overhang area that needs supporting is already thinner.

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_min_width_20.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 30,
    "support_conical_min_width": 15
},
"colours": 64
}-->
![A minimum width of 5mm](../images/support_conical_enabled.png)
![A minimum width of 15mm](../images/support_conical_min_width_20.png)

If a large volume of support is resting on a tiny pillar of support, this support will be very prone to falling over. Increasing the minimum width increases the width of the base pillar of support that the cone will gravitate to. This increases the reliability of the print, but will cost extra material. All in all, the conical support will be less effective at reducing print time.