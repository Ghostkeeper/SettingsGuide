Minimum Wall Line Width
====
When printing thin pieces, Cura adjusts the width of wall lines to fit the exact width of the model. Cura can also decide to use fewer wall lines instead. This setting decides the threshold at which Cura decides to remove a wall instead of making the existing walls thinner.

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
"image_path": "min_wall_line_width_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_wall_line_width": 0.1,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![Normally the lines are made wider to fit](../images/min_wall_line_width_0_34.png)
![Reducing the minimum line width, it chooses to use more lines](../images/min_wall_line_width_0_1.png)

Different numbers of walls
----
If there is a single central line and the [Wall Distribution Count](wall_distribution_count.md) is set to 1, this setting functions exactly as it says. If the line in the middle gets thinner than a certain width, it gets removed in favour of making other lines wider. In other cases, the calculation is more complex.

The precise calculation of this is complex, but an intuitive understanding can be useful. Effectively, you can simply divide the total width of the model by the [ordinary line width](../resolution/wall_line_width.md) to arrive at a certain number of walls. This can be a fraction though (such as 5.3 wall line widths). The Minimum Wall Line Width takes just that fractional part (0.3 line widths) and adds an extra wall if it exceeds the Minimum Wall Line width. With the number of walls known, it then determines the width of each of the lines according to the Wall Distribution Count.

![How Minimum Wall Line Width affects the number of walls](../images/min_wall_line_width.svg)

Effectively this means that if there are more lines that get their width adjusted, the line width will never be as extreme as the Minimum Wall Line Width would allow. For example, if the middle two lines are adjusted, the line width will not drop below the average of the normal line width and the Minimum Wall Line Width.

The setting can separately be tuned for [even](min_even_wall_line_width.md) and [odd](min_odd_wall_line_width.md) number of walls. Having 0 walls is also a separate case, which can be tuned using the [Minimum Feature Size](min_feature_size.md) setting.

Tuning
----
In theory, setting this to 50% of the line width ensures that the line width stays closest to the ordinary line width. However it's better to stay a bit above that. It's easier for a printer to print lines wider than the nozzle size than it is to print thinner lines, and having fewer lines also means that the print will be faster.

With very viscous materials or when printing faster, the Minimum Wall Line Width should be decreased to prevent creating lines that are too wide. These are hard to print if the material doesn't get the time to flow out to the sides enough. If the Minimum Wall Line Width is too high, the walls don't stick well together which makes the print fragile. 