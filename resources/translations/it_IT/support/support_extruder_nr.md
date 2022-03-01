Support Extruder
====
If your printer has multiple extruders, this setting allows you to choose which of these extruders is used to print the support structure with.

<!--screenshot {
"image_path": "support_extruder_nr.png",
"models": [
    {
        "script": "question_stick_clip.scad",
        "transformation": ["rotateY(90)"],
        "object_settings": {"extruder_nr": 1}
    }
],
"camera_position": [134, 134, 113],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_use_towers": false,
    "support_extruder_nr": 3
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![The support is printed in a white material, while the model is printed in blue](../images/support_extruder_nr.png)

Using a different type of material tends to make the support easier to remove without compromising the strength of the support. Different material types don't adhere very well to each other, especially if they have different shrinkage rates.

Also, some materials are designed to print support with. They can be made extremely brittle on purpose, for instance, so that they break off more easily. Some materials dissolve in water or in ethanol, so that you can remove support even if it's printed very closely to the model.

Printing support with a different extruder than the rest of the model requires the printer to switch materials at every layer though, which could increase printing time. If the support material has a different colour than the build material, the residue of support on the print could be very visible.