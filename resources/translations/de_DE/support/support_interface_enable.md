Stützstruktur-Schnittstelle aktivieren
====
Eine "Support-Schnittstelle" ist eine zwischengeschaltete Struktur zwischen dem normalen Support und dem Modell. Diese Struktur kann die Eigenschaften der Schnittstellen zwischen Support und Modell anpassen, ohne den Großteil des Supports wesentlich zu beeinflussen.

<!--screenshot {
"image_path": "support_interface_enable.png",
"models": [{"script": "trash_bin_lid.scad"}],
"camera_position": [93, 188, 87],
"settings": {
    "support_enable": true,
    "support_interface_enable": true
},
"colours": 64
}-->
![Die Support-Schnittstelle ist in einem dunkleren Blauton gehalten](../../../articles/images/support_interface_enable.png)

Standardmäßig sind die Zwischenschichten dichter als der normale Support. Dadurch wird eine bessere Überhangsfläche erzielt, ohne dass viel zusätzliches Material und Druckzeit benötigt wird. Allerdings ist es schwieriger, den Support zu entfernen.

Die Support-Oberfläche kann auch mit einem anderen Extruder gedruckt werden als der Rest des Supports. Einige Materialien für den Druck von Supports können sehr teuer sein und lassen sich nur langsam drucken. Auf diese Weise wird der größte Teil des Supports mit dem billigeren oder schnelleren Material gedruckt, aber die Schnittstelle, an der die Verwendung des Support-Materials zum Tragen kommt, wird mit dem hochwertigeren Material gedruckt.