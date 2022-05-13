Wall Transitioning Filter Margin
====
Some models have thin pieces hovering around the threshold where different numbers of walls get used. This could make the number of walls alternate back and forth even though the actual width of the piece doesn't vary much. The alternation ruins the print quality, requiring lots of flow changes and adding more travel moves. Using this feature, transitions are removed if it would have transitioned back and forth.

When a transition gets removed, then temporarily some of the lines can get too wide or too thin. This setting puts a limit on which transitions are filtered out by limiting how much wider or thinner the line is allowed to be.

<!--screenshot {
"image_path": "wall_transition_filter_off.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 0,
	"wall_transition_filter_margin": 0,
	"wall_line_count": 3
},
"colours": 64
}-->
<!--screenshot {
"image_path": "wall_transition_filter_on.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 100,
	"wall_transition_filter_margin": 0.2,
	"wall_line_count": 3
},
"colours": 64
}-->
![With a low margin, it alternates between 2 and 3 walls](../images/wall_transition_filter_off.png)
![With a higher margin, it no longer alternates](../images/wall_transition_filter_on.png)

To be precise, the lines are allowed to become thinner than the [Minimum Wall Line Width](min_wall_line_width.md) by this margin if that prevents going back and forth between different numbers of walls. Similarly, lines are also allowed to become slightly wider by this margin, even if an extra wall of the Minimum Wall Line Width could have fit in too.

This filter aims to solve a common problem with thin parts using low resolution 3D meshes. The 3D model, consisting of flat triangles, can't represent a curve exactly but only approximates it. The curve will have edges, with flat surfaces between them. When modelling a curved part with a constant width, it's important that the edges on the outside line up with the edges on the inside. If they don't, the width of the ring varies slightly, which can cause the effect shown above. If it does, the transitioning filter should prevent it from having too much of an effect.

Increasing the margin prevents creating small line segments in some cases. This is quicker to print and can make the surface look smoother. However it also allows for more extreme line widths, which may not extrude well out of your nozzle. When printing low-resolution models with thin pieces, increasing the margin may help to improve quality. With difficult materials, it's better to stay on the safe side.

**This setting doesn't just apply to normal walls, but also to extra skin walls, support walls, infill walls and concentric patterns.**