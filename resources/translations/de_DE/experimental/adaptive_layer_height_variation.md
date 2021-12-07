Maximale Abweichung für Anpassschichten
====
Mit dieser Einstellung können Sie den Bereich begrenzen, aus dem die Adaptiven Schichten eine Schichtdicke auswählen dürfen. Die Schichthöhe darf nicht mehr als diese Variation von der normalen [Schichthöhe](../resolution/layer_height.md) abweichen.

Bei einer normalen Schichthöhe von 0,15 mm und einer Variation von 0,1 mm kann Adaptive Layers beispielsweise Schichten mit einer Dicke zwischen 0,05 mm und 0,25 mm erzeugen.

Diese Einstellung schränkt die Leistungsfähigkeit der Funktion "Adaptive Schichten" ein. Wenn der Bereich der Schichtdicken zu eng ist, wird die Schichtdicke immer sehr nahe an der ursprünglichen Schichtdicke liegen, die durch die Einstellung der Schichthöhe festgelegt wurde. Die Funktion "Adaptive Schichten" trägt dann nicht viel zur Zeitersparnis oder Qualitätsverbesserung bei.

Ist der Bereich jedoch sehr groß, können die Schichten sehr dick oder sehr dünn werden. Sehr dicke Schichten erfordern einen starken Ausfluss aus der Düse, was aufgrund der begrenzten Düsengröße und Schmelzkapazität der Heizbahn im Druckkopf nicht immer möglich ist. Sehr dünne Schichten sind aufgrund der Viskosität des Materials oder der Ungenauigkeit der Z-Achse ebenfalls nicht immer möglich. Daher ist es sinnvoll, den Bereich, in dem Adaptive Layers die Schichtdicke einstellen kann, zu begrenzen. Andernfalls wird der Drucker Schwierigkeiten haben, die gewünschte Schichtdicke zu erreichen.

Die Schichtdicke kann niemals unter 0,001 mm sinken, auch wenn der Bereich dies zulassen würde.