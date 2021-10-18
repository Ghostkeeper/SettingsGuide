Einzugsturm aktivieren
====
Damit wird ein Turm mit einer Mischung von Materialien auf Ihre Bauplatte gedruckt. Der Turm ist dazu gedacht, entsorgt zu werden, aber er dient dazu, das Material nach jedem Extruderwechsel vorzubereiten.

![Wie ein Einzugsturm aussieht und welche Abmessungen er hat](../images/prime_tower.svg)

Während andere Extruder drucken, kann es vorkommen, dass aus einer Düse etwas Material austritt, so dass die Düsenkammer leer ist. Das anschließende Vorbereiten des Materials ist unerlässlich, da das Material sonst zu Beginn noch nicht richtig fließt.

Der Einzugsturm besteht aus einer Außenhülle, die mit einem Extruder komplett bedruckt wird, jede Schicht. Dies ist notwendig, um die Stabilität des Turms zu gewährleisten, erfordert aber manchmal zusätzliche Extruderwechsel für einige Drucke. Alle anderen Extruder drucken in Schleifen in dieser Hülle, indem sie ihr Material innerhalb des Turms, vorzugsweise entlang der Innenwände, entsorgen. Diese Extruder müssen nicht vorbereiten, wenn sie zufällig auf der Schicht beginnen, da sie dann nicht in den Stand-by-Modus gehen.

Das Material, das für die äußere Schale ausgewählt wird, ist das Material mit der größten [Haftungstendenz](../material/material_adhesion_tendency.md). Dies ist eine ausgeblendete Einstellung, die nicht über die Benutzeroberfläche geändert werden kann und die angibt, wie gut die Schichten aneinander haften. Durch die Wahl des Materials mit der größten Haftung zwischen den Schichten wird das Risiko, dass der Einzugsturm bricht, minimiert. Wenn mehrere Materialien die gleiche Haftungstendenz haben (z. B. bei zweifarbigen Drucken mit demselben Materialtyp), wird die niedrigste Extruderzahl gewählt.

Neben der Vorbereitung macht die Düse auch eine Bewegung innerhalb des Turms, um Material von der Düse abzuwischen, das sich während des Standby-Modus angesammelt hat. Dadurch wird verhindert, dass der ooze am Druckgut haften bleibt. Aus diesem Grund wird der Einzugsturm manchmal auch als *Wischturm* bezeichnet.

Die Nachteile des Einzugsturm bestehen darin, dass er zusätzliche Zeit für den Druck benötigt und etwas Platz auf der Bauplatte wegnimmt.