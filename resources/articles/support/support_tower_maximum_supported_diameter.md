Maximum Tower-Supported Diameter
====
This setting is a threshold for the diameter of a piece of overhang to choose between normal support and support towers. If the piece is thinner than this threshold, it'll get supported by a [support tower](support_use_towers.md). If it is wider than this threshold, it'll get supported by the ordinary support structures.

![The sword has an overhang area smaller than the minimum diameter](../images/support_use_towers.svg)

If a very thin strip of overhang needs support, normal support would topple over. Such support is too wonky to print properly. Instead, a more sturdy tower is generated.

Increasing this setting will cause towers to be generated more frequently. This increases the reliability of the support, but also requires slightly more material and printing time.
