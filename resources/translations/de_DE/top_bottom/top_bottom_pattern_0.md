Bottom Pattern Initial Layer
====
This setting configures which pattern will be used for the bottom side of the model where it rests directly on the build plate or the raft. The pattern for this layer is configured separately from the rest of the bottom layers.

<!--screenshot {
"image_path": "top_bottom_pattern_0.gif",
"models": [
    {
        "script": "gear_hollow.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [40, -40, 110],
"settings": {"top_bottom_pattern_0": "concentric"},
"layer": [1, 2, 3],
"colours": 64
}-->
![The initial layer is printed with a concentric pattern, but the rest is the lines pattern](../../../articles/images/top_bottom_pattern_0.gif)

The concentric pattern tends to adhere much better to the build plate than other patterns, because the tension in the lines when they are shrinking is spread out in all directions. This prevents warping and improves the reliability of the print. Other patterns contract all in one direction.

When printing with a raft, using the lines pattern tends to give a slightly stronger part. The lines are then also oriented such that they bridge the gaps between the raft lines well, creating a smoother bottom side.