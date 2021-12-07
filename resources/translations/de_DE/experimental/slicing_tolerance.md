Slicing-Toleranz
====
Mit der Slicing-Toleranz können Sie einstellen, wie mit der Ungenauigkeit der Unterteilung eines Netzes in eine begrenzte Anzahl von Schichten umgegangen werden soll. Sie können wählen, ob die Schichten sich der Oberfläche annähern, von der Oberfläche begrenzt bleiben oder die Oberfläche vollständig einschließen sollen.

Mitte
----
![Mitte](../../../articles/images/slicing_tolerance_middle.svg)

Bei der Verwendung von Mitte bleiben die Schichten so nah wie möglich an der Originaloberfläche. Das bedeutet, dass die Schichten manchmal über die Originaloberfläche hinausragen und manchmal in die Originaloberfläche eintauchen. Insgesamt wird das Volumen der Schichten dem Volumen des Originalnetzes sehr nahe kommen.

Um die mittlere Toleranz zu erhalten, berechnet Cura einen Querschnitt durch die Hälfte der Dicke jeder Schicht. Alles, was innerhalb des Querschnitts liegt, wird Teil der Schicht.

Inklusiv
----
![Inklusiv](../../../articles/images/slicing_tolerance_inclusive.svg)

Bei der Verwendung von Inklusiv enthalten die Schichten *mindestens* das gesamte ursprüngliche Volumen. Wenn die Oberfläche geneigt ist, werden die Schichten leicht überstehen. Das Gesamtvolumen der Schichten wird fast immer größer sein als das Volumen des ursprünglichen Netzes.

Um die Inklusive Toleranz zu erhalten, berechnet Cura Querschnitte am oberen und unteren Ende der Höhe jeder Schicht. Alle Flächen, die sich in *einem* dieser Querschnitte befinden, werden als Teil der Schicht betrachtet. Winzige Details, die zwischen den beiden Querschnitten liegen, werden weiterhin ignoriert, da sie kleiner als eine Schichthöhe sind.

Exklusiv
----
![Exklusiv](../../../articles/images/slicing_tolerance_exclusive.svg)

Bei der Verwendung von Exklusiv werden die Schichten im ursprünglichen Volumen enthalten sein. Wenn die Oberfläche geneigt ist, sind die Schichten etwas kleiner als das ursprüngliche Volumen. Das Gesamtvolumen der Schichten wird fast immer kleiner sein als das Volumen des Originalnetzes.

Um die Exklusiv Toleranz zu erhalten, berechnet Cura Querschnitte am oberen und unteren Ende der Höhe jeder Schicht. Nur Flächen, die sich in *beiden* dieser Querschnitte befinden, werden als Teil der Schicht betrachtet.

Verwendung
----
Diese Einstellung ist nach ihrem Verwendungszweck und nicht nach ihrer funktionalen Wirkung benannt. Wenn Sie mehrere Teile haben, die aneinander vorbeigeschoben werden müssen, kann die theoretische Form der Schichten eine exakte Passung physisch verhindern. In einem solchen Fall können Sie diese Einstellung auf Exklusiv setzen, damit die Schichten garantiert innerhalb der Grenzen des ursprünglichen Volumens bleiben. Abgesehen von Verformungen, Durchhängen und ähnlichen Deformationseffekten würde dies garantieren, dass die Teile ineinander passen und aneinander vorbeigleiten können.

In der Realität gibt es immer wieder andere Effekte, die dies verhindern. In der Praxis kann diese Einstellung verwendet werden, um etwas mehr oder weniger Toleranz zwischen zwei schrägen Flächen zu erreichen, wie in den obigen Bildern zu sehen ist.