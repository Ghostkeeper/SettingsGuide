Stützlinien verbinden
====
Bei einigen Support-Mustern kann der Support sehr instabil werden, wenn dünne Support-Streifen erforderlich sind. Diese Einstellung bewirkt, dass die Endpunkte der Support-Linien miteinander verbunden werden. Dadurch erhalten sie mehr Stabilität. Außerdem wird der Support dadurch mit einem kontinuierlichen Fluss gedruckt. Es sind weniger Fahrbewegungen erforderlich.

<!--screenshot {
"image_path": "zig_zaggify_support_disabled.png",
"models": [{"script": "plug.scad"}],
"camera_position": [71, 71, 147],
"settings": {
    "support_enable": true,
    "support_pattern": "triangles",
    "support_wall_count": 0,
    "support_offset": 0.2,
    "zig_zaggify_support": false
},
"layer": 236,
"colours": 64
}-->
<!--screenshot {
"image_path": "zig_zaggify_support_enabled.png",
"models": [{"script": "plug.scad"}],
"camera_position": [71, 71, 147],
"settings": {
    "support_enable": true,
    "support_pattern": "triangles",
    "support_wall_count": 0,
    "support_offset": 0.2,
    "zig_zaggify_support": true
},
"layer": 236,
"colours": 64
}-->
![Getrennte Support-Linien](../../../articles/images/zig_zaggify_support_disabled.png)
![Verbundene Support-Linien](../../../articles/images/zig_zaggify_support_enabled.png)

Wenn eine Unterstützungslinie gezeichnet wird, wird eine Linie entlang der Grenze des Unterstützungsbereichs in Richtung der nächsten Linie gezogen, anstatt zur nächsten Linie zu fahren. Dadurch wird das gesamte Support-Muster in eine einzige oder sehr wenige Linien umgewandelt. Die Umwandlung in eine einzige Linie ist nicht immer möglich. Der Anfangspunkt dieser Linie ist willkürlich, so dass sehr oft Linien in der Luft hängen, weil in einer Schicht zwei Linien an einem Endpunkt verbunden sein können, während sie in der nächsten Schicht auf der anderen Seite verbunden sind. Dadurch wird der Support etwas schwächer, aber immer noch stabil, und es werden Unterbrechungen im Fluss verhindert. Das Verhalten dieser Einstellung ist dasselbe wie bei [Füllungslinien verbinden](../infill/zig_zaggify_infill.md).

Das Verbinden der Support-Linien hat eine Reihe von Vorteilen, aber auch einige Nachteile:
* Der Support ist stabiler und kippt während des Druckens nicht so leicht um.
* Die Fließgeschwindigkeit wird konstanter gehalten, so dass Sie den Support mit höherer Geschwindigkeit ohne Fließprobleme drucken können. Dies ist besonders wichtig für Support-Materialien, die sich nur schwer extrudieren lassen.
* Wenn während des Supports Rückzüge vorgenommen werden, sind während des Drucks des Supports deutlich weniger Rückzüge erforderlich, was ein Abschleifen des Materials verhindert.
* Es wird mehr Material benötigt, um den Support zu drucken.
* In der Regel dauert es länger, den Support zu drucken, da die Fahrbewegungen in der Regel schneller sind als der Druck von Support-Linien.

Das Zickzack-Support-Muster wird immer verbunden (mit einer etwas anderen Technik). Diese Einstellung ist für das Zickzackmuster nicht verfügbar.