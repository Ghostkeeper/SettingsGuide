Support Stair Step Minimum Slope Angle
====
With this setting you can disable stair stepping on the very bottom of the support, up until the slope of the model has a certain angle.

![Stair stepping disabled until the slope is 10°](../images/support_bottom_stair_step_min_slope_10.png)
![Stair stepping disabled until the slope is 30°](../images/support_bottom_stair_step_min_slope_30.png)

At shallow slopes, the stair steps at the bottom can be very wide. They can never be wider than what the [maximum width](support_bottom_stair_step_width.md) indicates, but since that distance is held from all sides, the stair steps can become so wide that there is a substantial distance that the support will need to bridge. If there is a small valley that the support rests in, it can even just cause the whole bottom side to skip, making the entire support rest only on the corners of the stair steps.

For those cases, you can limit the stair steps to occur only on the steeper slopes. This setting decides what constitutes a "steep" slope in that regard.

Increasing this setting will prevent Cura from generating the stair steps on shallow surfaces. This will make the support more sturdy, but harder to remove. Your support will leave more scars on the surface. Reducing it will make support easier to remove and will leave a nicer surface where the support was resting, but in some cases it can cause support to have to bridge long distances or even appear to hang in mid-air completely.

To get a nice surface, it's best to leave this setting at a conservative low angle, 5° or 10° or so. If the support rests on a surface that's shallow but not completely flat, inspect layer view and increase the angle if you find that support looks very precarious.