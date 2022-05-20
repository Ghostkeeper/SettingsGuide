Wandübergangsfilter Rand
====
Einige Modelle haben dünne Elemente, die um die Schwelle liegen, wo eine unterschiedliche Anzahl von Wänden verwendet wird. Dies kann dazu führen, dass die Anzahl der Wände hin und her wechselt, auch wenn die tatsächliche Breite des Stücks nicht viel variiert. Dieser Wechsel beeinträchtigt die Druckqualität, da viele Änderungen des Flusses erforderlich sind und mehr Fahrbewegungen hinzugefügt werden müssen. Mit dieser Funktion werden Übergänge entfernt, wenn sie hin und her gegangen wären.

Wenn ein Übergang entfernt wird, können einige der Linien vorübergehend zu breit oder zu dünn werden. Mit dieser Einstellung werden die Übergänge herausgefiltert, indem begrenzt wird, um wie viel breiter oder dünner die Linie sein darf.

<!--screenshot {
"image_path": "wall_transition_filter_off.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 0,
	"wall_transition_filter_margin": 0,
	"wall_line_count": 3
},
"colours": 64
}-->
<!--screenshot {
"image_path": "wall_transition_filter_on.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 100,
	"wall_transition_filter_margin": 0.2,
	"wall_line_count": 3
},
"colours": 64
}-->
![Mit einer geringen Spanne schwankt sie zwischen 2 und 3 Wänden](../../../articles/images/wall_transition_filter_off.png)
![Mit einer höheren Spanne wechselt sie nicht mehr](../../../articles/images/wall_transition_filter_on.png)

Um genau zu sein, dürfen die Linien um diese Spanne dünner werden als die [Mindestwandlinienbreite](min_wall_line_width.md), wenn dadurch verhindert wird, dass zwischen verschiedenen Wandzahlen hin und her gewechselt wird. Ebenso dürfen Linien um diese Spanne etwas breiter werden, auch wenn eine zusätzliche Wand mit der minimalen Wandlinienbreite ebenfalls hineingepasst hätte.

Dieser Filter zielt darauf ab, ein häufiges Problem bei dünnen Teilen mit niedrig aufgelösten 3D-Netzen zu lösen. Das 3D-Modell, das aus flachen Dreiecken besteht, kann eine Kurve nicht exakt darstellen, sondern nur annähernd. Die Kurve wird Kanten haben, zwischen denen flache Flächen liegen. Bei der Modellierung eines gekrümmten Teils mit einer konstanten Breite ist es wichtig, dass die Außenkanten mit den Innenkanten übereinstimmen. Wenn dies nicht der Fall ist, variiert die Breite des Kreisrings leicht, was zu dem oben gezeigten Effekt führen kann. Wenn dies der Fall ist, sollte der Übergangsfilter verhindern, dass der Effekt zu stark ausfällt.

Eine Vergrößerung des Randes verhindert in manchen Fällen die Erstellung kleiner Liniensegmente. Dadurch lässt sich schneller drucken und die Oberfläche kann glatter aussehen. Es ermöglicht jedoch auch extremere Linienbreiten, die sich möglicherweise nicht gut aus der Düse extrudieren lassen. Wenn Sie Modelle mit niedriger Auflösung und dünnen Teilen drucken, kann eine Erhöhung des Randes die Qualität verbessern. Bei schwierigen Materialien ist es besser, auf der sicheren Seite zu bleiben.

**Diese Einstellung gilt nicht nur für normale Wände, sondern auch für Wände mit zusätzlicher Außenhaut, Support-Wände, Füllungen und konzentrische Muster.**