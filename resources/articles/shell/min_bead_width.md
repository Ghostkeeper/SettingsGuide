Minimum Thin Wall Line Width
====
This setting allows printing very tiny details with a line width that is actually too big for them. Instead of printing very thin lines, it prints with a more reasonable line width.

If the [Minimum Feature Size](min_feature_size.md) is very low, some very thin parts could be printed. This doesn't work well. It's possible to print lines smaller than the nozzle size, but not by much. Printing too thin lines lead to inconsistent extrusion.

Instead, those very thin lines are made wider so that they extrude more consistently. Any part of the model that is thinner than the Minimum Thin Wall Line Width will get printed using a single line of the Minimum Thin Wall Line Width. The lines then become wider than the original width of the model. This reduces dimensional accuracy, but at least it will print reliably.

The value of this setting should be the thinnest line width that the printer can reliably achieve before it starts creating rough surfaces and inconsistent extrusion. This is normally somewhere between the nozzle size and half the nozzle size. Increasing it leads to thin parts being printed too fatly, but reduces the chance of underextrusion due to trying to print lines that are too thin.