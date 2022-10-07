Monotonic Top Surface Order
====
Normally, Cura orders lines such that the travel distance between them is small. If this setting is enabled, it will order the top surface lines such that adjacent lines are always printed overlapping in the same direction.

When printing top surface lines, the lines usually overlap a bit with the lines next to them, because the shape of a line is not a perfect rectangle. This overlap gives the lines a slight slope, causing them to reflect light differently in different directions. If adjacent lines overlap differently, this reflection changes. You can see this in the final result. It gives different areas of the surface a different shine. Printing in a monotonic order ensures that the overlap is the same on the entire surface, so there is no difference in how it reflects light. This makes the surface look more consistent and smooth.

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
    "skin_monotonic": true
},
"layer": 1,
"line": [31, 47, 63, 77, 93, 109, 115, 131, 147, 163, 181, 197, 213, 229, 244, 263, 281, 296, 319, 340, 356, 372, 379, 395, 411, 427, 443, 459, 475, 491, 507, 511],
"delay": 125,
"colours": 32
}-->
![Not a monotonic order](../images/skin_monotonic_disabled.gif)
![Monotonic order, always from the bottom-right corner](../images/skin_monotonic_enabled.gif)

The monotonic order will slightly increase the length of travel moves, but this effect is very minimal. It only has a visual effect on the print. There are no mechanical advantages to the monotonic ordering.

To achieve a smooth surface, consider pairing this setting with setting the [Combing Mode](../travel/retraction_combing.md) to avoid skin, and perhaps to enable [Z Hops](../travel/retraction_hop.md). Alternatively you could also enable [ironing](../top_bottom/ironing_enabled.md), but that completely overrides the usefulness of this setting. Ironing has its own [monotonic option](../top_bottom/ironing_monotonic.md).