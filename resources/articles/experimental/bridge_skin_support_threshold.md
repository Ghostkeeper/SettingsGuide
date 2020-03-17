Bridge Skin Support Threshold
====
This setting allows you to adjust how sensitive the detection of bridging areas will be. Bridging areas are detected by virtue of the portion of the skin's area that is supported by something in the previous layer.

For each disjunct region of skin, this will look how much of that skin is supported by anything in the layer below. If the region is supported too little, then the bridging technique will be applied to the regions of the skin that are not supported.

Applying the bridge technique to skin brings about changes in flow rate and printing speed. These try to adjust the rate at which material is poured out the nozzle, but that tends to be hard to change. As a result, there will be overextrusion in some parts of the print and underextrusion in other parts, as the flow rate attempts to adjust itself. So adjusting the flow rate for a very small piece of overhang will more than likely reduce the print quality instead of improving it.

Increasing this setting will cause the bridging technique to be applied to more smaller parts of overhang, where the bridging is less effective but the flow rate is still interrupted. Reducing this setting will cause the bridging technique to only be applied in very large overhanging areas. This will not cause as many flow changes, but may reduce the quality of overhang for smaller overhang areas.