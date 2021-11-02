Maximale Anzahl von Einzügen
====
Das Feederrad muss in das Filament greifen, um es richtig zu bewegen. Das Einziehen des Materials führt häufig dazu, dass das Feederrad das Filament so weit abnutzt, dass es das Filament nicht mehr richtig greifen kann. Diese Einstellung begrenzt die Anzahl der Einzüge innerhalb einer bestimmten Länge des Filaments, um dies zu verhindern.

Die Einstellung gibt an, wie oft das Filament während der in der Einstellung [Fenster „Minimaler Extrusionsabstand“](retraction_extrusion_window.md) angegebenen Filamentlänge eingezogen werden darf. Alle weiteren Einzüge während dieses Zeitraums werden nicht eingezogen, sondern verlaufen einfach ohne Einzug.

![Visualisierung des Einziehens des Filaments über eine bestimmte Länge](../images/retraction_count_max.svg)

Die Länge des Filamentes, bei der die Anzahl der Einzüge begrenzt ist, ist ein dehnbares Fenster. Bei einer Fensterlänge von 3 mm und einer maximalen Anzahl von Rückzügen von 10 bedeutet dies, dass ein neuer Rückzug erlaubt ist, sobald der 10. vorherige Rückzug weiter als 3 mm zurück auf dem Filament erfolgt ist.

Durch die Verringerung der maximalen Anzahl der Einzüge wird das Abschleifen des Filaments verringert. Dies ist nützlich für weichere Materialien wie PVA. Allerdings erhöht sich dadurch auch das Stringing, da das Filament nicht mehr an einer Stelle eingezogen werden kann, an der dies offensichtlich erwünscht war.