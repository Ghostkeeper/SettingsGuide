Print Thin Walls
====
Normally, Cura will omit walls that are thinner than the <!--if cura_version<5.0:[Outer Wall Line Width](../resolution/wall_line_width_0.md)--><!--if cura_version>=5.0-->[Minimum Odd Wall Line Width](min_odd_wall_line_width.md)<!--endif-->, discarding them as being too small to print.

If this setting is enabled, Cura will make an attempt at printing these pieces anyway. The resulting print will be inaccurate<!--if cura_version<5.0: and messy-->, but it should produce the desired shape somewhat reliably.

![Some parts are too thin to print](../images/fill_outline_gaps_disabled.png)
![With this setting enabled, even thin parts will get printed](../images/fill_outline_gaps_enabled.png)

<!--if cura_version<5.0:
The tiny pieces are filled with extremely thin lines. These lines are then combined if they are adjacent to one another and not too long. This works for many cases, but in some cases it produces a tiny zig zag, significantly increasing printing time.

It is advisable, before resorting to this setting, to try adjusting the outer wall line width slightly. If your part is slightly thinner than one line width, it might give a better result if you reduce the outer wall line width of your entire print such that the thin parts print normally. However reducing the line width too far will cause the material to flow unreliably, leading to underextrusion.
-->
<!--if cura_version>=5.0-->
Thin pieces are printed using a very thin wall line. However this thin line may not print well. To remedy that, there is also the [Minimum Thin Wall Line Width](min_bead_width.md). That setting provides a lower bound for the line width. If it's any thinner, the line will be printed too thick, theoretically printing beyond the bounds of the model, but at least it should print reliably. Anything thinner than the [Minimum Feature Size](min_feature_size.md) will not get printed at all.
<!--endif-->

**This will only attempt to print pieces that are thin in the horizontal plane. For thin pieces in the Z direction, see the [Slicing Tolerance](../experimental/slicing_tolerance.md) setting or reduce the layer height.**