Unzulässige Bereiche
====
Diese Einstellung zeigt alle Bereiche auf der Bauplatte an, in denen der Druckkopf nicht drucken darf. Der Benutzer darf keine Objekte in diesen Bereichen platzieren oder so nahe, dass sie dazu führen würden, dass dort etwas gedruckt wird (wie ein Brim).

![Graue Felder kennzeichnen unzulässige Bereiche an der Stelle, an der sich die Clips auf der Bauplatte befinden.](../../../articles/images/machine_disallowed_areas.png)

Diese verbotenen Bereiche sind notwendig, um zu verhindern, dass der Druckkopf mit Dingen kollidiert. So kann sich beispielsweise eine Abwischbürste in Reichweite des Druckkopfs befinden, oder ein Schaltfeld, oder eine Kamera, die etwas zu weit in das Bauvolumen hineinragt. Wenn der Benutzer zu nahe an diesen Objekten drucken würde, würde der Druckkopf mit ihnen kollidieren. Im besten Fall kommt es zu einer [Schicht-Verschiebung](../troubleshooting/layer_shift.md). Im schlimmsten Fall wird der Druckkopf oder das Objekt, mit dem der Druckkopf kollidiert, beschädigt.

Die nicht zugelassenen Bereiche werden als graue Schattierung auf die Bauplatte gezeichnet, um den Benutzer darauf hinzuweisen, dass er dort keine Objekte platzieren kann. Diese Schatten können in alle Richtungen ausgedehnt werden, um zu verhindern, dass der Brim oder die Schürze dagegen stößt, sowie aus verschiedenen anderen Gründen. Es gibt auch andere Schattierungen auf der Bauplatte, zum Beispiel um den Bewegungsbereich zu begrenzen, wenn die Düsen einen Versatz haben.

Wenn nur die aktive Düse mit dem Hindernis kollidieren würde, kann die ähnliche Einstellung [Unzulässige Bereiche für die Düse](nozzle_disallowed_areas.md) verhindern, dass die Düse mit dem Hindernis kollidiert, während der Druckkopf weiterhin über das Hindernis fahren kann.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**