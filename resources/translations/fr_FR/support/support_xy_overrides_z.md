Both the [X/Y distance](support_xy_distance.md) and the [Z distance](support_z_distance.md) of support should be observed exactly; not more, not less. This is overconstrained, so there must be a preference between the two. This setting determines that preference.

X/Y overrides Z
----
![X/Y overrides Z](../../../articles/images/support_xy_overrides_z.svg)

If the X/Y distance overrides the Z distance, then the X/Y distance is always kept constant, even if that means that the Z distance is greater than desired. The Z distance is still held as a minimum distance though, so if the overhang is very horizontal, the Z distance still kicks in, making the X/Y distance greater than desired.

Z overrides X/Y
----
![Z overrides X/Y](../../../articles/images/support_z_overrides_xy.svg)

If the Z distance overrides the X/Y distance, then the Z distance is always kept constant, even if that means that the X/Y distance is smaller than desired. The X/Y distance then only gets any influence over the print in locations where the Z distance does not come into play, so not at the top of the support structures but only at the sides.

A minimum X/Y distance is still observed though. If the overhang is very vertical, the X/Y distance would become so small that the support may fuse to the sides of the model. The [Minimum X/Y Distance](support_xy_distance_overhang.md) prevents that.