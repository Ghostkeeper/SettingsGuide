Gerätekopf und Lüfter Polygon
====
Diese Einstellung teilt Cura mit, wie die Form Ihres Druckkopfes von oben gesehen ist. Dies ist notwendig, um Kollisionen beim Drucken im [Nacheinander Modus](../blackmagic/print_sequence.md) zu vermeiden.

![Abmessungen des Druckkopfes](../../../articles/images/head_dimensions.svg)
![Von oben gesehen, ist die Form des Druckkopfes relativ zur Düsenposition](../../../articles/images/machine_head_with_fans_polygon.png)

Diese Einstellung enthält eine Liste von Koordinaten, die ein Polygon bilden. Die Koordinaten sind relativ zur "Position" des Kopfes, zu der auch die Düsen relativ positioniert sind.

Cura verwendet dies, um einen Kollisionsbereich um die Objekte zu erstellen, die Sie im  "Nacheinander" Modus drucken. Dieser Kollisionsbereich verhindert, dass die Objekte zu nahe beieinander liegen, so dass sie nicht gedruckt werden können, ohne dass der Druckkopf mit dem zuvor gedruckten Modell zusammenstößt. Der Kollisionsbereich hat jedoch nicht die gleiche Form wie der Druckkopf selbst: Er ist eine konvexe Hülle um den Druckkopf, um Kollisionen auch bei Fahrbewegungen zu verhindern. Außerdem wird er reduziert, um symmetrisch zu sein. Befindet sich die Düse beispielsweise mehr auf der linken Seite des Druckkopfs (wie im obigen Bild), wird der Kollisionsbereich so verkleinert, dass ein anderes Objekt nahe der rechten Seite der bereits gedruckten Objekte platziert werden kann. Die Reihenfolge, in der diese Objekte gedruckt werden, wird dann so angepasst, dass sie ohne Kollisionen gedruckt werden können.

**Da es sich hierbei um eine Geräteeinstellung handelt, wird sie normalerweise nicht in der normalen Liste der Einstellungen aufgeführt. Die Größe des Druckkopfes kann jedoch grob im Dialog für die Druckereinstellungen notiert werden, der sich in der Liste der hinzugefügten Drucker im Einstellungsdialog befindet. Sie können dort nur die Position links, rechts oben und unten des Druckkopfes angeben.**