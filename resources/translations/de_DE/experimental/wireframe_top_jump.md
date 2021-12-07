Knotengröße für Drucken mit Drahtstruktur
====
Wenn die [Strategie für Drucken mit Drahtstruktur](wireframe_strategy.md) auf "Knoten" eingestellt ist, wird an der Spitze jedes Sägezahns eine kleine Auf- und Abwärtsbewegung ausgeführt. Mit dieser Einstellung wird das Ausmaß dieser Bewegung konfiguriert.

![Wo der Knoten platziert wird und welche Größe er hat](../../../articles/images/wireframe_top_jump.svg)

Die Bewegung für diesen "Knoten" besteht aus einer Reihe von Fahrbewegungen:
1. Zunächst bewegt sich die Düse um die in dieser Einstellung angegebene Strecke nach oben. Gleichzeitig bewegt sich die Düse um die Hälfte dieses Abstands nach hinten.
2. Wenn in der Spitze eine [Aufwärtsverzögerung](wireframe_top_delay.md) vorhanden ist, wird die Düse für die eingestellte Zeitspanne pausieren. Diese Pause wird in der Spitze der Bewegung des Knotens gemacht.
3. Drittens: Die Düse bewegt sich wieder auf die normale Höhe. Gleichzeitig bewegt sich die Düse um das 1,5-fache der Knotengröße vorwärts und endet in der in dieser Einstellung angegebenen Entfernung von der vertikalen Linie.

Der Zweck des Knotens ist es, dem darüber liegenden horizontalen Ring eine Fläche zu geben, um sich mit dem Sägezahnmuster zu verbinden. Der Knoten variiert ein wenig von Seite zu Seite, so dass, wenn der horizontale Ring nicht sehr genau platziert wird, eine größere Chance besteht, dass sie sich aneinander festhalten. Außerdem wird durch den Knoten die nach oben verlaufende Linie etwas weiter nach oben gezogen, so dass der horizontale Ring darüber geschoben wird. Und schließlich wird der Knoten aufgrund des fehlenden Einzugs bei dieser Fahrbewegung auch ein gewisses Sickern verursachen. Dadurch entsteht ein Klecks, auf dem der horizontale Ring besser aufliegen kann.