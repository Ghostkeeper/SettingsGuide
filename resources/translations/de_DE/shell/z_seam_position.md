Position der Z-Naht
====
Wenn die Position der Naht in der Einstellung [Justierung der Z-Naht](z_seam_type.md) auf "Benutzerdefiniert" gestellt ist, wird die Naht in der durch die Einstellung festgelegten Richtung platziert.

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
![Die Naht befindet sich auf der linken Seite](../../../articles/images/z_seam_x_left.png)
![Die Naht befindet sich auf der Rückseite](../../../articles/images/z_seam_y_back.png)
![Die Naht befindet sich auf der rechten Seite.](../../../articles/images/z_seam_x_right.png)
![Die Naht befindet sich auf der Vorderseite](../../../articles/images/z_seam_y_front.png)

Für die Position der Naht stehen acht verschiedene Richtungen zur Verfügung. Es ist am besten, eine Position für die Naht zu wählen, die im endgültigen Objekt schwer zu sehen ist, deshalb hängt es stark von der Gestaltung Ihres Modells ab. Normalerweise ist es am besten, eine Position der Naht zu wählen, die in einer Innenecke liegt, aber wenn eine solche Ecke nicht zur Verfügung steht, können Sie auch eine Position wählen, die sich nach dem Druck leicht mit einem Messer wegschneiden lässt.

**Die Naht wird so nah wie möglich an der Position platziert, die durch die Einstellungen [Z-Naht X](z_seam_x.md) und [Z-Naht Y](z_seam_y.md) angegeben ist. Dies ist eine einfache Einstellung, die die Koordinaten intuitiver festlegt.**