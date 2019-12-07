This setting directly adjusts the density of the spaghetti infill.

Normally, while printing infill, the [infill density](../infill/infill_sparse_density.md) setting only affects the [distance between infill lines](../infill/infill_line_distance.md). Because the [infill line width](../resolution/infill_line_width.md) is kept the same but the lines are spaced closer together, increasing the infill density has the effect that a greater portion of the infill volume gets filled with material in the end.

This works differently if [spaghetti infill](spaghetti_infill_enabled.md) is enabled. The infill line distance not only adjusts the distance between infill lines, but the line width will be adjusted as well in order to achieve the desired density as specified by this setting. This setting specifies exactly the fraction of the total infill volume that is going to get filled with material. Increasing this setting will cause the lines to become wider.

When using spaghetti infill to produce flexible infill, this setting essentially determines how stiff the infill material is going to be. Reducing the flow will produce softer infill, while increasing the flow will make the infill more stiff. However reducing the flow too much prevents the infill from being equally spread out. It will tend to fall down towards the bottom of the volume and produce piles of spaghetti there that don't add to the stiffness of the top. 

When using spaghetti infill to cast material, this setting should likely be set near 100% in order to fill up the model completely with material. However you may still adjust it slightly if your material has a tendency to shrink or expand as it sets.

**This setting is still multiplied by the [infill flow](../material/infill_material_flow.md) setting.**