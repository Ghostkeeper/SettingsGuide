Anzahl der langsamen Schichten
====
Die erste Schicht ist nicht die einzige Schicht, die langsamer gedruckt wird. Diese Einstellung legt fest, wie viele Schichten langsamer gedruckt werden sollen. Im Laufe dieser Schichten wird die Druckgeschwindigkeit allmählich auf die normale Druckgeschwindigkeit erhöht.

![Die Druckgeschwindigkeit erhöht sich schrittweise auf 50 mm/s.](../../../articles/images/speed_slowdown_layers.svg)

Ausgehend von der ersten Schicht steigt (oder sinkt) die Geschwindigkeit linear bis zur normalen Druckgeschwindigkeit. Dies geschieht getrennt für die Wände, die Außenhaut, die Füllung usw., wenn sie mit unterschiedlichen Geschwindigkeiten gedruckt werden.

Es gibt zwei Gründe, warum man über mehrere Schichten hinweg auf die normale Druckgeschwindigkeit übergehen sollte. Erstens befinden sich die zweite und dritte Schicht noch recht nahe an der Bauplatte, und wenn man schnell darüber fährt, kann der Druck ziemlich leicht abreißen. Zweitens kann der Unterschied in der Durchflussmenge zwischen der Druckgeschwindigkeit der ersten Schicht und der normalen Druckgeschwindigkeit so groß sein, dass es einige Zeit dauern kann, bis sich die große Durchflussmengenänderung auswirkt. Ein langsamer Übergang verhindert das Unterextrudieren bei einer großen Geschwindigkeitsänderung.

Ein langsamer Übergang führt jedoch auch dazu, dass das Drucken insgesamt länger dauert.