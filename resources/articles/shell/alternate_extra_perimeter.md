Alternate Extra Wall
====
This setting adds an extra wall every other layer. This way the infill gets wedged vertically between the walls, resulting in stronger prints.

For example, if you set the wall line count to two walls and enable alternate extra wall, it will print two walls on even numbered layers and three walls on odd numbered layers.

<!--screenshot {
"image_path": "alternate_extra_perimeter.gif",
"models": [
    {
        "script": "gear.scad",
        "transformation": ["scale(0.7)"]
    }
],
"camera_position": [0, 30, 123],
"settings": {
    "zig_zaggify_infill": true,
    "alternate_extra_perimeter": true
},
"layer": [15, 16, 17, 18],
"minimum_layer": [15, 16, 17, 18],
"colours": 32
}-->
![This image shows the walls affected when changing this setting.](../images/alternate_extra_perimeter.gif)