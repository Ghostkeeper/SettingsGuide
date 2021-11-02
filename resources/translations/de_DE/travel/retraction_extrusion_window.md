Fenster „Minimaler Extrusionsabstand“
====
Damit das Filament richtig bewegt werden kann, muss das Feederrad in das Filament greifen. Das Einziehen des Materials führt häufig dazu, dass das Feederrad das Filament so weit abnutzt, dass es das Filament nicht mehr richtig greifen kann. Diese Einstellung begrenzt die Anzahl der Einzüge innerhalb einer bestimmten Länge des Filaments, um diese Abnutzung zu verhindern.

Die Einziehvorgänge werden durch die Kombination aus [Maximale Anzahl von Einzügen](retraction_count_max.md) und dieser Einstellung begrenzt. Das Material darf innerhalb einer durch diese Einstellung des Fensters für die minimale Extrusionslänge angegebenen Länge des Filaments nicht weiter eingezogen werden als der Wert der maximalen Einzugsanzahl.

![Eine bestimmte Länge des Filaments, bei der die Anzahl der Einzüge begrenzt ist](../../../articles/images/retraction_count_max.svg)

Die Länge des Filaments, bei der die Anzahl der Einzüge begrenzt ist, ist ein sogenanntes Schiebefenster. Bei einer Fensterlänge von 3 mm und einer maximalen Anzahl von Rückzügen von 10 bedeutet dies beispielsweise, dass ein neuer Rückzug erlaubt ist, sobald der 10. vorherige Rückzug weiter als 3 mm zurück auf dem Filament erfolgt ist.

Durch die Vergrößerung des Extrusionsfensters wird die Anzahl der Einzüge effektiv reduziert. Das macht den Druck zuverlässiger, erhöht aber die Menge an Stringing und Blobs auf der Oberfläche. Dies ist besonders nützlich für weichere Materialien, die empfindlicher auf Abrieb reagieren.