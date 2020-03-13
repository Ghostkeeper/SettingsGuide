Cura needs to know where the inside of the model is in order to fill it with material. If the surface of your model is not precisely closed or has internal walls, it may be ambiguous where the inside of the model is.

A common case of the model not being manifold, is when an extra piece of the model is attached to an otherwise closed part. This is common when editing meshes with CAD software that was not designed for manufacturing (but only for digital rendering) such as Blender or SketchUp. You can see an example of this in the images below.

![The mesh looks normal on the outside](../../../articles/images/meshfix_extensive_stitching_shell.png)
![X-ray view reveals an extra surface on the inside](../../../articles/images/meshfix_extensive_stitching_xray.png)
![With this setting disabled, only the properly closed volume gets printed](../../../articles/images/meshfix_extensive_stitching_disabled.png)
![With this setting enabled, the extra piece gets attached properly](../../../articles/images/meshfix_extensive_stitching_enabled.png)

This setting causes Cura to make a better attempt at closing gaps in the mesh if it is not properly watertight. This increases the chances of a good print, but increases slicing time and may sometimes connect the wrong surfaces together.