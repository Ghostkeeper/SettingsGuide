Small Feature Max Length
====
Small details of the print are often very dimension-critical. This setting causes small holes in the print to be printed more slowly in order to achieve greater accuracy.

If a hole in the print has a circumference less than indicated by this setting, the speed at which the perimeter of that hole is printed will be multiplied by a factor of the [Small Feature Speed](small_feature_speed_factor.md) (reduced, normally). This setting is a different way of approaching the [Small Hole Max Size](small_hole_max_size.md) setting, which is more generic than just for circular holes.

A common use case for this feature is to print screw holes at very accurate dimensions. During the printing of small holes, the bead tends to get pulled along with the nozzle into the corner. If the corner is very sharp, as with small holes, this has the effect of making the hole smaller. When printing more slowly, this pull is reduced because the material has more time to settle in and because the mechanical pull is simply lower.

Increasing this setting causes more contours to be marked as a "small feature". A greater portion of the holes in the print will be printed slower. This causes those holes to be printed more accurately, but will increase printing time.