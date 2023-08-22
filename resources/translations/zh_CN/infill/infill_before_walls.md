先填充物后壁
====
这会影响打印的顺序。启用此设定后，将先打印零件的填充，然后再打印该层上的壁。

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
"line": [0, 1, 2, 3, 4, 7, 8, 9, 10, 12, 15, 18, 21, 24, 27],
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
"line": [0, 1, 4, 7, 10, 13, 16, 20, 21, 22, 23, 26, 27, 28, 29],
"colours": 32,
"delay": 250
}-->
![禁用本设置，墙壁先打印](../images/infill_before_walls_disabled.gif)
![启用本设置，填充先打印](../images/infill_before_walls_enabled.gif)

此设置是准确性和强度之间的折衷：
* 如果在填充之前打印壁，则壁可能没有任何可贴附的物件，导致壁下垂更多。然而，壁将首先凝固，不会被填充推开，这会防止填充透过壁。
* 如果在壁之前打印填充，则壁将被从填充贴附的位置推开，这会使壁不太精确，并可能导致填充透过表面，形成外部可见的图案。但是，在打印壁时，填充将更好地将壁固定到位。
