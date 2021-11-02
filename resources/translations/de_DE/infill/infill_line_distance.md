Linienabstand Füllung
====
Anstatt die [Fülldichte](infill_sparse_density.md) als Prozentsatz anzugeben, ist es auch möglich, die Fülldichte durch Festlegung des Abstands zwischen benachbarten Fülllinien zu konfigurieren. Ein größerer Abstand zwischen Fülllinien führt zu einer insgesamt geringeren Fülldichte.

Der Abstand zwischen den Fülllinien ist eine andere Art, diese Eigenschaft zu betrachten als die Fülldichte. Der Abstand zwischen den Fülllinien gibt den Abstand an, den die Linien der jeweiligen Oberfläche von einer Fülllinie zur nächsten zurücklegen müssen. Eine Verringerung des Fülllinienabstands verringert also den überbrückten Abstand und verbessert die Qualität der Oberflächen.

![4mm Abstand zwischen den Linien, was eine Fülldichte von 20% ergibt](../../../articles/images/infill_pattern_grid.png)
![8mm Abstand zwischen den Linien, was eine Fülldichte von 10% ergibt](../../../articles/images/infill_sparse_density_low.png)

Normalerweise wird der Fülllinienabstand aus der gewünschten Fülldichte berechnet, abhängig von dem gewählten Füllmuster und der Linienbreite. Der Fülllinienabstand hat Priorität.

Eine Erhöhung der Fülldichte (durch Verringerung des Linienabstands) hat große Auswirkungen auf Ihren Druck, nämlich
* Ihr Druck wird stabiler.
* Die Oberseite wird besser unterstützt, wodurch sie glatter und wasserdichter wird.
* Die Pillow-Effekte werden reduziert, da die Wärmeeinschlüsse kleiner sind.
* Ihr Druck benötigt mehr Material und ist daher schwerer.
* Es dauert länger, bis der Druck fertig ist.