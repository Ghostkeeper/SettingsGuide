WP Flow
====
With this setting, the flow rate can be adjusted while printing with the Wire Printing technique. This simply serves as a multiplier on the line width and layer height. It directly determines how much material is used for Wire Printing.

This setting adjusts the flow for the entire print, but the flow can also be adjusted separately for the [horizontal parts](wireframe_flow_flat.md) or the [connections](wireframe_flow_connection.md).

Wire Printing doesn't use the line width or layer height to determine how far lines and layers are spaced. It uses the [height](wireframe_height.md) and [inset distance](wireframe_roof_inset.md) only. So instead of adjusting the flow of the Wire Printing, you might as well adjust the [Layer Height](../resolution/layer_height.md) or [Line Width](../resolution/line_width.md) settings, or the [ordinary Flow](../material/material_flow.md). This will have the same effect. However these settings exist so that a print profile can be created that has correct flow for Wire Printing without influencing the print quality of normal prints that don't make use of Wire Printing.

Increasing the flow makes the wires thicker. This makes the frame more rigid once it's solidified. However it also increases the heat mass of the frame, making it take longer to solidify the wires. This makes the wires droop and reduces the reliability of the print, since the wires may not connect properly any more then.