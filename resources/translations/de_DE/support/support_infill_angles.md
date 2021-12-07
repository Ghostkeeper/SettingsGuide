Unterstützung Linienrichtung Füllung
====
Das Support-Muster ist normalerweise so ausgerichtet, dass die Linien senkrecht zu den meisten Dingen verlaufen, die es unterstützt. Auf diese Weise wird der Abstand, den das unterstützte Material zu überbrücken hat, minimiert. Mit dieser Einstellung kann die Ausrichtung der Support-Linien individuell angepasst werden.

<!--screenshot {
"image_path": "support_infill_angle_0.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_infill_angles": [0]
},
"layer": 160,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_angle_30.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_infill_angles": [30]
},
"layer": 160,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_angles.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_infill_angles": [30, 60]
},
"layer": 160,
"colours": 64
}-->
![Ein Winkel von 0°](../../../articles/images/support_infill_angle_0.png)
![Abwechselnd zwischen 30° und 60°](../../../articles/images/support_infill_angles.png)

Mit dieser Einstellung können mehrere Winkel eingegeben werden, die durch Kommas getrennt sind. Wenn mehrere Winkel eingegeben werden, wechselt Cura zwischen diesen Winkeln in den Schichten.

Wenn die [Richtungen der oberen/unteren Linie](../top_bottom/skin_angles.md) angepasst wurden, ist es ratsam, den Winkel des Supports auch entsprechend anzupassen, so dass er senkrecht zu den Linien der Unterseite des Drucks ausgerichtet bleibt. Dadurch liegen die unteren Linien richtig auf dem Support auf und fallen nicht zwischen die Support-Linien. Dies ist besonders wichtig bei Linien und Zickzack-[Stützstrukturmustern](support_pattern.md), bei denen lange Geraden zwischen den Support-Linien liegen, die keinen Support bieten.
