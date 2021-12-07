Topografie
====
Der "Topografie"-Effekt entsteht, wenn eine geneigte Ober- oder Unterseite mit einer geringen Anzahl von Schichten gedruckt wird, so dass die Grenzen zwischen den Schichten weit genug voneinander entfernt und leicht zu erkennen sind. Er ist nach [topografischen Karten](https://en.wikipedia.org/wiki/Topographic_maps) benannt, bei denen die Höhenunterschiede in der Regel durch Höhenlinien angezeigt werden.

![Sie können die Kanten der Schichten deutlich erkennen](../../../articles/images/topography.jpg)

Dieser Effekt ist beim 3D-Druck allgegenwärtig und einer der einfachsten Wege, um zu erkennen, dass ein Objekt 3D-gedruckt wurde. Er kann zwar verhindert werden, aber die Produktivität wird dadurch in der Regel erheblich reduziert.

Schichtdicke
----
Da der Topografie-Effekt auftritt, wenn die Grenzen zwischen den Schichten sehr weit auseinander liegen, kann der Effekt durch eine Verringerung der [Schichtdicke](../resolution/layer_height.md) verhindert werden. Wenn die Schichtdicke verringert wird, führen die kleineren vertikalen Abstände zwischen den Schichten auch zu kleineren horizontalen Schritten, wodurch der Topographieeffekt reduziert wird. Die Verringerung der Schichthöhe erhöht jedoch die Druckzeit erheblich.

Anstatt die Schichthöhe für den gesamten Druck zu reduzieren, können Sie die Schichthöhe auch nur für die flachen Flanken des Drucks reduzieren, indem Sie [Anpassschichten](../experimental/adaptive_layer_height_enabled.md) verwenden. Dadurch wird der Topographieeffekt stark reduziert, während die Druckzeit nur minimal beeinflusst wird. Allerdings ist es dann schwieriger, den Druck auf andere Qualitäten abzustimmen, da die Abstimmung normalerweise von der Schichthöhe abhängt.

Modellanpassungen
----
Sie können auch in Erwägung ziehen, das Modell so zu drehen, dass es keine flachen Schrägen mehr im Druck gibt. Dies bedeutet jedoch in der Regel, dass Sie viel mehr Support für Ihr Modell drucken müssen, was die Produktivität ebenfalls verringert, und die Überhänge sehen möglicherweise nicht so gut aus.