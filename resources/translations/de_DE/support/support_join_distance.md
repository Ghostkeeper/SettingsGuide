Abstand für Zusammenführung der Stützstrukturen
====
Dünne Supports sind im Allgemeinen nicht erwünscht. Sie neigen dazu, umzukippen, was den Druck ruinieren kann. Wenn mehrere Teile des Supports nebeneinander liegen, können sie miteinander verbunden werden und bilden dann ein einzelnes Support-Stück, das viel stabiler ist.

<!--screenshot {
"image_path": "support_join_distance_low.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 150, 75],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_join_distance": 0.1
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_join_distance_high.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 150, 75],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_join_distance": 2
},
"colours": 64
}-->
![Zwei Teile des Supports liegen dicht beieinander](../../../articles/images/support_join_distance_low.png)
![Bei ausreichendem Abstand werden sie zusammengeführt.](../../../articles/images/support_join_distance_high.png)

Das Zusammenfügen von Support-Teilen macht den Support stabiler und zuverlässiger. Außerdem verkürzt sich dadurch die Druckzeit, je nach Muster. Bei vielen Mustern muss eine zusätzliche Wand um den gesamten Umfang oder einen Teil des Umfangs herum gedruckt werden, und das Zusammenfügen von zwei Support-Teilen verringert diesen Umfang.

Wenn Sie diese Einstellung zu stark erhöhen, kann dies dazu führen, dass Support-Teile, die sehr weit voneinander entfernt sind, miteinander verbunden werden. Dies kann die Druckzeit und den Materialverbrauch erhöhen.