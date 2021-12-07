Mindestumfang Polygon
====
Cura entfernt normalerweise Details des Modells, die kleiner sind als das, was die Düse sinnvollerweise drucken kann. Mit dieser Einstellung können Sie diesen Schwellenwert anpassen, um mehr oder weniger Details zu entfernen. Diese Einstellung misst den Umfang jeder Form auf jeder Schicht und wenn er kleiner als der Wert dieser Einstellung ist, wird diese Form nicht gedruckt.

Es ist sinnvoll, Details zu entfernen, die kleiner als eine Linienbreite sind. Dies beschleunigt das Slicing etwas. Dies gilt jedoch nicht immer für Teile, die kleiner als die [Breite der äußeren Wandlinien](../resolution/wall_line_width_0.md) sind, wenn die Funktion [Drucken von dünnen Wänden](../shell/fill_outline_gaps.md) aktiviert ist. Wenn noch sehr kleine Stücke gedruckt werden sollen, können Sie diese Einstellung verkleinern.

Eine Erhöhung dieser Einstellung kann auch dazu beitragen, kleine Details zu entfernen und einen schnelleren Druck zu erzielen. Wenn diese kleinen Details nicht gedruckt werden müssen, kann man sich einige Fahrbewegungen sparen, um sie zu erreichen.