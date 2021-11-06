Z-Naht X
====
Wenn die Position der Naht in der Einstellung [Justierung der Z-Naht](z_seam_type.md) auf "Benutzerdefiniert" eingestellt ist, wird die Naht in der Nähe der mit den Einstellungen Z-Naht X und [Z-Naht Y](z_seam_y.md) festgelegten Position platziert.

<!--screenshot {
"image_path": "z_seam_x_left.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [-55, 128, 40],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "left"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_x_right.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [55, 128, 40],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "right"
},
"colours": 64
}-->
![Die Naht befindet sich auf der linken Seite](../../../articles/images/z_seam_x_left.png)
![Die Naht befindet sich auf der rechten Seite.](../../../articles/images/z_seam_x_right.png)

Diese Einstellung gibt eine absolute Position auf der Bauplatte an, wenn [Realitvwert der Z-Naht](z_seam_relative.md) deaktiviert ist, oder eine Position relativ zur Mitte des Modells, wenn Realitvwert der Z-Naht aktiviert ist. Wenn die Position absolut ist, ist die Koordinate im g-code Koordinatensystem, das sich von den Koordinaten unterscheidet, die Cura für die Platzierung von Objekten anzeigt.

Es ist sinnvoll, eine Stelle für die Naht zu wählen, die in der Anwendung Ihres Drucks kaum sichtbar ist. Wenn keine solche Stelle zur Verfügung steht oder nach dem Druck nachbearbeitet werden kann, können Sie die Naht an einer Stelle platzieren, an der sie leicht mit einem Messer abgeschnitten oder abgeschliffen werden kann.