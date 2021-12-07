Strategie für Drucken mit Drahtstruktur
====
Das kritischste Problem für die Zuverlässigkeit des Drahtdrucks sind die Verbindungspunkte, an denen die Schichten des Rahmens miteinander verbunden sind. Es gibt verschiedene Strategien, um diese Verbindungen zu stärken. Mit dieser Einstellung können Sie die Strategie wählen, die der Drucker verwenden soll.

Kompensieren
----
Bei dieser Strategie versucht der Drucker, die Senkungsfaktoren des Materials auszugleichen. Da das Material geschmolzen aus der Düse kommt, fällt es ein wenig nach unten, bevor es sich verfestigt, und wird von den Bewegungen der Düse mitgezogen. Durch diese Strategie wird das Sägezahnmuster, das die Schichten des Rahmens verbindet, so verformt, dass es hoffentlich wieder an der richtigen Stelle landet.

Es stehen zwei Ausgleichsfaktoren zur Verfügung: Einer, der das Sägezahnmuster nur vertikal verformt, um [ein Durchhängen zu kompensieren](wireframe_fall_down.md), und einer, der das Sägezahnmuster in diagonaler Richtung verformt, um [das Material zu kompensieren, das mit der Düse mitgezogen wird](wireframe_drag_along.md).

Knoten
----
Wenn diese Strategie gewählt wird, wird am oberen Ende jedes Sägezahns eine kleine Aufwärts- und Rückwärtsbewegung ausgeführt, um dort einen "Knoten" aus Material zu bilden. Der Zweck des Knotens ist es, dem horizontalen Ring darüber einen Bereich zu geben, in dem er sich mit dem Sägezahnmuster verbinden kann. Der Knoten variiert ein wenig von Seite zu Seite, so dass, wenn der horizontale Ring nicht sehr genau platziert wird, eine größere Chance besteht, dass sie sich miteinander verbinden. Außerdem wird durch den Knoten die nach oben verlaufende Linie etwas weiter nach oben gezogen, so dass der horizontale Ring darüber geschoben wird. Und schließlich wird der Knoten aufgrund des fehlenden Einzugs bei dieser Fahrbewegung auch ein gewisses Sickern verursachen. Dadurch entsteht ein Klecks, auf dem der horizontale Ring besser aufliegen kann.

![Wo der Knoten gezogen wird und welche Größe er hat](../../../articles/images/wireframe_top_jump.svg)

Die Bewegung für diesen "Knoten" besteht aus einer Reihe von Fahrbewegungen:
1. Zunächst bewegt sich die Düse leicht aufwärts und rückwärts.
2. Wenn es eine [Verzögerung](wireframe_top_delay.md) in der Spitze gibt, macht die Düse eine Pause für die eingestellte Verzögerungszeit. Diese Pause wird in der Spitze der Bewegung des Knotens gemacht.
3. Drittens: Die Düse bewegt sich wieder auf die normale Höhe. Gleichzeitig bewegt sich die Düse nach vorne und weg von der vertikalen Linie.

Einziehen
----
Wenn diese Strategie gewählt wird, wird das Material beim Drucken des Sägezahnmusters nach jeder Aufwärtsbewegung eingezogen. Die Idee ist, dass durch das Einziehen des Materials der Draht abgebrochen wird. Dadurch wird der Effekt verringert, dass das Material mit der Bewegung der Düse mitgezogen wird, da die vorherige Linie nicht mehr an der Düse befestigt ist. Danach macht die Düse einen kleinen Sprung von 1 Millimeter und fährt mit der diagonalen Bewegung nach unten in Richtung der unteren Schicht fort.

Ein großer Nachteil dieser Strategie ist, dass die diagonale Linie nach unten ebenfalls nicht mehr befestigt ist. Dies macht die Extrusion während dieser Linie praktisch nutzlos. Das Material landet einfach als Klecks auf der unteren Schicht. Außerdem wird das Material stärker geschliffen, da es hin- und hergezogen wird, ohne dass dazwischen viel extrudiert wird. Das alles kostet ebenfalls viel Zeit.