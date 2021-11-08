Winkel für Überhänge der Blitz-Füllung
====
Die Füllung "Blitz" unterstützt nur die Oberseite des Modells von innen, und zwar dort, wo sie überhängt. Diese Einstellung bestimmt den Winkel des Überhangs, der von der Innenseite des Modells durch den Blitz unterstützt wird.

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
"image_path": "lightning_infill_overhang_angle_70.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 30,
    "lightning_infill_overhang_angle": 70
},
"colours": 64
}-->
![Überhang von bis zu 30° wird nicht gestützt](../../../articles/images/lightning_infill_support_angle_30.png)
![Bis zu 70° ist nicht gestützt, so dass nur der oberste Teil der Kugel gestützt wird.](../../../articles/images/lightning_infill_overhang_angle_70.png)

Eine Vergrößerung des Winkels verringert die Menge der erzeugten Füllung. Die Oberseite wird weniger gestützt, wenn es sich nicht um einen sehr steilen Überhang handelt. Dies spart Zeit und Material, kann aber auch dazu führen, dass die Oberseite an einigen Stellen durchhängt. Das Ergebnis könnte [Pillowing](../troubleshooting/pillowing.md) oder eine allgemein rauere Oberfläche sein.

Im Gegensatz zu der übergeordneten Einstellung [Blitz Füllung Support-Winkel](lightning_infill_support_angle.md) beeinflusst diese Einstellung nicht den Überhang im Füllmuster selbst.
