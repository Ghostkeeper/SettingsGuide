Maximum Model Angle
====
With this setting, the overhang angle is configured (in degrees) that is produced to [make the overhang printable](conical_overhang_enabled.md). Increasing this angle allows for greater overhang, causing Cura to modify the model less. Reducing this angle gives the object barely any overhang at all any more.

<!--screenshot {
"image_path": "conical_overhang_enabled_enabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
    "conical_overhang_enabled": true,
    "conical_overhang_angle": 50
},
"colours": 8
}-->
<!--screenshot {
"image_path": "conical_overhang_angle_20.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
    "conical_overhang_enabled": true,
    "conical_overhang_angle": 20
},
"colours": 8
}-->
![A maximum model angle of 50°](../images/conical_overhang_enabled_enabled.png)
![A maximum model angle of 20°](../images/conical_overhang_angle_20.png)

An angle of 90° will leave the model as it was with all of its overhang. The model will not be altered. An angle of 0° will make all slopes completely vertical.

Reducing this angle reduces the overhang in the model. This allows the model to print better. It will not sag as much, and therefore the surface on the bottom sides will be smoother. However it will also make the printed object less truthful to the original model. It will also take slightly more time and material to print it.

The angle can also be negative. This makes the entire print conical with a wide base. This can produce interesting effects, but has no real practical use.