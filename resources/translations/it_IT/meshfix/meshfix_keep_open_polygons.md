Keep Disconnected Faces
====
Cura needs to know where the inside of your model is in order to fill the volume with material. If the model is not properly watertight, this is ambiguous. Normally Cura will not print parts that are not properly closed.

With this setting enabled, layers where the perimeter is not properly closed will be kept. The perimeter will be closed artificially with a straight line. This may fix some models that have small gaps in their surfaces. It may also misinterpret what the inside is of your model though.

<!--screenshot {
"image_path": "meshfix_keep_open_polygons_shell.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"layer": -1
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_disabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
    "meshfix_keep_open_polygons": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_enabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
    "meshfix_keep_open_polygons": true
},
"colours": 64
}-->
![This cube is missing a corner](../images/meshfix_keep_open_polygons_shell.png)
![Normally the layers that are not closed will not be printed](../images/meshfix_keep_open_polygons_disabled.png)
![With this setting enabled, the shape is closed artificially](../images/meshfix_keep_open_polygons_enabled.png)

X-ray view will show gaps that can be closed with this setting in red.