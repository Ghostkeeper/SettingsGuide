Pillowing is an effect where small bulges or holes appear in between the infill lines on the top side of the model. It is most often seen on (otherwise) flat top surfaces when printing at high flow rates.

![Severe bulges and small holes in the surface](../../../articles/images/pillowing.jpg)

Causes
----
Pillowing is a combination of several effects which work together to cause a bulging effect on the top side of the print.

The recognisable bulging of the top skin is actually a form of [warping](warping.md) where the top skin is compressed by the surrounding walls and underlying infill. Since the walls and infill are printed first in the lower layers, they will cool down and shrink while the skin is still being printed. While shrinking, the walls and infill push the skin lines inside to the point where they are bulging.

Another major factor in pillowing is the sagging of the skin lines in between the infill lines. Depending on the distance between the infill lines, the skin lines need to bridge quite a distance. If cooling is insufficient, the plastic will sag a bit. This makes the skin lines adhere less well to each other, leaving gaps between them. It takes a few layers of skin to repair that.

The pillowing effect tends to bulge up rather than down. While both up and down can happen, bulging up is more common since the nozzle is pulling on the top side of the plastic as it traverses over the skin, which exerts a shearing force upwards for a short moment. Once the lines are bulging upwards, the warping effect keeps them upwards.

Prevention
----
There are several methods to prevent pillowing in Cura:
* Increasing the [Top Thickness](../shell/top_thickness.md) is the most effective way to prevent pillowing. With more [top layers](../shell/top_layers.md), the higher layers are able to rest on the partially closed gaps of the previous layers. This gives them a better chance to close the gaps and form a strong top layer that doesn't pillow. In general, the thinner your layers are, the more top layers you will need since these layers are not as strong.
* Increasing the [Infill Density](../infill/infill_sparse_density.md) reduces the size of the gaps that need to be bridged by the top skin. This makes it easier to close those gaps. If you combine this with [gradual infill](../infill/gradual_infill_steps.md), most of the infill density can remain the same. Only the top will have a greater density to prevent pillowing.
* Printing at a lower [temperature](../material/material_print_temperature.md) improves bridging and warping in general, also with the top skin, which reduces the pillowing effect.
* Similarly, make sure to increase the [cooling](../cooling/cool_fan_speed.md) to improve the bridging as well.
* Reducing the [printing speed of the skin](../speed/speed_topbottom.md) will improve bridging directly. It will also push down the higher skin layers better on top of the lower layers. This closes the holes faster as well.