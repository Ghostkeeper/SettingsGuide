Bridge Sparse Infill Max Density
====
If you're printing with a very low infill density, the top skin tends to sag, causing [pillowing](../troubleshooting/pillowing.md) and just generally irregular surfaces on the top side of the print. Optionally, the bridging techniques can be applied to the top skin as well. This setting configures at what infill rate the bridging technique will start being applied.

<!--screenshot {
"image_path": "bridge_sparse_infill_max_density.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"layer": 108,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_sparse_infill_max_density": 100
},
"camera_position": [58, 27, 104],
"colours": 64
}-->
![The skin is bridging over the infill](../images/bridge_sparse_infill_max_density.png)

This setting is configured as a threshold, in order to allow profiles to contain a single value. While the user adjusts the infill density all the time, the bridging for skin will automatically be enabled or disabled.

Bridging for the top skin generally produces a smoother top surface at very low infill rates. However do make sure that if this is used, there are enough [top layers](../top_bottom/top_layers.md) to properly close the surface without applying the bridging technique on the highest layers. The bridging technique, especially with reduced [line width](bridge_skin_material_flow_3.md) will not close the surface completely. If the top skin doesn't have enough layers, you'll end up with holes in the print and compromised strength.