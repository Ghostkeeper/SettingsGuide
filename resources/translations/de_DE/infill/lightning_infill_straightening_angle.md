Blitz-Füllung begradigen
====
Diese Einstellung legt fest, wie steil das Blitz-Füllmuster nach innen überhängen darf.

Die Blitz-Füllung erzeugt die namensgebenden blitzartigen Zickzack-Linien dort, wo sie den oberen Teil des Drucks unterstützen muss, diese brauchen aber wegen der scharfen Ecken in den Linien sehr lange zum Drucken. Daher wird unten versucht, diese gezackten Linien zu begradigen, um die Druckzeit zu verkürzen. Diese Begradigung führt zu Überhängen. Die Einstellung bestimmt, wie viel Überhang zulässig ist.

<!--screenshot {
"image_path": "lightning_infill_straightening_angle_40.png",
"models": [
    {
        "script": "cylinder.scad",
        "transformation": ["scaleZ(0.5)"]
    }
],
"camera_position": [36, 44, 19],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 40,
    "lightning_infill_prune_angle": 10,
    "lightning_infill_straightening_angle": 40
},
"colours": 32
}-->
<!--screenshot {
"image_path": "lightning_infill_straightening_angle_10.png",
"models": [
    {
        "script": "cylinder.scad",
        "transformation": ["scaleZ(0.5)"]
    }
],
"camera_position": [36, 44, 19],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 40,
    "lightning_infill_prune_angle": 10,
    "lightning_infill_straightening_angle": 10
},
"colours": 32
}-->
![Bei 40° konvergieren die Ausfülllinien schnell zu geraden Linien](../../../articles/images/lightning_infill_straightening_angle_40.png)
![Bei 10° gibt es keine steilen Überhänge mehr in der Füllung](../../../articles/images/lightning_infill_straightening_angle_10.png)

Schnelles Begradigen (erhöhter Überhang) verkürzt zwar die Druckzeit etwas, verringert aber auch die Zuverlässigkeit des Drucks, insbesondere bei dünner Linienbreite. Wenn der Überhang zu steil ist, führt dies zu einer Spaltung der Schicht. Der Spalt befindet sich auf der Innenseite des Drucks und stellt oft kein Problem dar, aber er kann dazu führen, dass dieser Teil der Füllung vollständig ausfällt, wodurch ein Teil der Oberseite nicht mehr gestützt wird. Dies wird dann als unebener Bereich oder als pillowing auf der Oberseite sichtbar, im schlimmsten Fall sogar als Wirrwarr aus geschmolzenem Kunststoff.