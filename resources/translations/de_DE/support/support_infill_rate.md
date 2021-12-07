Dichte der Stützstruktur
====
Diese Einstellung bestimmt die Geschwindigkeit, mit der die Support-Strukturen mit Material gefüllt werden. Bei großen Füllungsraten werden die Support-Linien sehr nah beieinander platziert. Bei geringen Füllungsraten werden die Linien weiter auseinander platziert.

<!--screenshot {
"image_path": "support_infill_rate_low.png",
"models": [{"script": "spiral_stair.scad"}],
"camera_position": [-95, 18, 116],
"settings": {
    "support_enable": true,
    "support_infill_rate": 10
},
"layer": 256,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_rate_high.png",
"models": [{"script": "spiral_stair.scad"}],
"camera_position": [-95, 18, 116],
"settings": {
    "support_enable": true,
    "support_infill_rate": 20
},
"layer": 256,
"colours": 64
}-->
![Geringe Support-Dichte](../../../articles/images/support_infill_rate_low.png)
![Hohe Support-Dichte](../../../articles/images/support_infill_rate_high.png)

Die Erhöhung der Support-Dichte hat positive und negative Auswirkungen. Hier sind einige der Auswirkungen, die es abzuwägen gilt:
* Da der Abstand zwischen den Support-Linien geringer ist, wird die Oberfläche, die auf diesem Support ruht, weniger durchhängen.
* Der Support ist stabiler, was die Zuverlässigkeit des Drucks erhöht.
* Es ist schwieriger, den Support zu entfernen, da die Haftfläche größer ist.
* Es wird mehr Material benötigt, um den Support zu drucken.
* Der Druckvorgang dauert länger.