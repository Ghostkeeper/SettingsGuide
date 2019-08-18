Originally, this setting caused the printer to start each layer with the object nearest to the position specified in the [Layer Start X](layer_start_x) and [Layer Start Y](layer_start_y) settings, instead of with the object that was printed last in the previous layer.

**The setting was hidden in Cura 2.4 and never properly removed, which is why this setting still exists in this list. However, it has no effect on the print.**

The alternative behaviour was no longer possible after multi-threaded slicing was implemented, so the setting was hidden.

Printing every layer in the same order prevents stacking two layers on top of each other immediately after each other, if there are multiple parts to print. This allows the previous layer to cool down longer while the nozzle is busy printing the other parts. This improves overhang and reduces banding and sagging. On the other hand, it makes the printer travel around a bit more, increasing printing time slightly.