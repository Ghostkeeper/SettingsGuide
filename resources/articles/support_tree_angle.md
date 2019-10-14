This setting determines the maximum overhang angle that the branches of tree support are allowed to make. If the angle is increased, the branches can be printed more horizontally, allowing them to reach farther.

![A branch angle of 20°](images/support_tree_angle_20.png)
![A branch angle of 40°](images/support_tree_angle_40.png)

Reducing the branch angle will make the branches more vertical. Increasing it will make them go more horizontal. Because the branches are allowed to have greater overhang angles, they can reach farther around obstacles, allowing the support to rest on the build plate more often, rather than on the model. It will also allow the branches to split off at a later point.

The most important effects of increasing the branch angle for tree support include:
* Reduced scarring, due to less support needing to rest on the model rather than the build plate. If [Support Placement](support_type.md) is set to Touching Buildplate, more of the model can be supported.
* Reduced printing time and material usage, due to the branches splitting off at higher elevations. The branches are split off just in time to be able to reach all of the overhang.
* Reduced reliability. If the overhang angle becomes too great, the support will be greatly weakened, increasing the chance that the support breaks or tumbles over.

Large branch angles are best combined with low values for the [Tree Support Collision Resolution](support_tree_collision_resolution.md) setting. This will reduce the shifts in the tree's positions due to collision avoidance. That prevents the overhang distance from growing too big when the collision distance is adjusted.