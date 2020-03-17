Support Flow
====
This setting adjusts the flow rate for the support only. The flow rate for the support can be adjusted separately from the flow rate of the rest of the print.

Adjusting the flow rate during the support is a stop gap method to fix problems with extrusion rate or the adhesion between the support and the print. The same effect can be achieved by adjusting the [line width](../resolution/support_line_width.md) or [line spacing](../support/support_line_distance.md) of the support, but adjusting the flow may be more intuitive.

If there is a problem with extrusion rate or strength only during the support, it is better to look at the [printing speeds](../speed/speed_support.md) and [temperature](material_print_temperature.md). Perhaps the flow difference between the support and the other structures is too great to properly extrude. Another common issue with the flow rate of support is that there are too many crossings in the [support pattern](../support/support_pattern.md). It could help to choose a pattern that doesn't cross itself, such as Gyroid or Zigzag.