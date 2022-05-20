Schwellenwinkel für Wandübergang
====
Dieser Winkel gibt den Winkel an, bei dem Cura beginnt, Übergänge zu erstellen, um den Raum richtig auszufüllen. Alle Ecken, die schärfer als dieser Winkel sind, werden mit Linien variabler Breite gefüllt.

<!--screenshot {
"image_path": "wall_transition_angle.png",
"models": [{"script": "sharpening_corners.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_angle": 11,
	"wall_line_count": 4
},
"colours": 64
}-->
![breiter als 10°, schafft keine Übergänge mehr](../../../articles/images/wall_transition_angle.png)

Damit werden variable Linienbreiten für bestimmte Ecken ein- oder ausgeschaltet. Wenn zwei gegenüberliegende Wände fast parallel sind, also kleiner als der in dieser Einstellung angegebene Winkel, wird der Bereich zwischen ihnen mit Linien gefüllt, die in ihrer Breite variieren können. Stehen sie in einem größeren Winkel zueinander, wird der Raum zwischen ihnen mit Wänden konstanter Breite ausgefüllt.

Wie immer ist dies ein Kompromiss. Die Verwendung einer variablen Breite hat einige Vorteile, wie zum Beispiel:
* Es bleiben keine Lücken zwischen den Linien.
* Es wird nicht derselbe Raum mehrfach ausgefüllt.
* Die Abmessungen des Drucks sind dann genauer.

Allerdings hat es auch einige Nachteile:
* Es entstehen Ecken in dünnen Teilen, die als Wellen auf der Oberfläche erscheinen können.
* Es entstehen zusätzliche Fahrbewegungen.
* Der Drucker kann die Linienbreite in schneller Folge nicht genau ändern.

In der Praxis ist es gut, diesen Winkel groß genug zu wählen, um die Größe der Lücken in scharfen Ecken zu reduzieren, wie sie in der Schichtansicht zu sehen sind, aber ansonsten so klein wie möglich. Ein kleinerer Winkel lässt die Oberfläche im Allgemeinen glatter aussehen.

Es ist nicht möglich, den Winkel auf 0° zu reduzieren, um die variablen Linienbreiten ganz loszuwerden. Bei parallel gegenüberliegenden Wänden wird die Linienbreite immer an den Raum angepasst.

**Diese Einstellung gilt nicht nur für normale Wände, sondern auch für Wände mit zusätzlicher Außenhaut, Support-Wände, Füllungen und konzentrische Muster.**