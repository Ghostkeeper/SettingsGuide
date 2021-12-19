Ringing
====
Ringing (manchmal auch "Ghosting" genannt) ist ein Effekt, bei dem Wellen auf ansonsten flachen Oberflächen in der Nähe kleiner Details auf dieser Oberfläche auftreten. Die Wellen treten kurz nach dem Drucken der kleinen Details auf.

![Wellen auf der Oberfläche](../../../articles/images/ringing.jpg)

Ursachen
----
Ringing wird durch Vibrationen in Ihrem 3D-Drucker verursacht. Der Versuch, Ringing zu verhindern, besteht darin, diese Vibrationen zu reduzieren. Sie sind besonders ausgeprägt, wenn sich der Druckkopf in einer der Resonanzfrequenzen des Druckerrahmens bewegt.

Teurere 3D-Drucker versuchen in der Regel, dieses Phänomen durch einen steiferen Rahmen zu verhindern, der weniger vibriert. Sie haben ein stärkeres Portal mit gehärteten Stahlstangen und -stäben oder einen vollständig geschlossenen Rahmen aus sehr steifem Material. Dies ist jedoch teuer, so dass billige 3D-Drucker nicht über die Mittel verfügen, um Ringing zu verhindern. Bei Druckern, die mit einem Bowdenzug ausgestattet sind, tritt das Ringing ebenfalls nicht so stark auf, da der Druckkopf viel leichter ist als ein Druckkopf mit Direktantrieb (da der schwere Vorschubmotor auf dem Druckkopf ruht).

Obwohl sich das Ringing horizontal bemerkbar macht, sind die Schwingungen nicht immer horizontal. Das Auf- und Abschwingen der Bauplatte in Bezug auf die Düse ist ebenfalls ein sehr wichtiger Effekt, da der Kunststoff gequetscht und breiter wird, wenn die Bauplatte näher schwingt, oder dünner, wenn sie weiter schwingt.

Hardware-Lösungen
----
Bevor Sie Ihren Druck in Cura anpassen, sollten Sie zunächst prüfen, ob Sie Ihre Hardware verbessern können, um Ringing zu verhindern. Dies kann zu einer allgemeinen Verbesserung der Druckergebnisse führen, ohne dass andere Qualitäten des Drucks wie Stärke oder Produktivität geopfert werden müssen. Hier sind einige Dinge, die Sie in Betracht ziehen können:
* Fügen Sie Dämpfungselemente unter Ihrem Drucker hinzu. Sie können Gummifüße verwenden oder den Drucker einfach auf einen Block aus weichem Schaumstoff stellen. Dies verhindert Vibrationen, wenn der Tisch vibriert, und verhindert, dass der Drucker auch den Tisch vibrieren lässt. Dadurch wird die Rückkopplung des vibrierenden Druckers mit dem Tisch reduziert, was wiederum zur Verringerung der hochfrequenten Vibrationen beiträgt.
* Ziehen Sie die Antriebsriemen des Portals nach. Wenn diese Riemen nicht straff sind, kann der Druckkopf aufgrund der Elastizität des Gummis vibrieren.
* Wenn Ihr Druckkopf flexible Anbauteile hat, z. B. einen Bowdenzug, sollten Sie diese so befestigen, dass sie nicht mehr wackeln können. Kabelbinder eignen sich gut für Bowdenzüge, wenn es etwas gibt, an dem man sie befestigen kann.
* Fügen Sie dem Rahmen Ihres 3D-Druckers mehr Masse hinzu. Dadurch wird es schwieriger, den Rahmen aufgrund seiner größeren Trägheit zu bewegen, und es wird schwieriger sein, ihn zum Schwingen zu bringen.
* Erhöhen Sie die Steifigkeit des Rahmens Ihres 3D-Druckers durch zusätzliche Verstrebungen oder Querstreben. Sie könnten diese aus haltbaren Materialien wie Stahl herstellen, aber wenn das nicht in Frage kommt, finden Sie vielleicht etwas in einem Baumarkt, das mit minimalen Anpassungen passt. Sie können auch in Betracht ziehen, diese Streben und Querstreben in 3D zu drucken, aber bedenken Sie, dass die meisten Kunststoffe einer anhaltenden Krafteinwirkung nicht gut standhalten.

Die Cura-Lösungen
----
Wenn die Hardware-Lösungen nicht in Frage kommen, können Sie den Ringing-Effekt auch durch einige Anpassungen in den Cura-Einstellungen reduzieren.

Da die Vibrationen durch die Beschleunigung des Druckkopfes verursacht werden, zielen die wichtigsten Verbesserungen darauf ab, diese Beschleunigungen zu reduzieren.
* Die Verringerung der maximalen [Druckgeschwindigkeit](../speed/speed_print.md) reduziert die Dauer der Beschleunigungen.
* Die Verringerung der [Beschleunigungsrate](../speed/acceleration_print.md) verringert direkt die Beschleunigung und reduziert die Stärke der Vibrationen.
* Im 3D-Druck ist [jerk](../speed/jerk_print.md) ein Fachbegriff für momentane Geschwindigkeitsänderungen in Kurven. Das bedeutet, dass im Grunde genommen versucht wird, unendlich zu beschleunigen, um nicht in jeder Kurve zu stark abbremsen zu müssen. Dies führt zu sehr hohen Beschleunigungen für kurze Zeit in jeder Kurve. Die Verringerung des Rucks kann dann auch dazu beitragen, Vibrationen zu reduzieren. Anstelle einer kurzen, starken Beschleunigung wird langsamer und länger beschleunigt, wodurch hochfrequente Vibrationen verringert, niederfrequente Vibrationen jedoch verstärkt werden.

Durch diese Anpassungen dauert der Druckvorgang länger. Sie können das Ringing aber auch auf andere Weise verhindern, indem Sie die Art der Bewegungen, die es verursachen, unterbinden:
* Deaktivieren Sie die Methode [Lücken füllen](../shell/fill_perimeter_gaps.md) und drucken Sie keine [dünnen Wände](../shell/fill_outline_gaps.md), da diese Methoden manchmal sehr kleine Liniensegmente und zusätzliche Fahrbewegungen verwenden. Wenn anschließend eine Wand gedruckt wird, vibriert der Drucker noch ein wenig.
* Wenn Ihr Drucker nicht den Druckkopf, sondern die Bauplatte auf und ab bewegt, sollten Sie keinen [Z-Sprung](../travel/retraction_hop_enabled.md)verwenden. Diese bewirken, dass die Bauplatte noch lange nach Abschluss des Sprungs auf- und abschwingt.

Sie können auch die [Innenwände vor der Außenwand](../shell/outer_inset_first.md) drucken. Da der Druck der Wände in der Regel nicht so viele Vibrationen verursacht wie andere Teile, kann der Drucker so aufhören zu vibrieren, bevor die wichtige Außenwand gedruckt wird.

Abhängig von der Geometrie Ihres Druckportals werden die Vibrationen manchmal in verschiedenen Richtungen unterschiedlich stark absorbiert. Eine Drehung des Druckers um 45 Grad kann ebenfalls helfen. 