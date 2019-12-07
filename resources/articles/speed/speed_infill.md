The speed at which the infill material is printed can be configured separately from the normal print speed.

![Various structures printed at different speeds](../images/speed_difference.png)

The visual quality of infill is not usually important, so the infill can be printed at a fairly high speed to save time. On the other hand, increasing the infill speed also makes the infill shine through the walls more, because the nozzle will wobble more into the walls.

There is also the danger of introducing too great of a flow change. Especially when combined with settings like [Infill Layer Thickness](infill_sparse_thickness.md), the difference in the flow rate required for the infill and the flow rate required for the rest of the print can be very large. There is a large delay when adjusting the flow rate through the nozzle, so if the infill is made too fast compared to the rest, the flow could be inaccurate.