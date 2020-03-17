Z Seam Relative
====
When the seam is placed in a user-specified location according to the [Z Seam Alignment](z_seam_type.md) setting, you can enter coordinates for where the seam must be located. Normally those coordinates specify some location on the build plate, such as the back of the printer. If this setting is enabled, those coordinates will be taken relative to the position of the model.

![Disabled: The coordinates point to an absolute position in the centre of the build plate, so all the blue striped point towards the middle](../images/z_seam_relative_disabled.png)
![Enabled: The coordinates are relative to the model so every model will have the blue stripes in the same corner](../images/z_seam_relative_enabled.png)

When a mesh is duplicated on the build plate, this setting causes the seam to be positioned in exactly the same location for each of the duplicates, rather than having them point toward the same point on the build plate. This allows you to print every copy in exactly the same way regardless of their positions on the build plate.