Initial Layer Line Width
====
This makes the lines in the initial layer wider or thinner by a certain ratio.

<!--screenshot {
"image_path": "initial_layer_line_width_factor.png",
"models": [{"script": "hex_foot.scad"}],
"camera_position": [0, 92, 122],
"settings": {
    "adhesion_type": "brim",
    "initial_layer_line_width_factor": 200
},
"colours": 32
}-->
![The lines in the initial layer are twice as wide as the rest](../images/initial_layer_line_width_factor.png)

The goal of this setting is to improve adhesion to the build plate. In order to print wider lines, the nozzle has to extrude more material and that material has to flow wider outward. This causes the nozzle to press the material harder on the build plate, which increases adhesion between the filament and the build plate.
* Not only will the lines be wider or thinner, but they will also be farther apart or closer together by the same factor, so it would not produce overextrusion or underextrusion.
* This setting affects all line widths; skin, walls, adhesion, support, the prime tower, and so on. They will be made wider or thinner by the same ratio.