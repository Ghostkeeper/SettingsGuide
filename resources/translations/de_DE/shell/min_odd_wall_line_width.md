Minimale Wandlinienstärke (ungeradzahlig)
====
Wenn Sie dünne Teile drucken, passt Cura die Breite der Wandlinien an die exakte Breite des Modells an. Cura kann auch entscheiden, stattdessen weniger Wandlinien zu verwenden. Diese Einstellung ist der Schwellenwert, bei dem Cura eine Linie in der Mitte entfernt. Sie kann getrennt von der [Schwelle, bei der sich die beiden mittleren Linien verbinden](min_even_wall_line_width.md) eingestellt werden.


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
Mit dieser Einstellung kann der Schwellenwert für das Entfernen von Linien speziell bei einer ungeraden Anzahl von Linien angepasst werden. Dies ist der Fall, wenn sich in der Mitte eine einzige Linie befindet und nicht zwei. Sie legt fest, wann diese einzelne Linie entfernt wird, damit die beiden Linien um sie herum etwas breiter sind.

Die Mindestbreite der ungeraden Wandlinien kann sich von der Mindestbreite der geraden Linien unterscheiden, da sie ineinander übergehen. Wenn eine ungerade Linie entfernt wird, bleibt sie vor dem Übergang stehen und lässt die umliegenden Wände näher rücken. Während des Übergangs gibt es eine kleine Lücke, in der die umgebenden Linien noch nicht ganz zusammenkommen. Dies ist anders als bei einer geraden Anzahl von Wänden: Die beiden Linien in der Mitte fallen dann zusammen und überlappen sich leicht. Eine Verringerung der Mindestbreite der ungeraden Wandlinien verringert die Größe der Lücke an den Übergängen von ungeraden zu geraden Linien. Eine Verringerung der Mindestbreite der geraden Wandlinien verringert die Überlappung an den Übergängen von geraden zu ungeraden Linien.

Die Lücken, die am Ende einer ungeraden Linie entstehen, sind im Endergebnis sichtbarer als eine kleine Überschreitung an einer Verbindungsstelle, so dass es hilfreich sein kann, die Mindestbreite für ungerade Wandlinien etwas niedriger als die Mindestbreite für gerade Wandlinien einzustellen.

Eine Verringerung dieser Einstellung führt zu:
* Kleineren Lücken, wenn eine Mittellinie endet.
* Reduzierte maximale Breite eines Paares von gleichmäßigen Mittellinien.
* Dünnere Linien, die sich möglicherweise nicht gut extrudieren lassen.
* Längere Linien, die länger zum Drucken brauchen.

**Diese Einstellung gilt nicht nur für normale Wände, sondern auch für Wände mit zusätzlicher Außenhaut, Support-Wände, Füllungen und konzentrische Muster.**