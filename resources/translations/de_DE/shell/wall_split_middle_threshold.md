Schwellenwert für das Teilen der Mittellinie
====
Wenn Sie dünne Teile drucken, passt Cura die Breite der Wandlinien an die exakte Breite des Modells an. Cura kann auch entscheiden, stattdessen weniger Wandlinien zu verwenden. Diese Einstellung ist der Schwellenwert, bei dem Cura eine einzelne Linie in der Mitte in zwei teilt, wenn die Breite des Teils zunimmt. Sie kann unabhängig von der [Schwelle, bei der eine neue Mittellinie hinzugefügt wird](wall_add_middle_threshold.md) eingestellt werden.

Diese Einstellung ist die gleiche wie die [Minimale Wandlinienstärke (geradzahlig)](min_even_wall_line_width.md), verwendet aber eine andere Einheit. Die Einheit dieser Einstellung ist der Bruchteil einer Linienbreite, um den die Breite eines Teils zunehmen muss, um die Mittellinie in zwei Teile zu teilen. Da der Breitenunterschied nach der Teilung auf die beiden Linien in der Mitte aufgeteilt wird, entspricht eine kleinere Mindestlinienbreite für gerade Wände einem viel kleineren Schwellenwert für die Teilung der Mittellinie als im Falle der Entfernung einer ungeraden Wand.

<!--screenshot {
"image_path": "min_wall_line_width_0_34.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
<!--screenshot {
"image_path": "min_wall_line_width_even_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_even_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![Die Mittellinie wird verbreitert, damit sie passt](../../../articles/images/min_wall_line_width_0_34.png)
![Wird diese Einstellung reduziert, werden stattdessen zwei Linien verwendet](../../../articles/images/min_wall_line_width_even_0_1.png)

Gerade vs. Ungerade Linien
----
Mit dieser Einstellung können Sie den Schwellenwert für das Hinzufügen von Linien speziell dann anpassen, wenn es sich um eine gerade Anzahl von Linien handelt. Dies ist der Fall, wenn sich in der Mitte zwei Linien befinden und nicht nur eine einzelne Linie. Sie bestimmt, wann eine Linie in der Mitte in zwei Linien geteilt wird.

Der Schwellenwert für die Teilung einer mittleren Linie kann sich von dem Schwellenwert für die Hinzufügung einer mittleren Linie unterscheiden, da sich die beiden Linien auf unterschiedliche Weise miteinander verbinden. Gerade Linien verbinden sich an ihren Enden, indem sie die Enden näher zusammenrücken. Es gibt eine gewisse Überschneidung mit diesen Linien, was zu einer Überextrusion führt. Dies ist anders als bei einer ungeraden Anzahl von Wänden: Die Linie in der Mitte bleibt dann einfach stehen und hinterlässt eine Lücke im Druck. Durch Verringern des Schwellenwerts "Mittlere Linie teilen" wird die Überextrusion an den Übergängen von geraden zu ungeraden Linien reduziert. Eine Verringerung des Schwellenwerts für das Hinzufügen einer Mittellinie verringert die Größe der Lücke an den Übergängen von ungeraden zu geraden Linien.

Die Lücken, die beim Hinzufügen einer Mittellinie entstehen, sind im Endergebnis deutlicher sichtbar als eine leichte Überextrusion an einer Nahtstelle, so dass es hilfreich sein kann, den Schwellenwert "Mittellinie teilen" etwas höher einzustellen als den Schwellenwert "Mittellinie hinzufügen".

Eine Verringerung dieser Einstellung führt zu:
* Verringerung des Überlappungsbereichs, in dem zwei Linien zu einer Linie verschmelzen.
* Reduzierte maximale Breite von einzelnen Mittellinien.
* Dünnere Linien, die sich möglicherweise nicht gut extrudieren lassen.
* Mehr Linien, die länger zum Drucken brauchen.

**Diese Einstellung gilt nicht nur für normale Wände, sondern auch für Wände mit zusätzlicher Außenhaut, Support-Wände, Füllungen und konzentrische Muster.**