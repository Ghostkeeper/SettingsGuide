Automatische Temperatur
====
Wenn Sie schneller drucken möchten, ist es am besten, mit einer etwas höheren Temperatur zu drucken. Dadurch wird das thermoplastische Material flüssiger und kann schneller aus der Düsenöffnung fließen. Diese Einstellung passt die Temperatur automatisch in Abhängigkeit von der durchschnittlichen Fließgeschwindigkeit des Materials aus der Düse an.

Um zu wissen, wie stark die Temperatur angepasst werden muss, wird auf den [Fließtemperaturgraf](material_flow_temp_graph.md) verwiesen. Die Durchflussmenge wird in Kubikmillimetern pro Sekunde berechnet. Setzt man dies in die Durchfluss-Temperatur-Relation ein, erhält man eine bestimmte Temperatur. Diese Temperatur wird dann als Drucktemperatur verwendet. Wenn diese Einstellung aktiviert ist, wird die normale [Drucktemperatur](../material/material_print_temperature.md) nicht mehr verwendet, sondern die aus der Durchflussmenge berechnete Temperatur.

Ziel dieser Einstellung ist es, eine bessere Druckqualität zu erreichen, indem Über- und Unterextrusion bei großen Flussänderungen innerhalb eines Drucks reduziert werden. Ein häufiger Fall dafür ist die Grenze zwischen Außenhaut und Füllung. Da die Außenhaut normalerweise viel langsamer gedruckt wird als die Füllung, sollten die Schichten mit viel Füllung bei einer etwas höheren Temperatur gedruckt werden, damit das Material während des Drucks der Füllung richtig extrudiert werden kann.

Bei vielen Druckern neigt der PID-Regler, der die Temperaturen in der Düse des Druckers regelt, zu einer Überreaktion, wenn es in kurzer Zeit zu vielen Temperaturänderungen kommt. Dies kann dazu führen, dass die Drucktemperatur sehr ungenau ist, wenn diese Einstellung verwendet wird.

**Diese Einstellung ist derzeit in Curas Oberfläche nicht sichtbar und kann nicht aktiviert werden.**