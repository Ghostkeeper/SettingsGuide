Oberfläche Außenhaut Schichten
====
Ein Teil des oberen Teils des Drucks kann separiert und mit verschiedenen Einstellungen gedruckt werden. Diese Einstellung bestimmt, wie groß der Bereich ist, der separiert wird. Für wie viele Schichten des oberen Teils des Drucks werden separate Einstellungen vorgenommen?

<!--screenshot {
"image_path": "roofing_layer_count.png",
"models": [
    {
        "script": "question_stick_clip.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, -90, 60],
"settings": {
    "wall_line_count": 0,
    "skin_outline_count": 0,
    "roofing_layer_count": 1,
    "speed_roofing": 10,
    "cool_min_layer_time": 1,
    "roofing_extruder_nr": 1
},
"colour_scheme": "speed",
"colours": 32
}-->

![Die oberste Schicht der Außenhaut wird langsamer gedruckt (blau) als der Rest der Außenhaut (grün)](../../../articles/images/roofing_layer_count.png)

Einige Einstellungen können die Qualität der Oberseite des Drucks erheblich verbessern, sie können aber dazu führen, dass der Druck viel länger dauert, da sie auf alle Schichten der Außenhaut angewendet werden. Ein ähnlicher Effekt lässt sich erzielen, wenn diese Einstellungen nur für die oberste Schicht oder zwei Schichten vorgenommen, die restlichen Schichten der Außenhaut aber schneller gedruckt werden. Dies hat dann keine so großen negativen Auswirkungen auf die Druckzeit.

Folgende Einstellungen können für die Oberseite vorgenommen werden:
* [Oberfläche Außenhaut Extruder](roofing_extruder_nr.md)
* [Fluss Oberfläche Außenhaut](../material/roofing_material_flow.md)
* [Oberfläche Außenhaut Geschwindigkeit](../speed/speed_roofing.md)
* [Beschleunigung Oberfläche Außenhaut](../speed/acceleration_roofing.md)
* [Justierung der Oberfläche Außenhaut](../speed/jerk_roofing.md)
* [Oberfläche Außenhaut Linienbreite](../experimental/roofing_line_width.md)
* [Oberfläche Außenhaut Muster](../experimental/roofing_pattern.md)
* [Linienrichtungen der Oberfläche Außenhaut](../experimental/roofing_angles.md)

Um eine schönere Oberfläche zu erhalten, versuchen Sie, die Geschwindigkeit zu verringern und den Ruck (Jerk) zu erhöhen.

Wenn Sie die Außenhaut in einer anderen Farbe drucken (unter Verwendung der Einstellung [Oberfläche Außenhaut Extruder](roofing_extruder_nr.md)), ist es oft notwendig, mehr als eine Schicht in der anderen Farbe zu drucken. Andernfalls würde die ursprüngliche Farbe noch durchscheinen.