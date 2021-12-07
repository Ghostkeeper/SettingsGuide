Wechselnde Rotation der Außenhaut
====
Wenn die Ober- und Unterseite mit den Linien oder dem Zickzack-[Muster](../top_bottom/top_bottom_pattern.md) gedruckt werden, sind die Linien normalerweise in den diagonalen Richtungen ausgerichtet, wobei sich die beiden Richtungen später abwechseln. Wenn diese Einstellung aktiviert ist, wechseln sie stattdessen in vier Richtungen: zwei diagonale Richtungen, vertikal und horizontal.

![Abwechselnd vier Richtungen](../../../articles/images/skin_alternate_rotation.gif)

Diese Einstellung setzt die Einstellung [Richtungen der oberen/unteren Linie](../top_bottom/skin_angles.md) außer Kraft. Das Verhalten ist jedoch dasselbe. Diese Einstellung kann sogar vollständig emuliert werden, indem man die Winkel `[45, 135, 0, 90]` eingibt.

Im Allgemeinen wird Ihr Druck in der Richtung längs zur Richtung der Linien am steifsten sein. Wenn diese Einstellung nicht aktiviert ist, ist er in den beiden diagonalen Richtungen am steifsten und in den orthografischen Richtungen am schwächsten. Diese diagonalen Richtungen wurden gewählt, weil die gängigsten Gantry-Mechanismen für 3D-Drucker mehr Motoren für diagonale Bewegungen verwenden, wodurch sie in diesen Richtungen schneller beschleunigen können.

Wenn diese Einstellung aktiviert ist, werden die Richtungen der Linien gleichmäßiger verteilt. Dadurch wird auch die Stärke des Objekts gleichmäßiger verteilt. Dadurch wird das Objekt in den vertikalen und horizontalen Richtungen stärker, aber in den diagonalen Richtungen etwas schwächer. Außerdem dauert es etwas länger, bis das Objekt gedruckt ist.