Breite für das Entfernen der Außenhaut
====
Mit dieser Einstellung werden sehr dünne Streifen der Außenhaut entfernt und stattdessen durch Füllmaterial ersetzt.

Die Außenhaut wird nur dann entfernt, wenn sich daneben Füllmaterial befindet. Es wird also nicht die Außenhaut ganz oben oder unten im Druck entfernt, selbst wenn diese sehr dünn ist.

![Keine Entfernung der Außenhaut](../../../articles/images/skin_preshrink_original.png)
![Dünne Streifen werden entfernt](../../../articles/images/skin_preshrink_shrunk.png)

Die Außenhaut wird normalerweise überall dort erzeugt, wo sie sich vertikal in der Nähe des oberen oder unteren Randes des Objekts befindet. Dies ist nicht überall notwendig. Senkrechte Wände sind in der Regel stark genug, so dass die Außenhaut zwar normalerweise an den Eckpunkten der senkrechten Wände angebracht werden sollte, aber mit dieser Einstellung können Sie dies auslassen. Dies spart Druckzeit und Material.

Für die meisten Drucke ist die Einstellung auf eine Linienbreite von 1 oder 2 hilfreich, um die Druckzeit zu verkürzen. Wenn die Außenhaut für den Druck zu dünn wird, hinterlässt Cura zusätzlich eine Lücke an der Stelle, an der die Außenhaut hätte sein sollen (aber zu klein war). Die Füllung wird dann nicht richtig mit den Wänden verbunden. Wenn [Lücken zwischen Wänden füllen](../shell/fill_perimeter_gaps.md) aktiviert ist, werden diese Lücken aufgefüllt, allerdings benötigt diese Füllmethode mehr Zeit zum Drucken als die normale Außenhaut. Wenn Sie diese Einstellung mindestens auf die [Breite der oberen/unteren Linie](../resolution/skin_line_width.md) erhöhen, wird dies verhindert.

Wenn die Einstellung zu stark erhöht wird, können an der Ober- und Unterseite Lücken entstehen, in denen die Füllung sichtbar wird. Seien Sie vor allem bei Modellen mit dünnen Leisten vorsichtig, bei denen ein dünner Streifen Außenhaut erforderlich ist.

![Diese Stücke der Außenhaut werden entfernt und die Füllung wird sichtbar.](../../../articles/images/skin_preshrink_problem.svg)
![Die Füllung ist auch in der Schichtansicht zu sehen](../../../articles/images/skin_preshrink_problem_screenshot.png)
