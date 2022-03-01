First Layer Support Extruder
====
If your printer has multiple extruders, the layer of support that rests on the build plate can be printed with a different extruder than the rest of the support. This setting allows you to choose which extruder is used for the initial layer of support.

<!--screenshot {
"image_path": "support_extruder_nr_layer_0.png",
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
    "support_extruder_nr_layer_0": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![The initial layer of the support is printed in red, but the rest in white](../images/support_extruder_nr_layer_0.png)

Some materials are better suited for printing support than others. These are often inert materials that don't stick well to other materials, so they can be removed more easily. However this property is not desirable for sticking to the build plate. A material that sticks better to the build plate can then be used for the first layer, to which the normal support material can stick better than to glass or aluminium.