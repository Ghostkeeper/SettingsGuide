Maximaler Winkel des Modells
====
Mit dieser Einstellung wird der Überhangswinkel (in Grad) konfiguriert, der erzeugt wird, um [den Überhang druckbar zu machen](conical_overhang_enabled.md). Eine Vergrößerung dieses Winkels erlaubt einen größeren Überhang, was Cura dazu veranlasst, das Modell weniger zu verändern. Verringert man diesen Winkel, hat das Objekt kaum noch einen Überhang.

<!--screenshot {
"image_path": "conical_overhang_enabled_enabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
    "conical_overhang_enabled": true,
    "conical_overhang_angle": 50
},
"colours": 8
}-->
<!--screenshot {
"image_path": "conical_overhang_angle_20.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
    "conical_overhang_enabled": true,
    "conical_overhang_angle": 20
},
"colours": 8
}-->
![Ein maximaler Modellwinkel von 50°](../../../articles/images/conical_overhang_enabled_enabled.png)
![Ein maximaler Modellwinkel von 20°](../../../articles/images/conical_overhang_angle_20.png)

Bei einem Winkel von 90° bleibt das Modell so, wie es war, mit all seinen Überhängen. Das Modell wird nicht verändert. Bei einem Winkel von 0° werden alle Schrägen vollständig vertikal.

Durch Verkleinern dieses Winkels wird der Überhang des Modells verringert. Dadurch lässt sich das Modell besser drucken. Es hängt nicht mehr so stark durch, und die Oberfläche an den Unterseiten wird glatter. Allerdings entspricht das gedruckte Objekt dann nicht mehr so genau dem Originalmodell. Außerdem wird etwas mehr Zeit und Material benötigt, um es zu drucken.

Der Winkel kann auch negativ sein. Dadurch wird der gesamte Druck kegelförmig und hat eine breite Basis. Dies kann zu interessanten Effekten führen, hat aber keinen wirklichen praktischen Nutzen.