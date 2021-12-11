Extruder teilen sich eine Düse
====
Mit dieser Einstellung können Sie angeben, dass Ihr Drucker nur eine einzige Düse hat und das gesamte Filament durch dieselbe Düse gedrückt wird. Cura wird dann seine Vorbereitungsstrategie ändern.

Normalerweise geht Cura davon aus, dass nach der Ausführung des [Start G-Code](machine_start_gcode.md) alle Extruder ihr Filament an der Düsenspitze haben und bereit sind zu drucken. Wenn sich die Extruder eine Düse teilen, ist dies nicht möglich, da sich immer nur ein Filament in der Düse befinden kann. Anstelle der normalen Vorbereitungsprozedur mit einem [Einzugstropfen](../platform_adhesion/prime_blob_enable.md) oder zusätzlichen Skirt-Linien muss die Düse wie bei einem vollständigen Extruderwechsel vorbereitet werden. Dies beinhaltet das Drucken im [Einzugsturm](../dual/prime_tower_enable.md), falls aktiviert.

Wenn sich alle Extruder eine Düse teilen, ist es naheliegend, dass sie sich auch eine Heizung [teilen](machine_extruders_share_heater.md). Cura stellt jedoch von sich aus keine Verbindung zwischen den beiden her. Stellen Sie also sicher, dass Sie beides aktivieren, wenn Ihr Drucker tatsächlich eine einzelne Düse und eine einzelne Heizung für alle Extruder hat.

**Da es sich hierbei um eine Geräteeinstellung handelt, wird sie normalerweise nicht in der normalen Liste der Einstellungen aufgeführt. Es gibt jedoch ein Kontrollkästchen für diese Einstellung im Dialogfeld "Druckereinstellungen", das Sie in der Liste der hinzugefügten Drucker im Dialogfeld "Einstellungen" finden.**