Wipe Z Hop
====
With this setting, the wiping procedure will be done while Z hopped. This can be configured separately from the ordinary [Z hops](../travel/retraction_hop_enabled.md).

The wipe procedure contains two very long travel moves that go all the way to the side of the build volume. During these travel moves, the print head may pick up quite some speed because it has a lot of time to accelerate. At great speeds, there is an increased chance of the print head accidentally knocking over previously printed parts. Therefore you may want to enable Z hops even if you wouldn't do that for the ordinary printing process.

The Z hop in this procedure is executed regardless of whether [Z hops are only performed over previously printed parts](../travel/retraction_hop_only_when_collides.md) or whether there are printed parts in between.