Use Adaptive Layers
====
Adaptive Layers will adjust the layer thickness of your print locally to optimise printing time and quality based on the model's surface features. The layers will be made thinner where there are shallow slopes, or made thicker where the walls are steep. The purpose of this is to print fast where possible but still print detailed where needed.

![With the "layer thickness" colour scheme, you can see it colour thinner layers blue and thicker layers yellow](../images/adaptive_layer_height_enabled.png)

The layer height is adjusted such that the horizontal distance between the edges of the layers remains constant. Shallow surfaces cause a big horizontal displacement with a small vertical displacement, so a small vertical displacement is made to keep the horizontal displacement constant. With steep surfaces there is a small horizontal displacement with a large vertical displacement, so a large vertical displacement is made to keep the horizontal displacement constant. As such the topography effect of the layers is kept constant. The maximum distance between two adjacent layers is held at a constant distance of the [Threshold](adaptive_layer_height_threshold.md) setting.

If the model has both shallow surfaces and steep surfaces at the same height, the layer thickness is taken to be the smaller of the layer thicknesses. This sometimes makes the layer height unnecessarily small because there is a horizontal surface next to it. This can be seen in the screenshot above as well halfway the height of the silo on the left.

Adaptive Layers is heavily constrained in order to improve printing quality. The layer height is not allowed to deviate more than a specified [Maximum Variation](adaptive_layer_height_variation.md) from the original [Layer Height](../resolution/layer_height.md) setting. Between two adjacent layers the difference in layer height may not be more than a certain [Step Size](adaptive_layer_height_variation_step.md). This causes the layer thickness to gradually transition instead of suddenly cutting it in half from one layer to the next.

Adaptive Layers can considerably reduce the printing time without suffering a loss in print quality, or even while improving quality in some cases. The effect of adjusting the layer thickness is immense. In most cases, the printing time will be greatly reduced, due to using thicker layers where the model is vertical. The topography effect is also reduced because the layers are spaced closer together horizontally.

However this feature can introduce a number of problems as well.
* With changing the layer height, some other settings typically need to be adjusted as well, such as the nozzle temperature. Adaptive Layers will not automatically adjust those as well. This can make the print sub-optimal for e.g. overhangs that would fare better at a lower printing temperature.
* If the layer height is changed over the entire layer for a small feature somewhere in a small part of the layer, banding will be visible in the rest of the layer.
* Vertical distances are unintentionally adjusted with this as well. This may have a negative effect on the print quality. For instance, the [Top/Bottom Thickness](../shell/top_bottom_thickness.md) will typically become lower because Cura will hold the [Top Layers](../shell/top_layers.md) setting as truth, and the layers become thinner. This can cause pillowing. Affected settings that may no longer be correct include:
  * [Top Thickness](../shell/top_thickness.md)
  * [Bottom Thickness](../shell/bottom_thickness.md)
  * [Maximum Skin Angle for Expansion](../infill/max_skin_angle_for_expansion.md)
  * [Gradual Infill Step Height](../infill/gradual_infill_step_height.md)
  * [Gradual Support Infill Step Height](../support/gradual_support_infill_step_height.md)
  * [Infill Layer Thickness](../infill/infill_sparse_thickness.md)
  * [Support Infill Layer Thickness](../support/support_infill_sparse_thickness.md)
  * [Support Z Distance](../support/support_z_distance.md)
  * [Support Roof Thickness](../support/support_roof_height.md)
  * [Support Floor Thickness](../support/support_bottom_height.md)
  * [Support Overhang Angle](../support/support_angle.md)
  * [Support Stair Step Height](../support/support_bottom_stair_step_height.md)
  * [Tower Roof Angle](../support/support_tower_roof_angle.md)
  * [Ooze Shield Angle](../dual/ooze_shield_angle.md)
  * [Maximum Model Angle](../experimental/conical_overhang_angle.md)