Extruder für erste Schicht der Stützstruktur
====
Wenn Ihr Drucker mit mehreren Extrudern ausgestattet ist, kann die Schicht des Supports, die auf der Bauplatte aufliegt, mit einem anderen Extruder gedruckt werden als der Rest des Supports. Mit dieser Einstellung können Sie wählen, welcher Extruder für die erste Schicht des Supports verwendet werden soll.

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
![Die erste Schicht des Supports wird in Rot gedruckt, der Rest in Weiß.](../../../articles/images/support_extruder_nr_layer_0.png)

Einige Materialien eignen sich besser zum Drucken von Support als andere. Dabei handelt es sich oft um inerte Materialien, die nicht gut an anderen Materialien haften und sich daher leichter entfernen lassen. Diese Eigenschaft ist jedoch für die Haftung auf der Bauplatte nicht erwünscht. Für die erste Schicht kann dann ein Material verwendet werden, das besser auf der Bauplatte haftet und an dem das normale Support-Material besser haften kann als an Glas oder Aluminium.