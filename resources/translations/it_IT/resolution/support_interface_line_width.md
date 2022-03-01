Support Interface Line Width
====
The widths of the lines of support interface can be configured separately from the widths of the rest of the support lines.

<!--screenshot {
"image_path": "support_roof_line_width.png",
"models": [
    {
        "script": "trash_bin_lid.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [-47, 79, 110],
"settings": {
    "support_enable": true,
    "support_roof_enable": true,
    "support_roof_line_width": 0.8
},
"layer": 192,
"colours": 64
}-->
![The support interface lines are wider than the rest of the support lines](../images/support_roof_line_width.png)

Printing the support interface with slightly thinner lines is often advantageous for the quality of the overhanging surface that it supports, purely through having a smoother top surface above the support interface. Yet it doesn't necessarily increase the adhesion between the support interface and the model, so the support will not necessarily be harder to remove.

Similarly, the support floor will stick more evenly, reducing the scarring where the support was resting on the model without making support any weaker.

However, printing the interface lines too thin will cause uneven extrusion, which reduces the supporting effect of the interface, causing a worse overhang quality and less stable support. It may also introduce a great change in the flow rate through the nozzle, causing overextrusion when it starts printing support interface and underextrusion when printing whatever comes after the support interface.