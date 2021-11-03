Linienbreite der ersten Schicht
====
Dadurch werden die Linien der ersten Schicht in einem bestimmten Verhältnis breiter oder schmaler.

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
![Die Linien in der ersten Schicht sind doppelt so breit wie der Rest](../../../articles/images/initial_layer_line_width_factor.png)

Das Ziel dieser Einstellung ist es, die Haftung auf der Bauplatte zu verbessern. Um breitere Linien zu drucken, muss die Düse mehr Material extrudieren und dieses Material muss weiter nach außen fließen. Dadurch drückt die Düse das Material stärker auf die Bauplatte, was die Haftung zwischen dem Filament und der Bauplatte erhöht.
* Die Linien werden nicht nur breiter oder schmaler, sondern auch um den gleichen Faktor weiter auseinander oder näher beieinander liegen, so dass es nicht zu einer Über- oder Unterextrusion kommt.
* Diese Einstellung wirkt sich auf alle Linienbreiten aus: Außenhaut, Wände, Haftung, Stützstruktur, Einzugsturm und so weiter. Sie werden in demselben Verhältnis breiter oder schmaler gemacht.