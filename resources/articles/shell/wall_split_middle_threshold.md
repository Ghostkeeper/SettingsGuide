Split Middle Line Threshold
====
When printing thin pieces, Cura adjusts the width of wall lines to fit the exact width of the model. Cura can also decide to use fewer wall lines instead. This setting is the threshold at which Cura will split a single line in the centre into two, when the width of the part increases. It can be adjusted separately from the [threshold at which a new centre line is added](wall_add_middle_threshold.md).

This setting is the same as the [Minimum Even Wall Line Width](min_even_wall_line_width.md), but uses a different unit. The unit of this setting is in fractions of a line width that the width of a part needs to increase to split the centre line into two. Because the difference in width is divided over the two lines in the middle after splitting, a smaller Minimum Even Wall Line Width is equivalent to a much smaller Split Middle Line Threshold than in the case of removing an odd wall.

<!--screenshot {
"image_path": "min_wall_line_width_0_34.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
<!--screenshot {
"image_path": "min_wall_line_width_even_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_even_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![The centre line is made wider to fit](../images/min_wall_line_width_0_34.png)
![Reducing this setting, it uses two lines instead](../images/min_wall_line_width_even_0_1.png)

Even vs. Odd Lines
----
This setting allows adjusting the threshold for adding lines specifically when it becomes an even number of lines. This is when there are two lines in the centre rather than a single line. It determines when a line in the centre splits into two lines.

The threshold for splitting a middle line might be different from the threshold for adding a centre line because of the way they join together. Even lines join at their ends by making the ends come closer together. There is some overlap with these lines there, leading to overextrusion. This is different from when there is an odd number of walls: The line in the middle then just stops, leaving a gap in the print. Reducing the Split Middle Line Threshold reduces the overextrusion at the transitions from even to odd lines. Reducing the Add Middle Line Threshold reduces the size of the gap at the transitions from odd to even lines.

The gaps left when adding a centre line are more visible in the end result than a bit of overextrusion at a joint, so it could help to set the Split Middle Line Threshold a bit higher than the Add Middle Line Threshold.

Reducing this setting leads to:
* Reduced area of overlap where two lines join together to merge into one line.
* Reduced maximum width of single centre lines.
* Thinner lines, which may not extrude well.
* More lines, which take longer to print.

**This setting doesn't just apply to normal walls, but also to extra skin walls, support walls, infill walls and concentric patterns.**