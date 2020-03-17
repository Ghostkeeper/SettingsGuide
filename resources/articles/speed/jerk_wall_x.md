Inner Wall Jerk
====
This setting determines the speed at which the nozzle can go through corners while printing the inner walls. This can be configured separately from the outer wall.

The inner walls are not very visible on the outside, except on flat top and bottom sides where ringing isn't much of an issue. They are obscured by the outer wall. However when printing the [inner walls before the outer walls](../shell/outer_inset_first.md), the vibrations in the inner walls will push the outer wall aside in certain places, causing the ringing to shine through to the outside surface even if the outer wall would be printed with perfect accuracy. If the outer wall is printed first, the effect is reduced. However having a vibrating nozzle pass along partially over the outer wall will still cause a faint ringing to appear.

For this reason, the inner wall jerk is normally somewhat greater than the outer wall jerk, but still less than the rest of the print.