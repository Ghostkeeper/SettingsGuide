Minimum Odd Wall Line Width
====
When printing thin pieces, Cura adjusts the width of wall lines to fit the exact width of the model. Cura can also decide to use fewer wall lines instead. This setting is the threshold at which Cura will remove a line in the centre. It can be adjusted separately from the [threshold at which the middle two lines combine](min_even_wall_line_width.md).

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
This setting allows adjusting the threshold for removing lines specifically when there is an odd number of lines. This is when there is a single line in the centre rather than two. It determines when this single line is removed in favour of having the two lines around it be slightly wider.

The minimum odd wall line width might be different from the minimum even line width because of the way they transition. When an odd line is removed, it stops before the transition and lets the surrounding walls close in. During the transition there is a bit of a gap where the surrounding lines haven't quite come together yet. This is different from when there is an even number of walls: The two lines in the middle then collapse together, overlapping them slightly. Reducing the minimum odd wall line width reduces the size of the gap at the transitions from odd to even lines. Reducing the minimum even wall line width reduces the overextrusion at the transitions from even to odd lines.

The gaps left when an odd line ends are more visible in the end result than a bit of overextrusion at a joint, so it could help to set the Minimum Odd Wall Line Width a bit lower than the Minimum Even Wall Line Width.

Reducing this setting leads to:
* Smaller gaps when a central line ends.
* Reduced maximum width of a pair of even centre lines.
* Thinner lines, which may not extrude well.
* Longer lines, which take longer to print.

**This setting doesn't just apply to normal walls, but also to extra skin walls, support walls, infill walls and concentric patterns.**