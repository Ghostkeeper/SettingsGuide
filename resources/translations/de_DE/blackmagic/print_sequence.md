Druckreihenfolge
====
Wenn mehrere Modelle auf der Druckplatte platziert werden, bestimmt dies die Reihenfolge, in der die Schichten für diese Objekte gedruckt werden. Es gibt zwei Optionen.

Alle auf einmal
----
Alle Objekte werden gleichzeitig gedruckt, d. h. die Schichten werden für alle Objekte gleichzeitig von unten nach oben gedruckt. Es wird eine Ebene jedes Objekts gedruckt, bevor die nächste Ebene gedruckt wird.

Dies hat zwei große Vorteile:
* Die vorherige Schicht erhält mehr Zeit zum Abkühlen, was zu einer besseren Qualität beim Druck kleiner Objekte führt.
* Das gesamte Bauvolumen kann für den Druck genutzt werden.

Einer nach dem anderen
----
Die Objekte werden nacheinander gedruckt, d. h. es werden alle Schichten eines Objekts gedruckt, und dann geht es zurück zur Druckplatte, um das nächste Objekt zu drucken.

Die wichtigsten Vorteile dieses Modus sind:
* Wenn der Druck aus irgendeinem Grund fehlschlägt, sind alle Objekte, die vor dem Fehlschlag fertiggestellt wurden, völlig in Ordnung.
* Es sind weniger Verfahrbewegungen erforderlich, um zwischen den Modellen hin und her zu fahren. Das spart etwas Druckzeit und reduziert die Anzahl der Narben auf der Oberfläche, wo die Düse aus dem Objekt austritt und in das Objekt eintritt.

Dieser Modus ist jedoch mit einigen Einschränkungen verbunden, um Kollisionen des Kopfes und des Portals mit dem Modell zu vermeiden.
* Sie können keine Objekte drucken, die höher als die Portalhöhe Ihres Druckers sind. Die Gantry-Höhe kann im Dialog Maschineneinstellungen des Druckers eingestellt werden. Diese Gantry-Höhe gibt an, wie groß der vertikale Abstand zwischen der Düsenspitze und dem Druckkopfträger ist. Der Grund für diese Begrenzung ist, dass sich der Druckkopf nach unten zur Druckplatte bewegen muss, um das zweite Objekt zu drucken. Dies bedeutet, dass das erste Objekt vom Druckkopfträger getroffen werden kann, während das zweite Objekt gedruckt wird. Theoretisch kann das letzte gedruckte Objekt höher als der Druckkopfträger sein, aber der Einfachheit halber lässt Cura dies nicht zu.
* Die Objekte müssen weiter voneinander entfernt sein, um zu verhindern, dass der Druckkopf die zuvor gedruckten Modelle an der Seite trifft.
* Die Reihenfolge, in der die Objekte gedruckt werden, ist festgelegt und optimiert, damit die Objekte enger aneinander gedruckt werden können. Wenn Ihr Druckkopf nicht symmetrisch ist, kann dies eine Menge Platz auf der Druckplatte sparen.

**Ein einzelnes Objekt ist nur in der Einzelextrusion verfügbar. Wenn Sie einen Drucker mit mehreren Extrudern verwenden, müssen Sie alle bis auf einen Extruder deaktivieren, damit diese Einstellung angezeigt wird.**