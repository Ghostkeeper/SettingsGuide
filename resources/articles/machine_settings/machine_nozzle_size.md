Nozzle Diameter
====
This setting measures the diameter of the nozzle opening through which the material flows.

![Dimensions of the print head](../images/head_dimensions.svg)

This is an important dimension that other settings can base their defaults on. Most importantly, the [Line Width](../resolution/line_width.md) is normally adjusted based on the nozzle size. Some printer profiles limit the layer height based on the nozzle size as well, since the nozzle size is the most important factor in how fast material can be extruded.

The nozzle size is also used directly, for one detail: When filling [tiny gaps](../shell/fill_perimeter_gaps.md), line pieces further than two nozzle sizes away from each other are not merged together.

Do not adjust the nozzle size unless you actually modify the physical nozzle. Some slicers (including Cura 15.04 and earlier) use the term "nozzle size" to mean how wide the lines of the print should be. Cura uses the [Line Width](../resolution/line_width.md) setting for that.