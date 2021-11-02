Maximale Bewegungsauflösung
====
Wenn das Modell eine sehr hohe Auflösung hat, wird Cura die Auflösung so reduzieren, dass der Prozessor des Druckers mit der Verarbeitung der G-Code-Befehle während der Ausführung mithalten kann. Die maximale Auflösung der Fahrwege kann separat von der [Maximale Auflösung](meshfix_maximum_resolution.md) beim Drucken bestimmt werden.

Da Fahrwege wesentlich schneller ausgeführt werden als Druckbewegungen, durchläuft der Druckkopf die Liniensegmente des Fahrwegs wesentlich schneller als andere Liniensegmente. Die CPU müsste diese Zeilensegmente sehr viel schneller verarbeiten, um mit der Düse Schritt halten zu können. Aus diesem Grund sollte die Auflösung der Fahrwege geringer sein als die Auflösung der langsameren Extrusionsbewegungen.

Die Auflösung der Bewegung während der Fahrwege ist für die Druckqualität oft auch nicht wichtig. Da nicht extrudiert wird, gibt es keine Oberfläche, die unscharf oder kantig werden könnte. Aus diesem Grund hat eine Verringerung der Auflösung der Fahrwege keinen wesentlichen Einfluss auf die Druckqualität.

Die meisten Fahrwege von Cura sind gerade Linien. Das sind die schnellsten Bewegungen und erzeugen die wenigsten Vibrationen. Wenn Cura jedoch Kollisionen vermeiden soll, neigt es dazu, der Oberfläche der zu vermeidenden Fläche zu folgen. Der Fahrweg um diese Fläche herum hat dann eine ähnliche Auflösung wie die zu vermeidende Fläche. Daher hat diese Einstellung nur dann einen wirklichen Effekt, wenn [Combing-Modus](../travel/retraction_combing.md) aktiviert ist.