Temperatursteuerung der Düse aktivieren
====
Wenn diese Einstellung deaktiviert ist, gibt Cura keine Temperaturbefehle an den G-Code aus. Stattdessen überlässt Cura es der Firmware des Druckers, die Düsen vor dem Druck aufzuheizen.

Die Funktionsweise ist ähnlich wie bei [beheizte Druckplatte](machine_heated_bed.md). Wenn diese Einstellung deaktiviert ist, werden die Temperatursteuerungseinstellungen wie [Drucktemperatur](../material/material_print_temperature.md) dem Benutzer nicht angezeigt.

Die vorübergehende Deaktivierung könnte dazu dienen, einen Trockenlauf des Drucks durchzuführen. Dazu müssten Sie auch die [beheizte Druckplatte](machine_heated_bed.md), die [Temperaturstabilisierung für den Druckraum](machine_heated_build_volume.md) und die [Flussrate](../material/material_flow.md) auf 0 % setzen.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**