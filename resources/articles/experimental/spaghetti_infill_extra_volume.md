Spaghetti Infill Extra Volume
====
With this setting, an extra amount of material will be extruded every time when printing infill. This is done at every step if the spaghetti infill is printed in [steps](spaghetti_infill_stepped.md), or once per vertical pillar of infill otherwise.

When using spaghetti infill for casting, this allows filling up a [sprue](https://en.wikipedia.org/wiki/Sprue_\(manufacturing\)) with material or to compensate for losses due to the starting and stopping mechanism.

When using spaghetti infill to create soft infill structures, this allows you to compensate for underextrusion due to the sudden flow change to a higher flow rate. There is no mechanism to compensate for the sudden drop in flow rate after printing infill though, so there will still be blobs on whatever is printed afterwards. 