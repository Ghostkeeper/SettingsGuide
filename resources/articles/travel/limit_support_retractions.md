Limit Support Retractions
====
Instead of retracting when moving from one place to another to print support, this setting causes it to just travel directly without any retraction.

If enabled, the material will no longer be retracted when making a travel move from support to support in a straight line. When travelling to or from the actual print or when making a detour to avoid colliding with the actual print, the material will still be retracted.

Some effects of this setting in practice:
* It saves slightly on printing time, especially with soft materials that are difficult to retract.
* It prevents wearing down the material as much when printing soft materials. The feeder tends to wear down the filament if retracting too much on the same strip of filament, up to the point where it loses grip on the filament and your nozzle will print air for the rest of the print.
* It prevent interrupting the material flow with the retraction. Some materials, such as PVA, have trouble keeping the flow going so retracting is detrimental to their reliability. The nozzle may get clogged.
* There will be more oozing inside travel moves. This by itself just looks ugly but is harmless on support. However, all of the material that's being oozed will also result in underextrusion of the support being printed afterwards, which compromises the strength of the support.
* Through oozing, it will increase the chance for the formation of blobs on support. When hitting these blobs repeatedly, the support has a chance of falling over.