Stütz-Brim aktivieren
====
Wenn der Support-Brim aktiviert ist, wird ein zusätzlicher Rand innerhalb des Support-Bereichs der ersten Schicht gezeichnet.

<!--screenshot {
"image_path": "support_brim_4mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
    "support_enable": true,
    "support_use_towers": false,
    "support_brim_enable": true,
    "support_brim_width": 4
},
"colours": 64
}-->
![Der Support-Brim](../../../articles/images/support_brim_4mm.png)

Der Support-Brim wird im Gegensatz zum normalen Brim nach *innen* gezogen. Wenn der [Druckplattenhaftungstyp](../platform_adhesion/adhesion_type.md) auf Brim gestellt ist, wird ein weiterer Rand *um* den Support gezeichnet.

Der Zweck dieses Brims ist es, dem Support mehr Fläche zu geben, auf der er an der Bauplatte haften kann. Dies kann auch durch Anpassen des [Linienabstand der ursprünglichen Stützstruktur](support_initial_layer_line_distance.md) erreicht werden, aber mit dieser Funktion wird die Haftung um den Rand des Support-Bereichs konzentriert, wo sie effektiver ist, um Warping zu verhindern.

Ein Support-Brim erhöht auch die Druckdauer und die Materialkosten geringfügig, aber da er sich nur auf der ersten Schicht befindet, ist dies sehr minimal. Der Support wird dadurch deutlich stabiler, so dass es für das Zickzackmuster des Supports schwieriger werden kann, abzubrechen.