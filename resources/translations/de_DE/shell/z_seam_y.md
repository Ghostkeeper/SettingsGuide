Z-Naht Y
====
Wenn die Position der Naht in der Einstellung [Justierung der Z-Naht](z_seam_type.md) auf "Benutzerdefiniert" eingestellt ist, wird die Naht nahe der mit den Einstellungen [Z-Naht X](z_seam_x.md) und Z-Naht Y festgelegten Position platziert.

<!--screenshot {
"image_path": "z_seam_y_back.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [0, -77, 130],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "back"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_y_front.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [0, 77, 130],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "front"
},
"colours": 64
}-->
![Die Naht befindet sich auf der Vorderseite](../../../articles/images/z_seam_y_front.png)
![Die Naht befindet sich auf der Rückseite](../../../articles/images/z_seam_y_back.png)

Diese Einstellung gibt eine absolute Position auf der Bauplatte an, wenn [Realitvwert der Z-Naht](z_seam_relative.md) deaktiviert ist, oder eine Position relativ zur Mitte des Modells, wenn Realitvwert der Z-Naht aktiviert ist. Wenn die Position absolut ist, ist die Koordinate im g-code Koordinatensystem, das sich von den Koordinaten unterscheidet, die Cura für die Platzierung von Objekten anzeigt.

Es ist sinnvoll, eine Stelle für die Naht zu wählen, die in der Anwendung Ihres Drucks kaum sichtbar ist. Wenn keine solche Stelle zur Verfügung steht oder nach dem Druck nachbearbeitet werden kann, können Sie die Naht an einer Stelle platzieren, an der sie leicht mit einem Messer abgeschnitten oder abgeschliffen werden kann.