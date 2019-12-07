If your model has a small horizontal slit, smaller than the top/bottom skin thickness, this setting doesn't bother filling the top and bottom above/below that completely with skin. This saves on slicing and printing time, but might expose infill to the air.

![Normally there is skin around the small horizontal slit](../images/skin_no_small_gaps_heuristic_disabled.png)
![If this is enabled, it doesn't properly close the skin](../images/skin_no_small_gaps_heuristic_enabled.png)

The main intent of this setting is to reduce slicing time. This setting effectively reduces the resolution with which Cura samples where skin must be placed. Depending on the shape of the model, this could save anywhere between 5% and 30% on slicing time. It will also save on printing time if there are any small gaps, because instead of skin it will print infill.

If the model has no horizontal gaps smaller than the skin thickness, the only effect will be reduced slicing time.

If the model does have such horizontal gaps, there will be infill exposed in the gap. However if the gap is small enough, the overhang would make the walls sag down enough that it won't be visible anyway.