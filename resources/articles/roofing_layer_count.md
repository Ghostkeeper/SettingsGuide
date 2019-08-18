Part of the top of the print can be separated out and printed with different settings. This setting determines how big of a part to separate out. How many layers of the top of the print will get separate settings?

![The highest layer of the top is printed slower (blue) than the rest of the skin (green)](images/roofing_layer_count.png)

Some settings can greatly improve the quality of the top surface of the print, but they can make the print take much longer as they are applied to all skin layers at the top. A similar effect can be achieved by adjusting those settings only for the very top layer or two, but printing the rest of the skin layers faster. This will not have as big a negative effect on the printing time then.

Settings that can be adjusted for the top surface are:
* [Top Surface Skin Extruder](roofing_extruder_nr)
* [Top Surface Skin Flow](roofing_material_flow)
* [Top Surface Skin Speed](speed_roofing)
* [Top Surface Skin Acceleration](acceleration_roofing)
* [Top Surface Skin Jerk](jerk_roofing)
* [Top Surface Skin Line Width](roofing_line_width)
* [Top Surface Skin Pattern](roofing_pattern)
* [Top Surface Skin Line Directions](roofing_angles)

To achieve a nicer top surface, try reducing the speed and increasing the jerk.

When printing the top surface in a different colour (using the [Top Surface Skin Extruder](roofing_extruder_nr) setting), it is often necessary to print more than one layer in the other colour. Otherwise the original colour will still bleed through.