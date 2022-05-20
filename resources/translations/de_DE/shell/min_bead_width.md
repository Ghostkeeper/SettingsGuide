Minimale Wandlinienstärke (dünn)
====
Mit dieser Einstellung können sehr kleine Details mit einer Linienbreite gedruckt werden, die eigentlich zu groß für sie ist. Anstatt sehr dünne Linien zu drucken, wird mit einer vernünftigen Linienbreite gedruckt.

Wenn die [Mindestgröße des Merkmals](min_feature_size.md) sehr niedrig eingestellt ist, könnten einige sehr dünne Teile gedruckt werden. Das funktioniert nicht gut. Es ist zwar möglich, Linien zu drucken, die kleiner als die Düsengröße sind, aber nicht viel. Das Drucken zu dünner Linien führt zu inkonsistenten Extrusion.

Stattdessen werden diese sehr dünnen Linien breiter gemacht, damit sie gleichmäßiger extrudiert werden. Jeder Teil des Modells, der dünner ist als die Mindestbreite der dünnen Wandlinien, wird mit einer einzigen Linie der Mindestbreite der dünnen Wandlinien gedruckt. Die Linien werden dann breiter als die ursprüngliche Breite des Modells. Dies verringert die Maßgenauigkeit, aber zumindest wird zuverlässig gedruckt.

Der Wert dieser Einstellung sollte die dünnste Linienbreite sein, die der Drucker zuverlässig erreichen kann, bevor er anfängt, raue Oberflächen und inkonsistente Extrusion zu erzeugen. Dieser Wert liegt normalerweise zwischen der Düsengröße und der halben Düsengröße. Ein höherer Wert führt dazu, dass dünne Teile zu dick gedruckt werden, verringert aber die Gefahr der Unterextrusion, die durch den Versuch, zu dünne Linien zu drucken, entsteht.