Blitz-Füllung Support-Winkel
====
Das Blitz-Füllung-Muster ist nur dazu gedacht, den Druck von innen zu unterstützen. Diese Einstellung bestimmt den maximalen Winkel des Überhangs, nicht nur der Oberflächen, die es unterstützt, sondern auch innerhalb der Füllung selbst. Wenn Sie diese Einstellung verringern, wird mehr Füllung erzeugt. Durch Erhöhen dieser Einstellung wird die Menge der Füllung verringert.

Das Muster unterstützt die Oberseite des Drucks von innen, aber nur die Oberseite, die deutlich mehr als dieser Winkel überhängt. Das Muster hat außerdem Endpunkte, die in einem bestimmten Winkel überhängen, um eine verzweigte Baumstruktur zu erzeugen, und die Seiten dieser verzweigten Struktur haben einen Innenwinkel, um weiter in bestimmte Bereiche hineinzureichen. Diese drei Aspekte des Überhangs können auch individuell mit den Einstellungen [Winkel für Überhänge der Blitz-Füllung](lightning_infill_overhang_angle.md), [Blitz-Füllung Stutzwinkel](lightning_infill_prune_angle.md) und [Blitz-Füllung begradigen](lightning_infill_straightening_angle.md) gesteuert werden.

<!--screenshot {
"image_path": "lightning_infill_support_angle_30.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "lightning_infill_support_angle_60.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 60
},
"colours": 64
}-->
![Bei einem geringen Überhangwinkel wird viel Support benötigt](../../../articles/images/lightning_infill_support_angle_30.png)
![Bei einem hohen Überhangwinkel sind steile Überhänge erlaubt](../../../articles/images/lightning_infill_support_angle_60.png)

Wenn Sie diese Einstellung erhöhen, wird die benötigte Materialmenge stark reduziert und die Druckzeit verkürzt. Allerdings führt dies auch zu einer Verformung. Diese Verformung befindet sich auf der Innenseite des Modells und ist daher nicht sofort sichtbar. Wenn jedoch die [Obere Dicke](../top_bottom/top_thickness.md) nicht ausreichend ist, kann es zu [pillowing](../troubleshooting/pillowing.md) kommen. Da auch die Innenwinkel in der Füllung mehr überhängen dürfen, ist es wahrscheinlich, dass die Füllung weiter oben an den Wänden beginnt.