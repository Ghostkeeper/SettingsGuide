Small areas of overhanging surfaces produce small pillars of support. These pillars are prone to topple over. Instead of those small pillars, Cura can generate specialised towers that are wider and more sturdy, to prevent the support from falling over.

![A tower supports the sword which would otherwise have a very small overhanging area](../images/support_use_towers.svg)

Overhang areas smaller than the [Minimum Tower-Supported Diameter](support_minimal_diameter.md) will get supported by such a tower instead of the normal support structure. These towers are wider so that they won't topple over. Near the top of the tower, the tower will get more narrow towards the width of the overhanging surface that actually needs support.

These towers have a larger diameter than the region they support. This makes the towers more stable than regular support, but also requires more material, printing time and space on your build plate.