Skin Expand Distance
====
Make the solid layers on the top and bottom of your print wider or thinner in a horizontal direction. Normally the solid layers are only generated in parts where there is air above or beneath them, but with this setting you can expand it horizontally a bit further, improving strength by making the skin attach better to adjacent walls and closing gaps in the skin.

<!--screenshot {
"image_path": "skin_preshrink_original.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_preshrink": 0,
    "top_skin_preshrink": 0,
    "bottom_skin_expand_distance": 0,
    "top_skin_expand_distance": 0
},
"colours": 32
}-->
<!--screenshot {
"image_path": "expand_skins_expand_distance_1mm.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_expand_distance": 1,
    "top_skin_expand_distance": 1
},
"colours": 32
}-->
![How skins (the yellow parts) normally look](../images/skin_preshrink_original.png)
![Skins expanded by 1mm](../images/expand_skins_expand_distance_1mm.png)

* If you have small holes in the top or bottom layers of the print (holes that are filled with the infill pattern), setting this a bit higher will close them. This allows the printer to continuously print bottom lines, greatly improving strength.
* If your model has a horizontal surface next to a steep wall, increasing this setting can improve adhesion between the walls of the steep surface and the skin, because the skin will be printed directly touching those walls.
* Setting this setting to a negative value will reduce the width of the top and bottom layers, replacing it with infill. This can save some printing time, at the cost of strength.

**Due to technical limitations, you can't reduce this setting negatively below the value of [Skin Removal Width](skin_preshrink.md). Increase the Skin Removal Width setting in order to remove more skin.**