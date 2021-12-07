Fließtemperaturgraf
====
Wenn Sie schneller drucken möchten, ist es am besten, mit einer etwas höheren Temperatur zu drucken. Dadurch wird das thermoplastische Material flüssiger und kann schneller aus der Düsenöffnung fließen. Wenn [Automatische Temperatur](material_flow_dependent_temperature.md) aktiviert ist, gibt diese Einstellung für jede Flussrate an, bei welcher Temperatur das Material gedruckt werden soll. Die Durchflussrate wird dann für jede Schicht gemittelt, um eine Temperatur für diese Schicht zu bestimmen.

Die Durchflussmenge wird in Kubikmillimetern pro Sekunde berechnet, gemittelt über eine ganze Schicht. Die Temperatur wird in Grad Celsius angegeben. Der Wert dieser Einstellung muss eine durch Kommata getrennte Liste von Koordinaten sein. Jede Koordinate hat die Form `[<flow>, <temperature>]`.

Ziel dieser Einstellung ist es, eine bessere Druckqualität zu erreichen, indem Über- und Unterextrusion bei großen Flussänderungen innerhalb eines Drucks reduziert werden. Ein häufiger Fall dafür ist die Grenze zwischen Außenhaut und Füllung. Da die Außenhaut normalerweise viel langsamer gedruckt wird als die Füllung, sollten die Schichten mit viel Füllung bei einer etwas höheren Temperatur gedruckt werden, damit das Material während des Drucks der Füllung richtig extrudiert werden kann.

Bei vielen Druckern neigt der PID-Regler, der die Temperaturen in der Düse des Druckers regelt, zu einer Überreaktion, wenn es in kurzer Zeit zu vielen Temperaturänderungen kommt. Dies kann dazu führen, dass die Drucktemperatur sehr ungenau ist, wenn diese Einstellung verwendet wird.

**Diese Einstellung ist derzeit in Curas Oberfläche nicht sichtbar und kann nicht aktiviert werden.**