If this setting is enabled, the position where the printer will start with printing the infill on a layer will be randomised.

The start of the infill track is usually a bit weaker than the rest of the infill. This happens when the infill is printed faster, with thicker lines or has a greater layer height. The flow of material suddenly needs to speed up, and this doesn't happen instantaneously so there will be underextrusion for a short while. If this happens in the same location at every layer, this weakens the infill structure. The location where this happens will be the weakest link, and the infill around it will be subject to more strain. If the print is subjected to force, this is where it's more likely to break.

Normally the infill is started with the line that is closest to the position where the nozzle was when it starts with the infill, to reduce travel time. If this setting is enabled, that starting location is randomised instead. This will spread out the weak spots. There will not be one weakest link in the chain any more, and so the infill will be stronger in the end.

This does however increase the travel time slightly and lead to more oozing inside the model, since the distance to the starting location of the infill is no longer minimised.

**While the starting location is spread around randomly, it is still deterministic. Repeating the same slice twice should result in the same starting locations.**