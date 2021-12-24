Kompensation der Schrumpfung des Skalierungsfaktors
====
<!--if cura_version >= 4.8-->Mit dieser Einstellung wird das Modell vor dem Slicen automatisch skaliert. Ziel ist es, die Schrumpfung auszugleichen, die beim Abkühlen des Drucks auf Raumtemperatur auftritt. Indem man den Druck etwas größer als gewünscht macht, kann das Endergebnis den ursprünglichen Abmessungen des Eingabemodells besser entsprechen. Dieser Skalierungsfaktor wird auf alle Dimensionen (X, Y und Z) gleichermaßen angewendet.

Die gesamte Modellgruppe wird von ihrem Zentrum aus skaliert. Wenn Sie mehrere Modelle drucken, werden sie alle vom gleichen Ausgangspunkt aus skaliert. So können Sie die Modelle sehr nah beieinander positionieren, ohne dass sie sich im endgültigen Druck überlappen. Die Kollisionsbereiche der Modelle werden mitskaliert, so dass Sie genau sehen können, wo Ihr Druck am Ende landen wird. Dadurch wird auch verhindert, dass Sie Modelle an Stellen platzieren, an denen sie mit Merkmalen des Drucks oder des Druckers kollidieren würden, z. B. mit dem Einzugsturm oder den Clips der Bauplatte.

Ein Faktor von 100 % verursacht keine Skalierung. Ein Skalierungsfaktor von etwas mehr als 100 % ist für viele technische Materialien wie ABS oder Polypropylen angemessen. Ein Skalierungsfaktor von weniger als 100 % würde darauf hindeuten, dass das Material beim Abkühlen wächst, etwa wie ein Schaumstoff.

Rein chemische Daten darüber, wie stark ein Material zwischen Drucktemperatur und Raumtemperatur schrumpft, reichen nicht aus, um einen guten Wert für diese Einstellung vorherzusagen, da auch der Druckprozess die Schrumpfung beeinflusst. Wenn der Kunststoff in einer Linie extrudiert wird, wird er in Richtung der Länge der Linie gedehnt und schrumpft stärker in dieser Achse. Die Schrumpfung ist nicht gleichmäßig, aber diese Einstellung wendet nur einen einheitlichen Skalierungsfaktor in alle Richtungen an. Um genaue Ergebnisse zu erzielen, müssen Sie den Skalierungsfaktor auf die Achse anwenden, die für Ihre Anwendung am wichtigsten ist. Wenn es viele lange, gerade Linien entlang der wichtigsten Abmessung gibt, muss der Skalierungsfaktor größer sein.

Wenn der Skalierungsfaktor größer als 100,5% ist und Sie etwas Großes drucken, zeigt Cura eine Warnung an, dass es zu Problemen kommen könnte [warping](../troubleshooting/warping.md).<!--endif-->

<!--if cura_version < 4.8:Dies ist eine beschreibende Einstellung, die Cura mitteilt, wie stark das Material schrumpft, wenn es von der Drucktemperatur auf Raumtemperatur abkühlt.

Diese Einstellung wird derzeit nicht zum Slicen verwendet. Sie wird derzeit nur verwendet, um dem Benutzer beim Drucken großer Objekte eine Warnung anzuzeigen, wenn das Schrumpfungsverhältnis größer als 0,5 % ist.
-->
**Diese Einstellung ist in der Liste der Einstellungen nicht sichtbar. Es handelt sich nur um eine interne Einstellung, die vom Materialprofil überschrieben wird.**