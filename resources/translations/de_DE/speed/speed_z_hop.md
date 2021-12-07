Z-Sprung-Geschwindigkeit
====
Diese Einstellung konfiguriert die Bewegungsgeschwindigkeit, mit der die vertikalen Bewegungen bei einem Z-Sprung ausgeführt werden. Die horizontalen Bewegungen eines Z-Sprungs sind davon nicht betroffen, da diese durch die [Bewegungsgeschwindigkeit](speed_travel.md) konfiguriert werden.

![Die vertikale Bewegung erfolgt mit der Z-Sprung-Geschwindigkeit](../../../articles/images/speed_z_hop.svg)

<!--if cura_version >= 4.2-->Die Z-Sprung-Geschwindigkeit wird auch als Geschwindigkeit für die Fahrbewegung zwischen den Schichten verwendet. In der Praxis spielt diese Geschwindigkeit nur eine geringe Rolle, da die Bewegung einer einzelnen Schicht so kurz ist, dass sie fast immer durch die Beschleunigung und nicht durch die maximale Fahrgeschwindigkeit begrenzt wird.<!--endif-->

Bei den meisten Druckern ist die Z-Achse zwar robust, aber langsam. Durch Erhöhen der Z-Sprung-Geschwindigkeit werden die Grenzen der Z-Bewegung getestet, was dazu führen kann, dass der Z-Motor einige Schritte überspringt. Infolgedessen könnte die Düse nach dem Z-Sprung auf einer anderen Höhe landen. Eine Verringerung dieser Geschwindigkeit verringert die Wahrscheinlichkeit, dass dies geschieht.

Andererseits führt eine höhere Z-Sprung-Geschwindigkeit dazu, dass sich die Düse schneller von der gedruckten Oberfläche entfernt. Dadurch kann sich die Größe der Kleckse verringern.

Aufgrund der geringen Beschleunigungsraten der Z-Achse wird die gewünschte Z-Sprung-Geschwindigkeit nur selten erreicht, es sei denn, die Z-Sprung-Höhe ist sehr hoch oder die Geschwindigkeit sehr niedrig.