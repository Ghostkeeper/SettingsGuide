Maximaler Winkel Außenhaut für Expansion
====
Da die Außenhaut im gesamten Modell vorhanden ist, ist es nicht notwendig, alle diese Bereiche zu erweitern. Vielmehr werden nur die Bereiche erweitert, in denen der Winkel zwischen der Oberfläche der Außenhaut und dem horizontalen Rand kleiner als diese Einstellung ist. Auf diese Weise werden flache Oberflächen mit hervorstehenden Elementen verstärkt, ohne die Druckzeit für den Rest des Modells unnötig zu verlängern.

<!--screenshot {
"image_path": "max_skin_angle_for_expansion_90.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "expand_skins_expand_distance": 3,
    "max_skin_angle_for_expansion": 90
},
"colours": 64
}-->
<!--screenshot {
"image_path": "max_skin_angle_for_expansion_45.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "expand_skins_expand_distance": 3,
    "max_skin_angle_for_expansion": 45
},
"colours": 64
}-->
![Bei einer Einstellung von 90 Grad wird die gesamte Außenhaut mit der Einstellung "Expansionsdistanz Außenhaut" erweitert.](../images/max_skin_angle_for_expansion_90.png)
![Bei einer Einstellung von 45 Grad werden nur die flachen Bereiche erweitert.](../images/max_skin_angle_for_expansion_45.png)

Die Erweiterung der Außenhaut ist nützlich, um die Verbindung zwischen der Ober- oder Unterseite des Drucks und den Wänden an den Seiten zu verstärken. Es kann jedoch auch die Druckzeit und den Materialverbrauch stark erhöhen. Mit dieser Einstellung können Sie das Material an den Seiten des Drucks weglassen, wo es für die Verstärkung der Verbindung zwischen Wänden und Außenhaut weniger nützlich ist.

Bei dieser Einstellung ist 0° horizontal. Bei einer Einstellung von 0° wird keine Außenhaut erweitert. Bei 90°, werden alle Bereiche der Außenhaut erweitert.