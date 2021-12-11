Unzulässige Bereiche für die Düse
====
Diese Einstellung zeigt alle Bereiche auf Ihrer Bauplatte an, in die die aktive Düse nicht eindringen darf. Der Benutzer darf keine Objekte in diesen Bereichen platzieren oder so nahe, dass sie dazu führen würden, dass dort etwas gedruckt wird (wie ein Brim).

![Graue Flächen kennzeichnen die Bereiche, in denen die Clips auf der Bauplatte nicht zulässig sind.](../../../articles/images/machine_disallowed_areas.png)

Diese Einstellung gilt nur für die *aktive Düse*, d. h., Sie können weiterhin Objekte neben diesen nicht zugelassenen Bereichen drucken, auch wenn sich dadurch andere Düsen über diese nicht zugelassenen Bereiche bewegen würden. Diese Einstellung ist also nur für Drucker sinnvoll, die die inaktiven Düsen anheben oder außerhalb des Bauvolumens parken, wenn sie inaktiv sind. Im Gegensatz zu den normalen [Unzulässigen Bereichen](machine_disallowed_areas.md) werden diese unzulässigen Bereiche nicht in Abhängigkeit vom Versatz zwischen den Düsen verschoben.

Diese unzulässigen Bereiche sind notwendig, um zu verhindern, dass die Düse mit Dingen kollidiert. Beispielsweise können sich auf der Bauplatte einige Clips, ein Aufkleber oder ein Logo befinden. Wenn der Benutzer zu nahe an diesen Objekten drucken würde, würde die Düse mit ihnen kollidieren. Im besten Fall kommt es zu einer [Schichtverschiebung](../troubleshooting/layer_shift.md). Im schlimmsten Fall würde die Düse oder das Objekt, mit dem die Düse kollidiert, beschädigt.

Die unzulässigen Bereiche werden als graue Flächen auf die Bauplatte gezeichnet, um dem Benutzer anzuzeigen, dass er dort keine Objekte platzieren kann. Diese Flächen können in alle Richtungen ausgedehnt werden, um zu verhindern, dass der Brim oder der Skirt darauf trifft, und aus verschiedenen anderen Gründen. Es gibt auch andere Schattierungen auf der Bauplatte, zum Beispiel um den Bewegungsbereich zu begrenzen, wenn die Düsen einen Versatz haben.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**