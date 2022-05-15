Minimum Feature Size
====
This setting controls the minimum width of details of the model that will be printed. Anything thinner than this will not get printed.

Details that are smaller than the nozzle size are not likely to print well. This is a limitation of the printer. However Cura can still attempt to print them, accepting that it will not have a nice extrusion rate, or that the details will end up thicker than modelled.

Reducing the Minimum Feature Size makes the printer print smaller details of the print. Depending on the [Minimum Thin Wall Line Width](min_bead_width.md), these tiny details may be printed by extruding very little (causing [underextrusion](../troubleshooting/underextrusion.md)), or by extruding more reasonable line widths but printing them over-sized. Setting this value to 0 makes the printer go all the way into the very tips of every sharp corner.

Increasing the Minimum Feature Size makes the printer not bother with small details that wouldn't come out nicely anyway. This saves a bit of time and could make the print come out cleaner.