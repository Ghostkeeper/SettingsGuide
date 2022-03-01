Support Stair Step Maximum Width
====
If [Support Placement](support_type.md) is set to "Everywhere", the support is allowed to rest on the model. It won't follow the contours of the model exactly though. Instead, the bottom side of the support is given a stair stepping pattern. This way, the support only makes a connection to the model in a few locations.

This setting determines the maximum width of these steps. The step normally gets a width that follows the model's surface with a given value of [Support Stair Step Height](support_bottom_stair_step_height.md). However if that is too wide, the width gets limited to the Support Stair Step Maximum Width. It then follows the model's surface for the rest of the step.

<!--screenshot {
"image_path": "support_bottom_stair_step_width.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"settings": {
    "support_enable": true,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_width": 0.7
},
"colours": 64
}-->
![Stair steps limited in width, causing support to follow the model](../images/support_bottom_stair_step_width.png)

This setting should normally be set to the maximum distance that can be bridged by the material without compromising the stability of the support lines above it. Lowering the setting causes the support to follow the model more often, making support more stable. Increasing the setting causes the support to adhere to the set value for Support Stair Step Height more often, making support easier to remove from the model.