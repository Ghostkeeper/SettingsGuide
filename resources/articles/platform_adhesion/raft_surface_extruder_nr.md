Raft Top Extruder
====
This setting selects the extruder to use to print the top layers of the raft.

![Where the top layers are located in the raft](../images/raft_dimensions_simplified.svg)

The top layers are resting on top of the middle layers, and provide a bedding for the actual print. It is good to use a material that sticks well to the middle layer, but the adhesion with the model should be carefully tuned using the [Raft Air Gap](raft_airgap.md) setting. If the material used for the top layers doesn't stick well to the model, the adhesion must be improved by reducing the air gap, and vice versa. If the model sticks too well it won't come loose after the print, but if it doesn't stick well enough it might get loose during the print. 