Infill Before Walls
====
This affects the order in which things are printed. With this setting enabled, the infill of a part will be printed before the walls of that part on that layer are printed.

<!--screenshot {
"image_path": "infill_before_walls_disabled.gif",
"models": [
    {
        "script": "cube.scad",
        "transformation": ["scale(0.25)"]
    }
],
"camera_position": [0, 0, 100],
"settings": {
    "top_layers": 0,
    "infill_before_walls": false
},
"layer": 162,
"line": [0, 1, 2, 3, 4, 6, 7, 8, 9, 12, 16, 20, 24, 28, 32],
"colours": 32,
"delay": 250
}-->
<!--screenshot {
"image_path": "infill_before_walls_enabled.gif",
"models": [
    {
        "script": "cube.scad",
        "transformation": ["scale(0.25)"]
    }
],
"camera_position": [0, 0, 100],
"settings": {
    "top_layers": 0,
    "infill_before_walls": true
},
"layer": 162,
"line": [0, 1, 5, 9, 13, 17, 21, 26, 27, 28, 29, 31, 32, 33, 34],
"colours": 32,
"delay": 250
}-->
![Setting is disabled, so walls are printed first](../images/infill_before_walls_disabled.gif)
![Setting is enabled, so infill is printed first](../images/infill_before_walls_enabled.gif)

This setting is a trade-off between accuracy and strength:
* If the walls are printed before the infill, the walls could have nothing to attach to, causing them to sag more. However, the walls will have solidified first and won't be pushed away by the infill, which prevents the infill from shining through the walls.
* If the infill is printed before the walls, the walls will get pushed away where infill is attached to the walls, which makes the walls less accurate and can cause the infill to shine through the surface, creating a pattern visible on the outside. However the infill will hold the walls in place better while they are printed.