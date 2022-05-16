Alternate Wall Directions
====
If enabled, this setting makes the winding direction of the walls alternate between clockwise and counter-clockwise.

The first inner wall will be printed in the opposite direction as the outer wall, and the second inner wall will be printed in the opposite direction again. What's more, on the next layer it will start off opposite too, so that walls that are stacked on top of each other alternate as well.

Alternating the printing direction reduces the effect of internal stresses inside of the model, reducing the effect of [warping](../troubleshooting/warping.md). During the printing of any line, the nozzle pulls fairly hard on the string of molten material, which stretches the plastic. During the solidifying, this stress can deform the model. If the adjacent line is printed in the opposite direction, this stress is counteracted by adjacent lines pulling in the opposite direction. The force of the stress is countered by stress in the opposite direction.

The disadvantage of alternating the wall directions comes from hysteresis in the gantry of the printer. If there is any play in the axles or pulleys of the printer, then diagonal lines will be placed down in a slightly different spot when printing in the opposite direction. As a result, the wall becomes less smooth and the print dimensions less accurate. A well-tuned printer will not show this effect, so if the printer has tightened belts, pulleys and accurate components, alternating the wall directions is likely to only give advantages.

When [printing from the inside out](../shell/inset_direction.md), this setting makes the seam of the wall more visible and causes some ringing, because the nozzle does a complete 180° turn just before the start of the outer wall, which causes vibrations. This is not a salient effect when printing from the outside inwards.