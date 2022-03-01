Support Roof Extruder
====
If your printer has multiple extruders, the top side of the support, where the model rests on the support, can be printed with a different extruder than the floor of the support, where the support rests on the model. This setting allows you to choose which extruder is used for the support roof.

<!--screenshot {
"image_path": "support_roof_extruder_nr.png",
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
    "support_extruder_nr": 3,
    "support_roof_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![The support roof is printed in red, but the support floor in white](../images/support_roof_extruder_nr.png)

Some materials provide better overhang properties than other materials when used for support. For instance they might be able to print more closely to the surface because they don't chemically bond with the surface, or they are soluble in water. However such materials are often expensive and take longer to print. This setting allows you to print the support roof with a different extruder than the support floor. This way, the expensive or slow material is used sparingly but it is still effective at creating good overhangs.

The support roof is more important than the support floor for the quality of overhangs, so if an expensive material is to be used sparingly, it's best to use it at least for the support roof.