Stützdach aktivieren
====
Das Stützdach ist eine Zwischenstruktur zwischen dem Support und dem Modell, wobei das Modell auf dem Support ruht. Es kann verwendet werden, um mehr oder besseren Support für das Modell zu bieten, ohne die Druckzeit wesentlich zu beeinflussen. Das Support-Dach wird in der Regel dichter oder langsamer gedruckt.

<!--screenshot {
"image_path": "support_roof_enable.png",
"models": [{"script": "f3.scad"}],
"camera_position": [0, 134, 20],
"settings": {
    "support_enable": true,
    "support_roof_enable": true
},
"colours": 64
}-->
![Das Support-Dach ist in einem dunkleren Blauton gehalten](../../../articles/images/support_roof_enable.png)

Standardmäßig ist das Support-Dach dichter als der normale Support. Dies sorgt für eine bessere Qualität des Überhangs, da das Modell keine großen Abstände überbrücken muss. Allerdings ist es viel schwieriger, den Support zu entfernen.

Das Dach des Supports kann auch mit einem anderen Extruder gedruckt werden als der Rest des Supports. Einige Materialien für den Druck von Support können sehr teuer sein und lassen sich nur langsam drucken. Auf diese Weise wird der größte Teil des Supports weiterhin mit dem billigeren oder schneller zu druckenden Material gedruckt, aber das Dach, bei dem die Verwendung des Support-Materials zum Tragen kommt, wird mit dem hochwertigeren Material gedruckt.