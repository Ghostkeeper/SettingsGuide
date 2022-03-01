Monotonic Ironing Order
====
Normally, Cura orders ironing lines such that the travel distance between them is small. If this setting is enabled, it will order the ironing lines such that adjacent lines are always printed overlapping in the same direction.

Ironing lines are by default much thinner than the nozzle they are printed with, so the lines will overlap a lot with the lines next to them. This overlap gives the lines a slight slope, causing them to reflect light differently in different directions. If adjacent lines overlap differently, this reflection changes. You can see this in the final result. It gives different areas of the surface a different shine. Printing in a monotonic order ensures that the overlap is the same on the entire surface, so there is no difference in how it reflects light. This makes the surface look more consistent and smooth.

However, contrary to [the equivalent for top/bottom lines](skin_monotonic.md), this effect is for ironing is overwhelmed by a different effect. Ironing has such a low flow rate that the flow change coming from ordinary printing is very large. This makes the ironing layer thicker when it starts printing, and still leaves a noticeable border where printing was interrupted. A monotonic order will not remove these borders. While the surface might look slightly smoother, in practice printing the ironing lines in monotonic order is largely ineffective unless your printer has very accurate control over flow rate.

The monotonic order will slightly increase the length of travel moves, but this effect is very minimal.

To achieve a smooth surface, consider pairing this setting with setting the [Combing Mode](../travel/retraction_combing.md) to avoid skin, and perhaps to enable [Z Hops](../travel/retraction_hop.md).