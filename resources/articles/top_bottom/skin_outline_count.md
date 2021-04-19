Extra Skin Wall Count
====
When printing the top and bottom with the lines pattern, the outer rim of the skin areas can still be printed with a few concentric lines. This is different than printing an extra wall, because the extra skin wall also gets put between the skin and the infill.

<!--screenshot {
"image_path": "skin_outline_count_0.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 0},
"layer": 115,
"colours": 64
}-->
<!--screenshot {
"image_path": "skin_outline_count_2.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 2},
"layer": 115,
"colours": 64
}-->
![No extra skin outlines](../images/skin_outline_count_0.png)
![Two extra skin outlines](../images/skin_outline_count_2.png)

Normally the skin lines can end inside the sparse infill. Their endpoints will sag a little bit then. If there are any extra skin walls, the printer will print a perimeter around the skin first that the normal skin lines can attach to. The skin won't sag as much in the end points then. In the end, this tends to improve the quality of top surfaces a bit.