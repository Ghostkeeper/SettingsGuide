Rückzugstellung der gemeinsam genutzten Düse
====
Wenn die Extruder eines Druckers [eine Düse teilen](machine_extruders_share_nozzle.md), geht Cura nicht davon aus, dass alle Extruder mit dem Filament an der Düsenspitze beginnen. Diese Einstellung gibt an, wie weit das Filament von der Düse entfernt beginnt. Es kann sein, dass das Filament in einem anderen Abstand als dem [Düsenwechsel Einzugsabstand](../dual/switch_extruder_retraction_amount.md) beginnt, weil das Filament möglicherweise weiter weg gelagert wurde, während der Drucker inaktiv war, als wenn der Extruder während des Druckens bereitsteht.

![Abstand des inaktiven Filaments vor dem Drucken](../../../articles/images/machine_extruders_shared_nozzle_initial_retraction.svg)

Cura verwendet dies, um sicherzustellen, dass das Filament an der Düsenspitze ist, bevor es mit der Materialbereitstellung für den ersten Extruderwechsel beginnt.