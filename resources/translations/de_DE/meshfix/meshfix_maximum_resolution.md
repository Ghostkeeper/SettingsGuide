Maximale Auflösung
====
Während Eingaben mit hoher Auflösung auf den ersten Blick besser erscheinen mögen, kommt der Drucker mit hochauflösendem G-Code oft nicht gut zurecht. Daher wird Cura die Auflösung der Eingabe während des Slicing-Prozesses reduzieren. Diese Einstellung bestimmt die Auflösung, die Cura als Maximum hält.

<!--screenshot {
"image_path": "meshfix_maximum_resolution_0.05.png",
"models": [{"script": "cylinder.scad"}],
"camera_position": [40, -20, 116],
"settings": {
    "meshfix_maximum_resolution": 0.05
},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_maximum_resolution_1.png",
"models": [{"script": "cylinder.scad"}],
"camera_position": [40, -20, 116],
"settings": {
    "meshfix_maximum_resolution": 4,
    "meshfix_maximum_deviation": 0.5
},
"colours": 64
}-->
![Vor der Reduzierung der Auflösung](../../../articles/images/meshfix_maximum_resolution_0.05.png)
![Nach Reduzierung der Auflösung (ad extremum)](../../../articles/images/meshfix_maximum_resolution_1.png)

Der Drucker muss den G-Code verarbeiten, während er ausgeführt wird. Wenn der G-Code viele kleine Zeilensegmente enthält, kann der Druckkopf so schnell durch die Bewegung rasen, dass der Prozessor des 3D-Druckers nicht mithalten kann. Dies hat zur Folge, dass der Druckkopf sporadisch langsamer wird, damit die CPU aufholen kann oder einfach nur auf den nächsten Bewegungsbefehl wartet. Dies führt dazu, dass die Oberfläche sehr rau wird oder sogar kleine Kleckse aufweist, weil die Flussrate aus der Düse nicht perfekt mit der sporadischen Bewegung der Düse übereinstimmt. Manchmal führt eine niedrigere Auflösung zu einer besseren Druckqualität.

Diese Einstellung gibt eine Mindestlänge für die Liniensegmente an. Liniensegmente, die kürzer als die angegebene Länge sind, werden zum Verbinden mit anderen Liniensegmenten in Betracht gezogen. Sie werden dann zusammengefügt, wenn der neue Pfad nicht mehr als die [Maximale Abweichung](meshfix_maximum_deviation.md) von seinem ursprünglichen Pfad abweicht.

Beachten Sie, dass es nicht garantiert ist, dass dieselben Eckpunkte aus jeder Schicht entfernt werden, wenn die Eckpunkte zufällig übereinstimmen. Die Auflösungsreduzierung wird in 2D durch das Entfernen von Eckpunkten der Formen der Schicht durchgeführt, nicht in 3D durch das Entfernen von Eckpunkten des Netzes. Folglich führt eine zu starke Reduzierung der Auflösung oft zu einer unregelmäßigen Oberfläche statt zu einer kantigen Oberfläche.

Es wird empfohlen, die Auflösung des Modells so weit zu verringern, dass der Druckkopf nicht wesentlich langsamer wird, damit die CPU den Rückstand aufholen kann. Wird die Auflösung nicht ausreichend reduziert, wird die Oberfläche rau, weil der Druckkopf seine Geschwindigkeit reduziert, während die Extrusion weiterläuft. Wenn die Auflösung zu stark reduziert wird, wird die Oberfläche auch dadurch rau, dass die Wände nicht überall exakt übereinander liegen.