Vertical Scaling Factor Shrinkage Compensation
====
This setting scales the model automatically before slicing, in the vertical direction. The aim is to compensate for any shrinkage that happens when the print cools down to room temperature. By making the print slightly bigger than desirable, the final result could be more accurate to the original dimensions of the input model. This scaling factor applies only to the Z direction.

Scaling in the vertical direction is less of an issue than in the horizontal directions, because there are fewer internal stresses in the vertical direction. There are no vertically printed lines, and so the contraction after printing will almost completely be horizontal. The material itself contracts due to cooling, but this is a very small effect, especially with PLA.

A factor of 100% will not cause any scaling. A scaling factor of slightly more than 100% is appropriate for some high-temperature materials such as polycarbonate. A scaling factor of less than 100% would indicate that the material grows when cooling, like a foam perhaps.