When printing concave shapes, there will be some top skin that ends somewhere halfway through the infill. This setting adds an extra line through the infill to support the edge of the skin, so that it sags a little bit less.

![A perimeter is drawn through the infill under the edge of the skin](../images/skin_edge_support_thickness.png)

A single line through the gaps in the infill will still sag, so the line may be drawn on multiple layers underneath the edge of the skin that needs supporting. This setting configures the vertical thickness of the line underneath the edge of the skin. Alternatively you can directly adjust the [number of layers](skin_edge_support_layers.md) underneath the edge of the skin where this line will get drawn.

Increasing this thickness will generally have the following effects on the print:
* The edge of the skin will get supported better, leading to a more smooth top side because the skin can bridge completely from one side to the other.
* It takes slightly longer to print, and will use more material.

If the infill rate is high, this setting will hardly have any effect on the top surface and could cause [overextrusion](../troubleshooting/overextrusion.md) in the infill. It is best left at 0mm then.