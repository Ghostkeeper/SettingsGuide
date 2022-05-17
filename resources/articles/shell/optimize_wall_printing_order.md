Optimize Wall Printing Order
====
If this is enabled, Cura will spend some extra slicing time to optimise the order in which the walls are printed. The goal is to reduce the number of travel moves and retractions by printing walls that surround the same part after one another.

<!--screenshot {
"image_path": "optimize_wall_printing_order_disabled.gif",
"models": [
    {
        "script": "plate_with_indent.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "optimize_wall_printing_order": false
},
"layer": 37,
"line": [0, 5, 9, 13, 17, 25, 29, 33, 37, 47, 54, 61, 71, 89, 106, 122, 142, 156, 160, 164, 169, 176, 183, 188, 194, 225, 241, 262, 282, 293, 297, 302, 309, 319, 326, 332, 343, 353, 358, 363, 368],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "optimize_wall_printing_order_enabled.gif",
"models": [
    {
        "script": "plate_with_indent.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "optimize_wall_printing_order": true
},
"layer": 37,
"line": [0, 4, 7, 11, 17, 25, 31, 36, 41, 47, 51, 55, 60, 67, 71, 76, 83, 92, 99, 106, 114, 123, 130, 136, 147, 165, 181, 197, 217, 239, 256, 278, 299, 312, 316, 320, 325, 331, 336, 343, 350],
"delay": 125,
"colours": 32
}-->
![Optimisation disabled](../images/optimize_wall_printing_order_disabled.gif)
![Optimisation enabled](../images/optimize_wall_printing_order_enabled.gif)

If this optimisation is enabled, the nozzle will print all the walls around one part first before moving to the next part, instead of printing all of the inner walls first before printing the outer walls. Optimising is usually positive, but with some parts it may impact dimensional accuracy because the previous wall hasn't solidified yet when placing down the next one next to it.

If the inner wall and the outer wall have greatly different flow rates, this optimisation also causes many more changes in flow rate. This manifests itself with a bigger [seam](../troubleshooting/seam.md) or some [blobs](../troubleshooting/blobs.md). The line width has a bigger impact on the print than this travel optimisation, so it's better to turn off the optimisation if this could be the problem in your print.