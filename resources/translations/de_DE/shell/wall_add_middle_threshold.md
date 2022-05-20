Schwellenwert für das Hinzufügen einer Mittellinie
====
Wenn Sie dünne Teile drucken, passt Cura die Breite der Wandlinien an die exakte Breite des Modells an. Cura kann auch entscheiden, stattdessen weniger Wandlinien zu verwenden. Diese Einstellung ist der Schwellenwert, bei dem Cura eine Linie in der Mitte hinzufügt. Sie kann getrennt von der [Schwelle, bei der sich die beiden mittleren Linien verbinden](wall_split_middle_threshold.md) eingestellt werden.

Diese Einstellung ist die gleiche wie die [Minimale Wandlinienstärke (ungeradzahlig)](min_odd_wall_line_width.md), verwendet aber eine andere Einheit. Die Einheit dieser Einstellung ist in Bruchteilen einer Linienbreite, die die Breite eines Teils erhöhen muss, um eine neue Mittellinie hinzuzufügen.

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
"image_path": "min_wall_line_width_odd_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_odd_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![Wenn die Mittellinie zu klein ist, werden die beiden Linien um sie herum breiter gemacht](../../../articles/images/min_wall_line_width_0_34.png)
![Wird diese Einstellung verringert, beginnt und endet die Mittellinie viel kleiner](../../../articles/images/min_wall_line_width_odd_0_1.png)

Gerade vs. Ungerade Linien
----
Mit dieser Einstellung kann der Schwellenwert für das Hinzufügen von Linien speziell dann angepasst werden, wenn es sich um eine ungerade Anzahl von Linien handelt. Dies ist der Fall, wenn sich in der Mitte eine einzige Linie befindet und nicht zwei. Sie bestimmt, wann eine neue Linie zwischen den beiden mittleren Linien hinzugefügt wird.

Der Schwellenwert für das Hinzufügen einer Mittellinie kann sich von dem Schwellenwert für das Teilen der Mittellinie in zwei Linien unterscheiden, da die beiden Linien unterschiedlich ineinander übergehen. Wenn eine ungerade Linie hinzugefügt wird, beginnt sie erst, wenn die beiden umgebenden Linien ihr den nötigen Platz gemacht haben. Während des Übergangs gibt es eine kleine Lücke, in der die umliegenden Linien noch nicht genug Platz geschaffen haben. Dies ist anders als bei einer geraden Anzahl von Wänden: Die Linie in der Mitte teilt sich dann in zwei, und diese beiden Linien überlappen sich leicht, bis sie weit genug voneinander entfernt sind. Durch Verringern des Schwellenwerts "Mittlere Linie hinzufügen" wird die Größe der Lücke an den Übergängen von geraden zu ungeraden Linien verringert. Durch Verringern des Schwellenwerts "Mittlere Linie teilen" wird die Überschneidung an den Übergängen von ungeraden zu geraden Linien verringert.

Die Lücken, die entstehen, wenn eine ungerade Linie beginnt, sind im Endergebnis sichtbarer als eine leichte Überextrusion an einer Nahtstelle, so dass es hilfreich sein kann, den Schwellenwert "Mittlere Linie hinzufügen" etwas niedriger einzustellen als den Schwellenwert "Mittlere Linie teilen".

Eine Verringerung dieser Einstellung führt zu:
* Kleinere Lücken, wenn eine Mittellinie endet.
* Reduzierte maximale Breite eines Paares von gleichmäßigen Mittellinien.
* Dünnere Linien, die sich möglicherweise nicht gut extrudieren lassen.
* Längere Linien, die länger zum Drucken brauchen.

**Diese Einstellung gilt nicht nur für normale Wände, sondern auch für Wände mit zusätzlicher Außenhaut, Support-Wände, Füllungen und konzentrische Muster.**