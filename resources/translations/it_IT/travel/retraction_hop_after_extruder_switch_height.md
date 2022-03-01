Z Hop After Extruder Switch Height
====
This setting controls the height difference when making a Z hop after the extruder switch. This height can be adjusted separately from the ordinary [Z Hop Height](retraction_hop.md) setting.

This can be useful since the nozzle tends to ooze more while it's been in stand-by while other extruders have been printing. This extra ooze will be bigger and thus requires a greater clearance between the nozzle and the last printed layer. Setting the Z hop height slightly higher after an extruder switch prevents the bigger-than-usual blob underneath the nozzle from hitting the print as well, without incurring additional printing time for most of the Z hops.