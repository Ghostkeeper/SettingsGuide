WP Fall Down
====
While printing the wire frame, the material is expected to sag due to latent heat before it has the time to solidify. This would make the saw-tooth pattern too short. Whereas the horizontal rings are able to bridge due to the continuous horizontal motion, the saw-tooth pattern cannot. This setting compensates for the short stature of the saw-tooth pattern, making the pattern slightly taller so that the next horizontal ring will rest properly on it.

![How the height of the saw-tooth pattern is compensated for](../images/wireframe_fall_down.svg)

The value of the setting is added to the height of the saw teeth. Hopefully, this compensates for the sag during the printing of those saw teeth. If tuned well, the horizontal ring will be printed resting firmly on top of the saw-tooth pattern, instead of falling down lower than its intended printed height.

When combined with [Drag Along](wireframe_drag_along.md), the height of the saw-tooth pattern will become the normal [height](wireframe_height.md) plus the value of the Drag Along setting plus the value of this setting.