If [Support Placement](support_type) is set to "Everywhere", the support is allowed to rest on the model. It won't follow the contours of the model exactly though. Instead, the bottom side of the support is given a stair stepping pattern. This way, the support only makes a connection to the model in a few locations.

This setting determines the height of these steps.

![Stair steps forming at the bottom of support](images/support_bottom_stair_step_height.png)

The stair step height is counted by the distance from the surface of the model. This means that if you have a vertical distance set in the [Support Bottom Distance](support_bottom_distance) setting, this gets subtracted from the height and the connection between the model and the support will be greater. Similarly, the [Support Floor](support_bottom_enable) also causes the effect of the stair steps to be reduced.

The [Support Stair Step Maximum Width](support_bottom_stair_step_width) setting limits the width of the steps. If the model's surface is so shallow that a small step height would incur a huge step width, the support will follow the surface of the model for the rest of the step's height.

Reducing this setting will cause the bottom of support to be smoother. This increases adhesion between the support and the model, making it harder to remove the support but also making the support more stable.