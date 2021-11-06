Außenwandüberlappungen ausgleichen
====
Beim Druck von sehr dünnen Teilen können die gegenüberliegenden Außenwände so nahe beieinander liegen, dass sie sich überlappen. Würden beide Wände mit ihrer normalen Linienbreite gedruckt, würden sie überextrudieren. Diese Einstellung verhindert diese Überextrusion, indem sie die Breite einer der Linien reduziert, wodurch diese Überextrusion verhindert und eine bessere Maßgenauigkeit erreicht wird.

<!--screenshot {
"image_path": "travel_compensate_overlapping_walls_enabled_disabled.png",
"models": [
    {
        "script": "text.scad",
        "scad_params": ["content=\"Part\""],
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 20],
"settings": {"travel_compensate_overlapping_walls_0_enabled": false},
"colours": 16
}-->
<!--screenshot {
"image_path": "travel_compensate_overlapping_walls_enabled_enabled.png",
"models": [
    {
        "script": "text.scad",
        "scad_params": ["content=\"Part\""],
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 20],
"settings": {"travel_compensate_overlapping_walls_0_enabled": true},
"colours": 16
}-->
![Wo die Linienbreite reduziert wird](../../../articles/images/travel_compensate_overlapping_walls_enabled_schematic.svg)
![Alle Linien werden mit ihrer vollen Breite extrudiert, wodurch ein zu breites Teil entsteht.](../../../articles/images/travel_compensate_overlapping_walls_enabled_disabled.png)
![Die Hälfte der Linien wurde in ihrer Breite reduziert, was zu einem genaueren Druck führt.](../../../articles/images/travel_compensate_overlapping_walls_enabled_enabled.png)

Die Linienbreite der Außenwand, die eine andere Außenwand überlappt, wird um die Überlappungsfläche reduziert. Dadurch wird die Überextrusion kompensiert.

Wie oben beschrieben, wird dadurch die Maßhaltigkeit tendenziell verbessert. Der Nachteil ist jedoch, dass die Fließgeschwindigkeit ungleichmäßiger wird, was an einigen Stellen zu Unterextrusion und an anderen zu Überextrusion führt. Außerdem kann die Durchflussmenge unter die Mindestdurchflussmenge der Düse und der Extrudereinstellung sinken, was zu ungleichmäßigem Fluss und Tropfenbildung führt. Um diesen Effekt zu verringern, können Sie den [Mindestwandfluss](wall_min_flow.md) einstellen, der einige der dünnsten Wände zu Fahrwegen auf Kosten der Maßhaltigkeit macht.

**Diese Einstellung sieht in der Schichtansicht eher unschön aus. Im tatsächlichen Druck gibt es keine Grenzen zwischen den Linien. In der Schichtansicht werden nur die Pfade des G-Codes angezeigt, aber in Wirklichkeit wird das Material von der anderen Wand, mit der es sich überlappt, zur Seite geschoben. Auch winzige Verringerungen des Durchflusses machen sich im tatsächlichen Druck nicht bemerkbar, da sich die Durchflussrate durch die Düse nicht so schnell anpassen kann. Diese Effekte führen dazu, dass der tatsächliche Druck glatter ausfällt, als es in der Schichtansicht dargestellt wird.**