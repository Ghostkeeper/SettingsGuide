Geschwindigkeit beim Drucken in Aufwärtsrichtung mit Drahtstruktur
====
Diese Einstellung legt fest, wie schnell sich die Düse nach oben bewegt, während sie eine vertikale Bewegung im Sägezahnmuster ausführt. Die Geschwindigkeit der Aufwärtsbewegung kann getrennt von der restlichen Drahtdruckgeschwindigkeit konfiguriert werden.

![Wo die unterschiedlichen Geschwindigkeiten für den Drahtdruck gelten](../../../articles/images/wireframe_printspeed.svg)

Die Aufwärtsbewegung erfolgt nicht mit der angegebenen Geschwindigkeit für die gesamte Bewegung. Für das kleinste Stück der Aufwärtsbewegung, das durch die Einstellung [Langsame Aufwärtsbewegung](wireframe_up_half_speed.md) definiert ist, bewegt sich der Druckkopf mit der Hälfte dieser Geschwindigkeit.

Eine langsamere Aufwärtsbewegung nimmt mehr Zeit in Anspruch, gibt dem Material aber mehr Zeit zum Verfestigen. Auf diese Weise wird es nicht so stark in Richtung der Diagonale gezogen. Wenn Sie jedoch zu langsam fahren, wird die Linie aufgrund der Trägheit des Filaments und des Drucks in der Düsenkammer auch nach unten gedrückt. Das Filament neigt dann dazu, zu wobblen, was die Wahrscheinlichkeit verringert, dass die nächste horizontale Linie eine gute Verbindung herstellen kann.