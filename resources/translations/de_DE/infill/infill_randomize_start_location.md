Füllstart randomisieren
====
Wenn diese Einstellung aktiviert ist, wird die Position, an der der Drucker mit dem Druck der Füllung auf einer Schicht beginnt, zufällig bestimmt.

Der Anfang der Füllung ist normalerweise etwas schwächer als der Rest der Füllung. Das passiert, wenn die Füllung mit dickeren Linien oder mit einer größeren Schichthöhe schneller gedruckt wird. Der Materialfluss muss sich plötzlich beschleunigen, und das geschieht nicht sofort, so dass es für kurze Zeit zu einer Unterextrusion kommt. Wenn dies in jeder Schicht an der gleichen Stelle geschieht, schwächt dies die Füllstruktur. Die Stelle, an der dies geschieht, ist das schwächste Glied, und die Füllung um sie herum wird stärker belastet. Wenn der Druck einer Kraft ausgesetzt wird, ist es hier am wahrscheinlichsten, dass er bricht.

Normalerweise wird die Füllung mit der Linie begonnen, die der Position am nächsten liegt, an der sich die Düse beim Start der Füllung befand, um die Fahrzeiten zu verkürzen. Wenn diese Einstellung aktiviert ist, wird diese Startposition stattdessen zufällig gewählt. Dadurch werden die Schwachstellen verteilt. Es gibt dann nicht mehr nur ein schwächstes Glied in der Kette, so dass die Füllung am Ende stärker ist.

Allerdings verlängert sich dadurch die Fahrtzeit geringfügig und es kommt zu vermehrtem Tropfen im Modell, da die Entfernung zum Startpunkt der Füllung nicht mehr optimiert wird.

**Die Startposition ist zwar zufällig verteilt, aber dennoch deterministisch. Wird derselbe Slice zweimal wiederholt, sollte dies zu denselben Startpositionen führen.**