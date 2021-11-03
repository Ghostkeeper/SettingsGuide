Höhe stufenweise Füllungsschritte
====
Bei der stufenweisen Füllung wird die Dichte der Füllung in mehreren Schritten von oben nach unten reduziert. Bei jedem Schritt wird die Dichte der Füllung halbiert. Diese Einstellung gibt die Höhe dieser Stufen an, also den Abstand zwischen zwei Stellen, an denen die Füllung halbiert wird.
![Höhe der stufenweise Füllungsschritte 1.5mm](../../../articles/images/gradual_infill_step_height_small.png)
![Höhe der stufenweise Füllungsschritte of 5mm](../../../articles/images/gradual_infill_step_height_large.png)

Bei stufenweise Füllungsschritten bleibt naturgemäß ein Teil der Füllung in der Luft hängen. Dies korrigiert sich jedoch normalerweise von selbst. Die erste Schicht der Füllung hängt in der Luft und haftet nur an den Seiten des Drucks richtig. Die darüber gelegten Schichten können sich an den Enden ein wenig auf der vorherigen Schicht abstützen, hängen aber in der Mitte durch. Dies wird allmählich besser, Schicht für Schicht.

* Verringern Sie die Schrittgröße für die stufenweise Füllung, um schnell zu einer niedrigen Fülldichte zu gelangen. Dies spart Druckzeit und Materialverbrauch.
* Erhöhen Sie die Schrittgröße für die stufenweise Füllung, wenn die Füllung nicht genug Platz hat, um sich selbst zu korrigieren, wenn der nächste Schritt in der Fülldichte erfolgt. Wenn Sie den Wert dieser Einstellung erhöhen, wird der Druck zuverlässiger.