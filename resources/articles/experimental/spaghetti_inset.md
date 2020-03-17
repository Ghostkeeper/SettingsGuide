Spaghetti Inset
====
To allow the spaghetti infill to expand in all directions equally, some distance must be kept from the walls. This setting determines that distance.

The behaviour of this setting is almost the same as that of the [infill overlap](../infill/infill_overlap_mm.md) setting. If the infill overlap is set to be the negative of this setting's value, the area that the nozzle will travel across will be the same. However, the difference is that the total volume extruded for the infill remains unchanged by this setting. Whereas reducing the infill overlap reduces the amount of material extruded as infill, adjusting this setting won't change the total volume extruded as infill.

When using spaghetti infill as a flexible infill pattern, this setting must be tuned such that the material doesn't hit the walls while travelling down, before it rests on the material. If the inset is too small, the spaghetti infill will just stick to the walls instead and produce big blobs of material there. If the inset is too big however, all of the material will be concentrated in the middle rather than adding equal amounts of strength on all sides.

When using spaghetti infill to cast with, this should be tuned to adjust for the wider casting nozzles that are typical for printers that are able to cast material, such that no material flows over the wall outside of the infill volume.