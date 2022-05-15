Minimum Even Wall Line Width
====
When printing thin pieces, Cura adjusts the width of wall lines to fit the exact width of the model. Cura can also decide to use fewer wall lines instead. This setting is the threshold at which Cura will combine two lines into one. It can be adjusted separately from the [threshold at which the middle line is removed](min_odd_wall_line_width.md).

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
This setting allows adjusting the threshold for removing lines specifically when there is an even number of lines. This is when there are two lines in the centre rather than a single line. It determines when these two lines in the middle combine into a single line.

The minimum even wall line width might be different from the minimum odd wall line width because of the way they join together. Even lines join at their ends by making the ends come closer together. There is some overlap with these lines there, leading to overextrusion. This is different from when there is an odd number of walls: The line in the middle then just stops, leaving a gap in the print. Reducing the minimum even wall line width reduces the overextrusion at the transitions from even to odd lines. Reducing the minimum odd wall line width reduces the size of the gap at the transitions from odd to even lines.

The gaps left when an odd line ends is more visible in the end result than a bit of overextrusion at a joint, so it could help to set the Minimum Even Wall Line Width a bit higher than the Minimum Odd Wall Line Width.

Reducing this setting leads to:
* Reduced area of overlap where two lines join together to merge into one line.
* Reduced maximum width of single centre lines.
* Thinner lines, which may not extrude well.
* More lines, which take longer to print.