This setting controls the maximum difference in layer height from the previous layer (in either direction).
This setting is meant to prevent print quality issues in cases where the algorithm would normally decide to increase or decrease the layer height significantly compared to the previous layer.
This sudden large change results in a large difference in material flow (because flow is based roughly on layer height times line width) which can cause over- or underextrusion.
The value determines the maximum distance that two layers' heights can deviate from one another.
