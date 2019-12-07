With the [Top Surface Skin Layers](roofing_layer_count.md) setting, a number of layers at the very top can be given a different line width than the deeper top surface layers.

The skin on the top side of the print serves several functions. In particular it needs to close the holes on the top side left by the infill and it provides a great deal of strength to the part. Apart from that, it would ideally still look nice and smooth. Reducing the [line width of the top and bottom](skin_line_width.md) can serve to create a smoother surface, but will make the print take much more time. This setting allows for creating a smooth top surface with very thin lines without needing to print the rest of the top and bottom with the same line width. This incurs less of a penalty on printing time.

Reduce the top surface skin line width to achieve a smoother surface on the top side of your print. This will make the print take slightly longer though.

Reducing the line width too much can cause interruptions in the flow if it becomes less than the minimum flow rate out the nozzle. This causes the material to form beads as it flows out the nozzle and will make the top surface pockmarked and underextruded.

This technique is similar to [Ironing](ironing_enabled.md). However with Ironing, an extra pass is made on the same layer with very thin lines and extruding only minute amounts. With this setting the thin lines will be drawn in its own layer instead of the top skin. Ironing will cause overextrusion (on purpose). This setting will not.