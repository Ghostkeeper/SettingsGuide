Präferenz Nahtkante
====
Mit dieser Einstellung können Sie steuern, wie die Nähte im Verhältnis zu den Ecken Ihres Modells positioniert werden.

Im Allgemeinen gibt es zwei Möglichkeiten, wo die Naht platziert werden kann: verdeckt in einer Innenecke oder offen in einer Außenecke. Das Verstecken der Naht in einer Innenecke ist im Allgemeinen vorzuziehen, da die Naht dort kaum sichtbar ist. Es ist aber auch möglich, sie an einer Außenecke anzubringen, so dass Sie die Naht mit einem Messer entfernen oder mit etwas Schleifpapier glatt schleifen können, wenn das Teil nachbearbeitet werden kann.

Dies sind die verfügbaren Optionen für diese Einstellung und ihre Auswirkungen.
* **Keine:** Es gibt keine bevorzugte Ecke. Die Naht wird so gewählt, dass sie den Anforderungen für die [Justierung der Z-Naht](z_seam_type.md) am besten entspricht.
* **Naht verbergen:** Dadurch wird die Naht bevorzugt in einer Innenecke versteckt. Wenn Justierung der Z-Naht auf "Schärfste Kante" eingestellt ist, wird immer die innerste Ecke gewählt. Wenn sie auf "Kürzester" eingestellt ist, wird eine Innenecke gewählt, die sich in der Nähe der aktuellen Position der Düse befindet, wenn sie die Kontur beginnt.
* **Naht offenlegen:** Dadurch wird die Naht bevorzugt an einer Außenecke freigelegt. Wenn die Justierung der Z-Naht auf "Schärfste Kante" eingestellt ist, wird immer die schärfste Außenecke gewählt. Wenn sie auf "Kürzeste" eingestellt ist, wird eine Außenecke gewählt, die sich in der Nähe der aktuellen Position der Düse befindet, wenn sie die Kontur beginnt.
* **Naht verbergen oder offenlegen:** Dadurch wird eine Naht an einer scharfen Kante erzeugt, unabhängig davon, ob es sich um eine Innen- oder Außenecke handelt, solange sie nicht an einer flachen Wand liegt.
<!--if cura_version >= 4.2 -->
* **Intelligent verbergen:** Dies platziert die Naht an einer scharfen Kante, genau wie "Naht verbergen oder offenlegen", aber es werden eher Innenecken als Außenecken bevorzugt, wenn in der Kontur eine Innenecke vorhanden ist. Wenn es keine Innenecken gibt, wird eine Außenecke gewählt..<!--endif-->