Gleichmäßige Reihenfolge oben
====
Normalerweise ordnet Cura Linien so an, dass der Abstand zwischen ihnen gering ist. Wenn diese Einstellung aktiviert ist, werden die Linien auf der Oberfläche so angeordnet, dass benachbarte Linien immer überlappend in dieselbe Richtung gedruckt werden.

Beim Drucken von Linien auf der Oberfläche überlappen die Linien normalerweise ein wenig mit den benachbarten Linien, da die Form einer Linie kein perfektes Rechteck ist. Durch diese Überlappung erhalten die Linien eine leichte Neigung, wodurch sie das Licht unterschiedlich in verschiedene Richtungen reflektieren. Wenn sich benachbarte Linien unterschiedlich überlappen, ändert sich diese Reflexion. Sie können dies im Endergebnis sehen. Es verleiht verschiedenen Bereichen der Oberfläche einen anderen Glanz. Durch das Drucken in einer gleichmäßigen Reihenfolge wird sichergestellt, dass die Überlappung auf der gesamten Oberfläche gleich ist, so dass es keine Unterschiede bei der Lichtreflexion gibt. Dadurch wirkt die Oberfläche gleichmäßiger und glatter.

<!--screenshot {
"image_path": "skin_monotonic_disabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": false
},
"layer": 1,
"line": [29, 45, 61, 77, 93, 109, 125, 141, 157, 161, 177, 193, 199, 211, 231, 246, 262, 280, 296, 312, 326, 342, 358, 374, 397, 417, 433, 449, 464, 480, 499],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_monotonic_enabled.gif",
"models": [
    {
        "script": "yen.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 130],
"settings": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": true
},
"layer": 1,
"line": [31, 47, 63, 77, 93, 109, 115, 131, 147, 163, 181, 197, 213, 229, 244, 263, 281, 296, 319, 340, 356, 372, 379, 395, 411, 427, 443, 459, 475, 491, 507, 511],
"delay": 125,
"colours": 32
}-->
![Keine gleichmäßige Reihenfolge](../../../articles/images/skin_monotonic_disabled.gif)
![Gleichmäßige Reihenfolge, immer von der rechten unteren Ecke aus](../../../articles/images/skin_monotonic_enabled.gif)

Die gleichmäßige Reihenfolge erhöht die Länge der Fahrbewegungen geringfügig, aber dieser Effekt ist sehr minimal. Er wirkt sich nur optisch auf den Druck aus. Die gleichmäßige Reihenfolge hat keine mechanischen Vorteile.

Um eine glatte Oberfläche zu erzielen, sollten Sie diese Einstellung mit der Einstellung [Combing-Modus](../travel/retraction_combing.md) kombinieren, um fahrten durch die Außenhaut zu vermeiden, und vielleicht [Z-Sprung](../travel/retraction_hop.md) aktivieren. Alternativ könnten Sie auch [Glätten](../top_bottom/ironing_enabled.md) aktivieren, aber das macht den Nutzen dieser Einstellung komplett zunichte. Glätten hat seine eigene [Gleichmäßige Reihenfolge](../top_bottom/ironing_monotonic.md).