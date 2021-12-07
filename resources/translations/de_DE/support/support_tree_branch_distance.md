Astabstand der Baumstützstruktur
====
Diese Einstellung legt den Abstand zwischen zwei benachbarten Ästen fest, bei dem die Äste die Bauplatte berühren.

<!--screenshot {
"image_path": "support_tree_branch_distance_1_4.png",
"models": [
    {
        "script": "gutter_lift.scad",
        "transformation": ["scale(0.5)", "rotateZ(-90)"]
    }
],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_distance": 1.4
},
"minimum_layer": 1310,
"layer": 1311,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_tree_branch_distance_5.png",
"models": [
    {
        "script": "gutter_lift.scad",
        "transformation": ["scale(0.5)", "rotateZ(-90)"]
    }
],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_distance": 5
},
"minimum_layer": 1310,
"layer": 1311,
"colours": 64
}-->
![Äste im Abstand von 1,4 mm](../../../articles/images/support_tree_branch_distance_1_4.png)
![Äste im Abstand von 5 mm](../../../articles/images/support_tree_branch_distance_5.png)

Um das Modell zu unterstützen, platziert die Baumstützstruktur Kontaktpunkte unter dem Modell in einem versetzten Gittermuster. Diese Einstellung bestimmt im Wesentlichen die Größe dieses Rasters und damit den Abstand der Äste. Aufgrund der Ausrichtung der Äste in Bezug auf die (voreingestellte) Richtung der Außenhautlinien wird der Abstand, den die Außenhautlinien überbrücken müssen, höchstwahrscheinlich größer sein als dieser Abstand.

Durch die Verringerung des Abstands zwischen den Ästen kann eine bessere Qualität des Überhangs erreicht werden, da die Linien, die auf der Stütze aufliegen, nicht so weit überbrücken müssen. Der Support wird auch steifer, weil mehr Material für den oberen Teil des Supports verwendet wird, was den Druck zuverlässiger macht.

Eine Verringerung des Abstands zwischen den Ästen führt jedoch auch dazu, dass der Support mehr Material verbraucht und mehr Zeit zum Drucken benötigt.

Wird der Abstand der Äste unter den [Astdurchmesser der Baumstützstruktur](support_tree_branch_diameter.md) verringert, verschmelzen die Äste, bevor sie richtig geformt werden konnten. Dies kann dazu führen, dass die Mitte großer überhängender Bereiche nicht mehr richtig unterstützt wird.