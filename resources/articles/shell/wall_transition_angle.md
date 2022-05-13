Wall Transitioning Threshold Angle
====
This angle indicates the angle at which Cura starts creating transitions to properly fill the space. Any corners that are sharper than this angle will get filled with variable-width lines.

<!--screenshot {
"image_path": "wall_transition_angle.png",
"models": [{"script": "sharpening_corners.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_angle": 11,
	"wall_line_count": 4
},
"colours": 64
}-->
![Wider than 10°, it's no longer creating transitions](../images/wall_transition_angle.png)

Effectively this turns variable line widths on or off for certain corners. If two opposite walls are almost parallel, smaller than the angle specified in this setting, the area between them gets filled with lines that may vary in their width. If they are at a greater angle from one another, the space between them gets filled with constant-width walls.

As always, this is a trade-off. Using a variable width has some advantages, such as:
* It leaves no gaps between the lines.
* It doesn't fill the same space multiple times.
* The dimensions of the print will be more accurate there.

However it also has some disadvantages:
* It introduces corners in thin pieces that may appear as ripples on the surface.
* It creates extra travel moves.
* The printer may not accurately change the line width in quick succession.

In practice, it's good to make this angle large enough to reduce the size of the gaps in sharp corners, as can be seen in layer view, but as small as possible otherwise. A smaller angle generally makes the surface look smoother.

It's not possible to reduce the angle to 0° to get rid of variable line widths altogether. Parallel opposite walls will always get their line width adjusted to fit the space.