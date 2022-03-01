Gradual Support Infill Step Height
====
When using gradual support, the density of the support gets periodically reduced from top to bottom in several steps. At each step, the support density is halved. This setting indicates the height of these steps, the distance between two places where the support density is halved.

<!--screenshot {
"image_path": "gradual_support_infill_step_height_1mm.png",
"models": [
    {
        "script": "stair.scad",
        "transformation": ["rotateY(-90)", "scaleZ(0.5)"]
    }
],
"camera_position": [49, 91, -38],
"settings": {
    "support_enable": true,
    "support_pattern": "grid",
    "support_wall_count": 0,
    "support_infill_rate": 50,
    "gradual_support_infill_steps": 3,
    "gradual_support_infill_step_height": 1
},
"colours": 64
}-->
<!--screenshot {
"image_path": "gradual_support_infill_step_height_3mm.png",
"models": [
    {
        "script": "stair.scad",
        "transformation": ["rotateY(-90)", "scaleZ(0.5)"]
    }
],
"camera_position": [49, 91, -38],
"settings": {
    "support_enable": true,
    "support_pattern": "grid",
    "support_wall_count": 0,
    "support_infill_rate": 50,
    "gradual_support_infill_steps": 3,
    "gradual_support_infill_step_height": 3
},
"colours": 64
}-->
![1mm step height](../images/gradual_support_infill_step_height_1mm.png)
![3mm step height](../images/gradual_support_infill_step_height_3mm.png)

Gradual support by its nature will suspend some of the support in mid-air. However this normally repairs itself automatically. The first layer of support will hang in mid-air and only attach to the sides of the support properly. The layers on top of it can rests on the previous layer a bit on the ends, but will sag in the middle. This gradually gets better, layer by layer. If the gradual support step height is large enough, the support is properly sturdy by the time the next density step occurs.

Reduce the Gradual Support Infill Step Height in order to quickly descend to a low support density. This saves on printing time and material use. Increase the Gradual Support Infill Step Height if the support will not get enough room to repair itself by the time the next step in support density occurs. Increasing the value of this setting makes the print more reliable.