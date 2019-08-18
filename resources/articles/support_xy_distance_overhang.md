If the Z distance of support is preferred over the X/Y distance, the horizontal distance between the support and the model is allowed to become smaller than the [Support X/Y Distance](support_xy_distance) setting to satisfy the required [Support Z Distance](support_z_distance).

This setting defines a minimum X/Y distance that must be held regardless of the Z distance. This minimum X/Y distance overrides the Z distance again.

![Minimum X/Y distance kicks in if the Z distance means that the X/Y distance would become very small](images/support_z_overrides_xy.svg)

Increasing this setting reduces the chance that the support hits the model on the side, leaving a scar where it's unnecessary. It also makes the support easier to remove. Keep in mind though that this only really kicks in at medium-steep overhangs where the overhang normally needs to be supported anyway, so it's meant to hit the support there. Increasing this setting also makes the overhang sag more, reducing its surface quality.