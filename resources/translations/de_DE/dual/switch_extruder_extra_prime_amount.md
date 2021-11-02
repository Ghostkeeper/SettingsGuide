Zusätzliche Einzugsmenge bei Düsenwechsel
====
Mit dieser Einstellung können Sie den Drucker so konfigurieren, dass er jedes Mal, wenn der Extruder gewechselt wird, ein wenig zusätzliches Material abgibt. Damit soll der Druck auf die Düse wiederhergestellt werden, nachdem sie während des Drucks anderer Extruder oder während eines Extruderwechsels ausgelaufen ist.

Während andere Extruder drucken, hat dieser Extruder auf Stand-by gewartet. Während dieser Zeit wird er jedoch Material absondern. Dieser Materialverlust kann ausgeglichen werden, indem etwas zusätzliches Material durchgedrückt wird. Dadurch wird der Druck in der Düsenkammer wieder aufgebaut. Das Material, das herausgesickert ist, befindet sich jedoch immer noch an der Düsenspitze. Wenn also kein [Einzugsturm](prime_tower_enable.md) oder [Sickerschutz](ooze_shield_enabled.md) verwendet wird, landet es auf der Seite des Drucks. 

**Diese Einstellung ist pro Extruder konfigurierbar. Die konfigurierte Materialmenge wird am *Anfang* des jeweiligen Extruderplans abgelassen, bevor mit dem Material gedruckt wird.**