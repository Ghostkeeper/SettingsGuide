壁顺序
====
该设置定义内外壁哪个先打印，从外向内还是从内向外。

<!--screenshot {
"image_path": "outer_inset_first_disabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
"skin_outline_count": 0,
"inset_direction": "inside_out"
},
"layer": 2,
"line": [0, 6, 12, 18, 25, 35, 41, 47, 54, 57, 61, 64, 65, 68, 72, 74, 77, 79, 80, 82, 86, 96, 102, 108, 114, 125, 131, 137, 144],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "outer_inset_first_enabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
"skin_outline_count": 0,
"inset_direction": "outside_in"
},
"layer": 2,
"line": [0, 6, 12, 18, 25, 35, 41, 47, 54, 58, 61, 63, 64, 66, 70, 72, 76, 79, 80, 83, 88, 97, 103, 109, 116, 125, 131, 137, 144],
"delay": 125,
"colours": 32
}-->
![内壁先打印](../images/outer_inset_first_disabled.gif)
![外壁先打印](../images/outer_inset_first_enabled.gif)

该设置对质量和尺寸精度有些小的影响:
* 从外向内打印可以提高尺寸精度。相邻的壁通常互相挤压，尤其当壁线宽度小于喷嘴尺寸时。先打印的壁固化后，不会被挤压很多。因此，先打印外壁会使他的位置更准确。
* 如果填充在壁之前打印，那么从外向内打印可以减少填充在表面上的透出效果。否则如果先打印填充，然后由内向外打印。内壁会受到填充的挤压，外壁又会受到内壁的挤压。结果就是表面会透出填充。如果先打印外壁，则在打印内壁时外壁已固化完毕，这样就可以避免上述问题。
* 从内向外打印更适合悬垂。这是因为悬垂的外壁比内壁离上一层更远。如果先打印外壁，后一层的外壁没有稳固的抓手（容易脱落）。先打印内壁时，外壁则可以侧着黏到其他外壁上。

当壁的数量是奇数时，中心的壁总是最后被打印。
