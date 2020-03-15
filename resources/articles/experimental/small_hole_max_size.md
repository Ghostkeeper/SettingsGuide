Small Hole Max Size
====
Small details of the print are often very dimension-critical. This setting causes small holes in the print to be printed more slowly in order to achieve greater accuracy.

If a circular hole has a diameter less than this setting's value, the speed at which the perimeter of that hole is printed will be multiplied by a factor of the [Small Feature Speed](small_feature_speed_factor.md) (reduced, normally). For holes that are not circular, they will be printed at a different speed if the circumference is less than a circle with the diameter specified here. See also [Small Feature Max Length](small_feature_max_length.md); that is the setting that will actually be used for slicing.

A common use case for this feature is to print screw holes at very accurate dimensions. During the printing of small holes, the bead tends to get pulled along with the nozzle into the corner. If the corner is very sharp, as with small holes, this has the effect of making the hole smaller. When printing more slowly, this pull is reduced because the material has more time to settle in and because the mechanical pull is simply lower.

Increasing this setting causes more contours to be marked as a "small feature". A greater portion of the holes in the print will be printed slower. This causes those holes to be printed more accurately, but will increase printing time.