Ausspüldauer
====
Wenn der Drucker das Filament für eine Düse wechseln muss, muss er das restliche Material, das sich noch in der Düsenkammer befindet, ausspülen. Diese Einstellung bestimmt, wie viel Material zum Ausspülen des vorherigen Materials verwendet wird.

Dies gilt nur für die Zeit nach dem Wechsel zu einem anderen Materialtyp. Wenn dieselbe Materialart erneut geladen wird (z. B. weil die vorherige Spule leer war), wird eine andere [Ausspüldauer am Ende des Filaments](material_end_of_filament_purge_length.md) verwendet.

**Diese Einstellung ist derzeit nicht in Curas Oberfläche sichtbar. Sie kann nur von den Profilen gesetzt werden. Sie wird auch nicht von Cura beim Slicen verwendet. Drucker, die das Materialdateiformat von Cura verstehen, können es jedoch verwenden, um ihre Filament-Wechselprozedur korrekt zu konfigurieren.** 
Durch ein Post-Processing-Skript kann der Befehl `M600` in den Druck eingefügt werden, der einen Filament-Wechsel auslöst.