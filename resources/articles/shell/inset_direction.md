Wall Ordering
====
This setting determines which walls are printed first, printing them from the outside in, or from the inside out.

<!--screenshot {
"image_path": "outer_inset_first_disabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "outer_inset_first": false
},
"layer": 2,
"line": [0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 23, 29, 35, 45, 51, 57, 63, 67, 68, 69, 70, 71, 72, 73, 74, 84, 90, 96, 102, 113, 119, 125, 131],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "outer_inset_first_enabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "outer_inset_first": true
},
"layer": 2,
"line": [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 24, 30, 36, 47, 53, 59, 65, 70, 71, 72, 73, 74, 75, 76, 77, 86, 92, 98, 104, 114, 120, 126, 132],
"delay": 125,
"colours": 32
}-->
![The inner wall is printed first](../images/outer_inset_first_disabled.gif)
![The outer wall is printed first](../images/outer_inset_first_enabled.gif)

This setting has a small effect on quality as well as dimensional accuracy:
* Printing from outside inwards will improve dimensional accuracy. Adjacent walls generally push each other a bit, especially if the wall line width is smaller than the nozzle size. The wall that gets printed first will have been solidified and then doesn't get pushed as much. Therefore printing the outer wall first will make your outer wall be in a more accurate location.
* If the infill is printed before the walls, printing from the outside in will reduce how much the infill shows through on the surface. Otherwise the infill is printed first, then the inner walls which get pushed outwards by the infill, and then the outer wall which gets pushed outwards by the inner walls. As a result, a pattern could be visible on the outside. If the outer wall is printed first, the outer wall can solidify before the inner wall is able to push on it.
* Printing from the inside out is better for overhang. The outer wall is further removed from the previous layer than the inner wall. When printing the outer wall first, the outer wall has nothing yet to grab on to. When the inner wall is printed first, the outer wall can attach sideways to the outer wall.