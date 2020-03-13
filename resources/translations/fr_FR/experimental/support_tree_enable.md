Tree support offers an alternative approach to supporting the model than the ordinary support technique. In tree support, a branching structure is generated that starts on the build plate with a small base, but grows towards the parts that need supporting.

![A tree-like structure supports the overhang](../../../articles/images/support_tree_enable.png)

Tree support can avoid obstacles when growing towards the overhang areas. If at all possible, the tree will be grown from the build plate upwards to prevent scarring of the surface that the support rests on. If this is not possible, the tree will be resting on the model's surface as close to the overhang as possible to minimise time and material usage. The branches of tree support are limited by the [Tree Support Branch Angle](support_tree_angle.md) so that they don't produce too steep an overhang of themselves. This limits the ability to grow around obstacles and also determines the height at which trunks will start branching out.

Tree support is hollow by default. However the ordinary support settings still apply to the area circumscribed by the tree's branches. In particular, the [Support Density](../support/support_infill_rate.md) can be used to give the support more structural strength. Due to the nature of tree support being greatly jagged, it normally has plenty of strength for its purpose.

Tree support has a number of advantages over normal support, to name a few:
* Tree support generally uses way less material than ordinary support. Between 25% and 50% of the material usage is typical. This saves a lot of time and cost in material.
* When printed with the same material as the print, overhang tends to look better when using tree support.
* Tree support is easier to remove than normal support.
* Tree support leaves fewer scars on the surface than normal support, due to being able to reach around the model towards the build plate.

However this comes with some disadvantages as well:
* Tree support takes an order of magnitude longer to slice. Patience will be necessary, especially with tall models.
* There are lots of interruptions in the flow when the smallest branches are printed, making tree support unsuitable to print using materials that are hard to extrude, such as PVA or flexible materials.
* Tree support doesn't work very well to support some mechanical models. In particular, it tends to place too few branches to support flat, sloped overhangs.

While tree support can be activated at the same time as ordinary support, this is generally not desirable. The two types of support will intersect and cause overextrusion.