Wandfluss außen
====
Mit dieser Einstellung wird die Durchflussmenge nur für die Außenwand eingestellt. Die Durchflussmenge für die Außenwand kann getrennt von der Durchflussmenge der Innenwände eingestellt werden.

Die Anpassung der Durchflussrate für die Außenwand ist eine Notlösung, um Probleme mit der Extrusionsrate oder der Maßgenauigkeit zu beheben. Der gleiche Effekt kann auch durch Anpassen der Einstellungen [Breite der äußeren Wandlinien](../resolution/wall_line_width_0.md) und [Einfügung Außenwand](../shell/wall_0_inset.md) erzielt werden, aber diese Einstellung könnte anfangs eine intuitivere Methode zur Anpassung sein.

Wenn es ein Problem mit der Extrusionsrate nur bei der Außenwand gibt, ist es besser, sich die [Druckgeschwindigkeiten](../speed/speed_wall_0.md) und die [Drucktemperatur](material_print_temperature.md) anzusehen. Vielleicht bekommt das Material nicht genug Momentum aus der Düse, eine höhere Druckgeschwindigkeit könnte helfen. Vielleicht sind die Linien zu dünn, um richtig zu extrudieren. Vielleicht ist das Material zu kühl oder zu heiß.

Wenn es ein Problem mit der Maßgenauigkeit gibt, ist es besser, sich die [Linienbreiten](../resolution/wall_line_width_0.md), die [Horizontale Erweiterung](../shell/xy_offset.md) und die [Druckreihenfolge](../shell/outer_inset_first.md) anzusehen.