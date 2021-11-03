Lightning Infill Prune Angle
====
The Lightning infill pattern produces a tree-like structure on the inside of the print which starts small, but branches out to reach all the parts of the top of the print that need to be supported from the inside. This setting indicates how far the tree's branches can overhang at the endpoints.

![At 40° the Lightning infill is pretty stable](../images/lightning_infill_prune_angle_40.png)
![At 70° the branches overhang quite steeply](../images/lightning_infill_prune_angle_70.png)

Increasing the prune angle means that the infill will be able to start smaller at the bottom while still reaching all of the top surface. In many cases it doesn't even need to start at the bottom any more but can simply hang on to the sides. The prominent effects of increasing this angle are:

* Reduced printing time and material usage.
* Smoother walls, because there will not be as much infill touching the walls from the inside.
* Slightly reduced strength.
* More chance of print failure. If the overhang is too steep, there will be a significant overhang on the end of each line, which will sag and could get loose.

In practice, the prune angle can be higher than normal overhang angles or the other Lightning infill overhang angles. Since the lines are supported well on the layer below, having some more overhang isn't really a problem.
