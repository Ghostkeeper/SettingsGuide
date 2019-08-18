Many prints contain pieces that are thinner than the desired wall thickness. In most cases that is fine, but for some prints this would leave a gap between the walls. If this setting is enabled, gaps between the walls will be filled up with a spot of extra material.

![A long, thin gap between opposite walls is shown on the left and right side of the image](images/fill_perimeter_gaps_disabled.png)
![The gaps between walls are filled with material](images/fill_perimeter_gaps_enabled.png)

There are two common cases where filling gaps is useful:
* Between two opposite walls in prints that are thin (as shown in the images above). Filling these gaps increases strength of the part in those locations, because the two opposite walls are no longer able to move separately from each other.
* In very sharp corners, there will be a gap within the outer wall where the inner wall is too thick to reach into the corner. Filling these gaps increases strength but also makes the outside wall look more consistent.

**It's advisable to take good care to look which travel moves are necessary if this is enabled. The gap filling is done after the walls have completed printing.**