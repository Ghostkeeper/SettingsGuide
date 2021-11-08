Innenwandüberlappungen ausgleichen
====
Beim Druck von sehr dünnen Teilen können die gegenüberliegenden Wände so nahe beieinander liegen, dass sie sich überlappen. Würden beide Wände mit ihrer normalen Linienbreite gedruckt, würden sie überextrudieren. Diese Einstellung verhindert diese Überextrusion, indem sie die Breite einer der Linien reduziert, wodurch diese Überextrusion verhindert und eine bessere Maßgenauigkeit erreicht wird.

<!--screenshot {
"image_path": "travel_compensate_overlapping_walls_x_enabled_disabled.png",
"models": [
    {
        "script": "moon_sickle.scad",
        "transformation": ["rotateZ(90)"]
    }
],
"camera_position": [0, 0, 45],
"settings": {
    "wall_line_count": 99,
    "travel_compensate_overlapping_walls_0_enabled": false,
    "travel_compensate_overlapping_walls_x_enabled": false
},
"layer": 23,
"colours": 128
}-->
<!--screenshot {
"image_path": "travel_compensate_overlapping_walls_x_enabled_enabled.png",
"models": [
    {
        "script": "moon_sickle.scad",
        "transformation": ["rotateZ(90)"]
    }
],
"camera_position": [0, 0, 45],
"settings": {
    "wall_line_count": 99,
    "travel_compensate_overlapping_walls_0_enabled": false,
    "travel_compensate_overlapping_walls_x_enabled": true
},
"layer": 23,
"colours": 128
}-->
![Alle Linien werden mit ihrer vollen Breite extrudiert, wodurch ein zu breites Teil entsteht.](../../../articles/images/travel_compensate_overlapping_walls_x_enabled_disabled.png)
![Die Hälfte der Linien wurde in ihrer Breite reduziert, was zu einem genaueren Druck führt.](../../../articles/images/travel_compensate_overlapping_walls_x_enabled_enabled.png)

Diese Einstellung gilt nur für die Innenwände. Die Kompensation der Überlappung in den Innenwänden ist auf der Außenseite weniger sichtbar, da weniger Artefakte der Fließgeschwindigkeitsänderungen sichtbar werden, aber sie trägt dennoch genauso stark zur Verringerung des Effekts der Überextrusion bei, da die Innenwände weniger nach außen gedrückt werden.

Die Linienbreite der Wand, die eine andere Wand überlappt, wird um die Überlappungsfläche reduziert. Dadurch wird die Überextrusion kompensiert.

Wie oben beschrieben, wird dadurch die Maßhaltigkeit tendenziell verbessert. Der Nachteil ist jedoch, dass die Fließgeschwindigkeit ungleichmäßiger wird, was an einigen Stellen zu Unterextrusion und an anderen zu Überextrusion führt. Außerdem kann die Durchflussmenge unter die Mindestdurchflussmenge der Düse und der Extrudereinstellung sinken, was zu ungleichmäßigem Fluss und Tropfenbildung führt. Um diesen Effekt zu verringern, können Sie den [Mindestwandfluss](wall_min_flow.md) einstellen, der einige der dünnsten Wände zu Fahrwegen auf Kosten der Maßhaltigkeit macht.

**Diese Einstellung sieht in der Schichtansicht eher unschön aus. Im tatsächlichen Druck gibt es keine Grenzen zwischen den Linien. In der Schichtansicht werden nur die Pfade des G-Codes angezeigt, aber in Wirklichkeit wird das Material von der anderen Wand, mit der es sich überlappt, zur Seite geschoben. Auch winzige Verringerungen des Durchflusses machen sich im tatsächlichen Druck nicht bemerkbar, da sich die Durchflussrate durch die Düse nicht so schnell anpassen kann. Diese Effekte führen dazu, dass der tatsächliche Druck glatter ausfällt, als es in der Schichtansicht dargestellt wird.**