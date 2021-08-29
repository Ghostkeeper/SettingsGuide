Monotonic Top/Bottom Order
====
Normally, Cura orders top/bottom lines such that the travel distance between them is small. If this setting is enabled, it will order the top/bottom lines such that adjacent lines are always printed overlapping in the same direction.

Due to the shape of the bead, 3D printed lines overlap slightly with the adjacent lines. The monotonic ordering ensures that the overlap is always in the same direction. This helps to make the shape of each line more consistent, resulting in a smoother looking surface.

<!--screenshot {
"image_path": "skin_monotonic_disabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": false
},
"layer": 1,
"line": [29, 45, 61, 77, 93, 109, 125, 141, 157, 161, 177, 193, 199, 211, 231, 246, 262, 280, 296, 312, 326, 342, 358, 374, 397, 417, 433, 449, 464, 480, 499],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_monotonic_enabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": true
},
"layer": 1,
"line": [31, 47, 63, 77, 93, 109, 115, 131, 147, 163, 181, 197, 213, 229, 244, 263, 281, 296, 319, 340, 356, 372, 379, 395, 411, 427, 443, 459, 475, 491, 507, 511],
"delay": 125,
"colours": 32
}-->
![Not a monotonic order](../images/skin_monotonic_disabled.gif)
![Monotonic order](../images/skin_monotonic_enabled.gif)

The surface looks more consistent with a monotonic order because the adjacent lines layer on top of each other in the same direction. This causes the surface to reflect light in the same direction. As a result, the shimmer of the surface is completely smooth, instead of some parts of the surface shimmering under a different angle than others.