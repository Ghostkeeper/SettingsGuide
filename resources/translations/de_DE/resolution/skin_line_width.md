Breite der oberen/unteren Linie
====
Die Breite der Linie auf der Ober- und Unterseite. Die Breite einer Linie kann von der Düsengröße abweichen, indem einfach mehr oder weniger Material als nötig extrudiert wird. Wenn mehr Material extrudiert wird, fließt der Kunststoff zu den Seiten, wodurch die Linie dicker wird. Wird weniger Material extrudiert, zieht die Oberflächenspannung des Materials das Material in Richtung der Mittellinie des Düsenwegs.

<!--screenshot {
"image_path": "skin_line_width.png",
"models": [
    {
        "script": "flipper_grip.scad",
        "transformation": ["scale(0.6)"]
    }
],
"camera_position": [0, 37, 107],
"settings": {"skin_line_width": 0.8},
"layer": 300,
"colours": 64
}-->
![Die oberen/unteren Linie sind deutlich breiter als der Rest](../../../articles/images/skin_line_width.png)

Die oberen/unteren Linie breiter zu machen, ist eine einfache Möglichkeit, die Druckzeit zu verkürzen, da weniger Linien erforderlich sind, um die Ober- und Unterseite des Objekts zu drucken. Eine zu starke Vergrößerung kann jedoch zu großen Extrusionsschwankungen führen. Dies führt zu einer Unterextrusion beim Druck der oberen/unteren Linie und einer Überextrusion beim Druck des nächsten Teils, da sich der Fluss durch die Düse nicht schnell genug anpassen kann. Wenn Sie die Breite der oberen/unteren Linie erhöhen, erhöht sich auch die Wahrscheinlichkeit, dass Löcher in der Oberfläche entstehen, was nicht schön ist und verhindert, dass sie wasserdicht ist.

Eine Verringerung der Breite der oberen/unteren Linie führt in der Regel zu einer schöneren Oberseite, allerdings auf Kosten der Druckzeit. Es ist oft effektiver, eine andere Technik wie [Glätten](../top_bottom/ironing_enabled.md) zu verwenden oder nur die [Oberfläche Außenhaut Linien](../top_bottom/roofing_line_width.md) anzupassen.