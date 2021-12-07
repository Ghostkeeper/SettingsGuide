Stringing
====
Wenn der Drucker mit dem Drucken eines Teils einer Schicht fertig ist und zu einem anderen Teil wechseln muss, muss er das Extrudieren vorübergehend unterbrechen. Wenn das Material während des Transports weiterfließt, wird ein dünner Kunststofffaden zwischen den beiden Teilen gezogen. Dies wird als Stringing bezeichnet.

![An den Stellen, an denen sich die Düse von einem Teil zum anderen bewegt hat, sind dünne Linien aus Kunststoff sichtbar.](../../../articles/images/stringing.jpg)

Oft sind die Stränge übereinander angeordnet, weil die Düse in jeder Schicht an der gleichen Stelle ein Teil fertigstellt. Dadurch entsteht ein vertikales Geflecht. Der zusätzliche Kunststoff kann sich auch auf dem Stringing der vorhergehenden Schichten stauen, was zu unschönen Blobs führt, die überall verteilt sind.

Stringing geht manchmal mit Unterextrusion einher. Der Slicer geht in der Regel davon aus, dass bei Fahrbewegungen kein Material verloren geht, und weist den Drucker daher an, gerade so viel Material zu extrudieren, dass er das nächste Teil drucken kann. Wenn während einer Bewegung etwas Material aus der Düse austritt (was zu einem Strang führt), wird dieses Material beim Drucken des nächsten Teils nicht verwendet, was dort zu Unterextrusion führt. Stringing ist normalerweise kein Problem, wenn es innerhalb der Füllung auftritt, aber wenn das Stringing zu extrem ist, kann es auch dort ein Problem verursachen, weil es anschließend zu Unterextrusion führt.

Ursachen
----
Stringing tritt auf, weil das Material während einer Fahrbewegung aus der Düse austritt. Obwohl der Drucker während einer Fahrbewegung kein neues Material zuführt, wird der Materialfluss nicht sofort gestoppt. Während des Druckens herrscht in der Düsenkammer ein gewisser Druck, der dadurch entsteht, dass das Filament wie eine Feder eine gewisse Kraft aufbaut. Wenn sich die Düse durch die Luft bewegt, kann sich dieser Druck entladen, wodurch das Material unbeabsichtigt aus der Düse gedrückt wird.

Selbst wenn das Material vor der Fahrbewegung zurückgezogen wird, befindet sich noch etwas Material in der Düsenkammer. Das liegt daran, dass das Material in dieser Düse geschmolzen ist. Wenn man es von einer Seite zurückzieht, zieht man die Schmelze nicht zurück. Solange sie nicht verfestigt ist, verbleibt ein Wulst aus geschmolzenem Material in der Düse. Bei einer Fahrbewegung tritt diese Wulst aus der Düse aus, wenn sie flüssig genug ist.

Prävention
----
Das Einziehen ist die wichtigste Technik, um Stringing zu verhindern. Wenn Sie in Ihren Ausdrucken Stringing feststellen, können Sie Folgendes versuchen:
* Vergewissern Sie sich, dass der [Einzug aktiviert ist](../travel/retraction_enable.md). Dies kostet zwar zusätzliche Druckzeit, reduziert aber das Stringing erheblich.
* Verringern Sie die [Drucktemperatur](../material/material_print_temperature.md). Dadurch wird das Material weniger flüssig, so dass es weniger aus der Düse herausläuft. Außerdem wird ein effektiverer Einzug ermöglicht, da mehr Material aus der Düsenkammer herausgezogen wird.
* Wenn Ihr Material zähflüssig ist, verringert eine Erhöhung der [Einzugsgeschwindigkeit](../travel/retraction_speed.md) im Allgemeinen das Stringing bei kurzen Bewegungen, indem ein Unterdruck auf die Düsenkammer ausgeübt wird. Dieser Unterdruck sorgt dafür, dass das Material angesaugt wird und nicht ausläuft.
* Bei langen Fahrbewegungen wird das Material durch Erhöhen des [Einzugsabstand](../travel/retraction_amount.md) an einem kälteren Ort gehalten, während die Fahrbewegung durchgeführt wird, wodurch die Geschwindigkeit, mit der das Material schmilzt und aus der Düse austritt, verringert wird.
* Manchmal versucht Cura, die Abnutzung des Filaments zu verhindern, indem es die Anzahl der Einzüge über eine bestimmte Länge des Filaments begrenzt. Da es dann keine Einzüge gibt, wird das Stringing eher ein notwendiges Übel sein, als dass der Druck fehlschlägt. Wenn Ihr Feeder das Material nicht zu sehr schleift, können Sie die [Maximale Anzahl von Einzügen](../travel/retraction_count_max.md) erhöhen oder die [Länge des Filaments](../travel/retraction_extrusion_window.md) reduzieren, entlang derer diese Einzüge gezählt werden.
* Wenn Sie [Combing](../travel/retraction_combing.md) an mehreren Stellen zulassen, geht die Düse durch das Innere des Modells und nicht durch das Äußere. Dies verhindert das Stringing nicht wirklich, macht es aber unsichtbar, indem es im Inneren des Modells platziert wird.
* Wenn sie die [Reihenfolge des Wanddrucks optimieren](../shell/optimize_wall_printing_order.md), dann bewegt sich die Düse weniger oft zwischen den Teilen hin und her, was das Stringing reduziert.
* Wenn Sie die [Bewegungsgeschwindigkeit](../speed/speed_travel.md) erhöhen, werden die Strings bei längeren Fahrbewegungen im Allgemeinen dünner. Bei kurzen Fahrbewegungen macht dies jedoch keinen großen Unterschied, da die Beschleunigungsgrenzen der Drucker ohnehin verhindern, dass die Düse diese Geschwindigkeiten erreicht.
* Wenn man mit einer kleineren Düse druckt, wird das Stringing normalerweise ebenfalls reduziert. Aus einer größeren Düse kann der Kunststoff leichter austreten.