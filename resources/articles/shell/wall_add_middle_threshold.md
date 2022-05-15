Add Middle Line Threshold
====
When printing thin pieces, Cura adjusts the width of wall lines to fit the exact width of the model. Cura can also decide to use fewer wall lines instead. This setting is the threshold at which Cura will add a line in the centre. It can be adjusted separately from the [threshold at which the middle two lines combine](wall_split_middle_threshold.md).

This setting is the same as the [Minimum Odd Wall Line Width](min_odd_wall_line_width.md), but uses a different unit. The unit of this setting is in fractions of a line width that the width of a part needs to increase to add a new middle line.

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
"image_path": "min_wall_line_width_odd_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_odd_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![When the centre line is too small, the two lines around it are made wider](../images/min_wall_line_width_0_34.png)
![Reducing this setting, the centre line starts and ends much smaller](../images/min_wall_line_width_odd_0_1.png)

Even vs. Odd Lines
----
This setting allows adjusting the threshold for adding lines specifically when it becomes an odd number of lines. This is when there is a single line in the centre rather than two. It determines when a new line is added in between the two central lines.

The threshold for adding a centre line might be different from the threshold for splitting the middle line in two, because of the way they transition. When an odd line is added, it starts only when the two surrounding lines have made way for it. During the transition there is a bit of a gap where the surrounding lines haven't made enough room yet. This is different from when there is an even number of walls: The line in the middle then splits off into two, and those two lines overlap slightly until they are far enough apart. Reducing the Add Middle Line Threshold reduces the size of the gap at the transitions from even to odd lines. Reducing the Split Middle Line Threshold reduces the overextrusion at the transitions from odd to even lines.

The gaps left when an odd line starts are more visible in the end result than a bit of overextrusion at a joint, so it could help to set the Add Middle Line Threshold a bit lower than the Split Middle Line Threshold.

Reducing this setting leads to:
* Smaller gaps when a central line ends.
* Reduced maximum width of a pair of even centre lines.
* Thinner lines, which may not extrude well.
* Longer lines, which take longer to print.

**This setting doesn't just apply to normal walls, but also to extra skin walls, support walls, infill walls and concentric patterns.**