Anzahl verteilter Wände
====
Cura kann die Breite der Wandlinien anpassen, um sie besser an die zu druckende Form anzupassen, aber es muss nicht jede Wand um den gleichen Betrag angepasst werden. Cura zieht es vor, die Breite der Wände weiter im Inneren des Modells zu verändern. Diese Einstellung bestimmt die Anzahl der Wände, von innen nach außen gezählt, die an den verfügbaren Platz angepasst werden.

<!--screenshot {
"image_path": "wall_distribution_count_1.png",
"models": [
	{
		"script": "misaligned_ring.scad",
		"transformation": ["scale(2)"]
	}
],
"camera_position": [-11, 0, 111],
"settings": {
	"wall_line_count": 5,
	"wall_distribution_count": 1
},
"colour_scheme": "line_width",
"colours": 128
}-->
<!--screenshot {
"image_path": "wall_distribution_count_5.png",
"models": [
	{
		"script": "misaligned_ring.scad",
		"transformation": ["scale(2)"]
	}
],
"camera_position": [-11, 0, 111],
"settings": {
	"wall_line_count": 5,
	"wall_distribution_count": 5
},
"colour_scheme": "line_width",
"colours": 128
}-->
![Konzentriert in der Mitte, dort mit großen Unterschieden in den Linienbreiten ](../../../articles/images/wall_distribution_count_1.png)
![Verteilt auf viele Wände](../../../articles/images/wall_distribution_count_5.png)

Wände mit unterschiedlicher Breite sind schwieriger zu drucken als einfache Wände mit konstanter Breite. Es braucht einige Zeit, um die Durchflussmenge aus der Düse einzustellen, und für den Übergang müssen auch einige scharfe Ecken gemacht werden, die ein Ringing verursachen können. All dies wird am besten so weit wie möglich von außen gemacht, wo es auf der Oberfläche des Drucks sichtbar wäre. Daher konzentriert Cura die Anpassung der Linienbreite auf die innersten Wände.

Andererseits bedeutet die Konzentration der Variation auch, dass die Linien in der Mitte sehr unterschiedliche Breiten haben werden. Die Verteilung auf mehrere Linien bedeutet, dass die Amplitude der Variationen kleiner sein kann, wodurch die Auswirkungen der variablen Linienbreite reduziert werden, anstatt sie auf der Innenseite zu verstecken.

Mit dieser Einstellung wird eine Anzahl von Wänden auf der Innenseite ausgewählt, zwischen denen die Linienbreite angepasst werden kann, um den verfügbaren Platz zu füllen. Dies gilt in beide Richtungen von der Mitte aus, so dass bei einer Einstellung von 2 bis zu 4 Wände in der Mitte angepasst werden können. Auch innerhalb dieser Wände ist die Anpassung nicht gleichmäßig verteilt. Die Wände in der Mitte werden immer etwas stärker angepasst als die Wände an der Außenseite.

Die äußere Wand wird nach Möglichkeit immer auf der Nennlinienbreite gehalten. Diese Wand hat einen so großen Einfluss auf die Druckqualität, dass sie auf einer konstanten Linienbreite gehalten wird, um die Oberfläche so glatt wie möglich zu machen. Nur wenn das Stück so dünn wird, dass es nur noch aus Außenwänden besteht, werden diese Wände angepasst.

In der Praxis ist es fast immer besser, die Unvollkommenheiten in der Mitte zu verstecken, als sie über mehrere Wände zu verteilen. Daher ist es am besten, diese Einstellung so niedrig wie möglich zu halten. Wenn Sie mit Materialien arbeiten, die schwer zu extrudieren sind oder deren Fließverhalten sich nur schwer ändern lässt, wie z. B. flexible Materialien, ist es hilfreich, diese Einstellung zu erhöhen, um Fließveränderungen zu reduzieren. Ganz verhindern lassen sich diese Fließveränderungen jedoch nicht.

**Diese Einstellung gilt nicht nur für normale Wände, sondern auch für Wände mit zusätzlicher Außenhaut, Support-Wände, Füllungen und konzentrische Muster.**