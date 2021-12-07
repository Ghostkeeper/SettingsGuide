Linienabstand der Stützstruktur
====
Diese Einstellung definiert den Abstand zwischen zwei benachbarten Linien im Support-Muster. Diese Art der Anpassung der Stützdichte ist möglicherweise intuitiver als die Anpassung der Stützdichte, da sie direkt den Abstand anpasst, den die gestützten Linien überbrücken müssen.

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
![Großer Linienabstand](../../../articles/images/support_infill_rate_low.png)
![Geringer Leitungsabstand](../../../articles/images/support_infill_rate_high.png)

Die Verringerung des Abstands zwischen den Support-Linien hat einige positive und negative Auswirkungen. Hier sind einige der Auswirkungen, die es abzuwägen gilt:
* Die Oberfläche, die auf diesem Support aufliegt, wird weniger durchhängen, weil sie einen geringeren Abstand zwischen den beiden  Supports überbrücken muss.
* Der Support ist stabiler, was die Zuverlässigkeit des Drucks erhöht.
* Es ist schwieriger, den Support zu entfernen, da die Haftfläche größer ist.
* Es wird mehr Material benötigt, um den Support zu drucken.
* Der Druckvorgang dauert länger.