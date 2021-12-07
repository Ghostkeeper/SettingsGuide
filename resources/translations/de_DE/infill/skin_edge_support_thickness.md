Stützenstärke für Außenhautkanten
====
Beim Drucken von konkaven Formen entsteht eine Außenhaut, die irgendwo in der Mitte der Füllung endet. Diese Einstellung fügt eine zusätzliche Linie durch die Füllung hinzu, um die Kante der Außenhaut zu unterstützen, so dass sie etwas weniger durchhängt.

![Unter dem Rand der Außenhaut wird eine Begrenzung durch die Füllung gezogen](../../../articles/images/skin_edge_support_thickness.png)

Eine einzelne Linie durch die Lücken in der Füllung wird immer noch durchhängen, daher kann die Linie auf mehreren Schichten unterhalb der Kante der Außenhaut, die unterstützt werden muss, gezeichnet werden. Mit dieser Einstellung wird die vertikale Dicke der Linie unterhalb des Randes der Außenhaut eingestellt. Alternativ können Sie auch direkt die [Anzahl der Schichten](skin_edge_support_layers.md) unterhalb der Kante der Außenhaut einstellen, auf der diese Linie gezeichnet wird.

Eine Erhöhung hat im Allgemeinen folgende Auswirkungen auf den Druck:
* Der Rand der Außenhaut wird besser unterstützt, was zu einer glatteren Oberseite führt, da die Außenhaut vollständig von einer Seite zur anderen überbrückt werden kann.
* Der Druckvorgang dauert etwas länger und es wird mehr Material verbraucht.

Wenn die Füllrate hoch ist, hat diese Einstellung kaum Auswirkungen auf die Oberseite und kann zu [Überextrusion](../troubleshooting/overextrusion.md) in der Füllung führen. Am besten belassen Sie es dann bei 0 Schichten.