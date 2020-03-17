Connect Support ZigZags
====
If the zig-zag pattern is chosen for the [Support Pattern](support_pattern.md) setting, this setting makes the endpoints of the support pattern connect back towards itself, making the support stronger.

If the support connects back into itself, there will be no proper endpoint to the zig-zag pattern. The end point is normally fairly weak, especially for materials that are hard to extrude and need some time to get started after a travel move. This setting prevents that, making the support stronger. It improves adhesion to the build plate as well, since there is no enpoint where it can warp from.

This setting also increases adhesion to the model significantly, if support is allowed to rest on the model. The extra connection follows the model. It will be placed on top of the model, increasing the surface with which support adheres to the model. This makes support more stable as well, but makes it harder to remove and causes it to leave more of a scar.