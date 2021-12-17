Mindestzeit Standby-Temperatur
====
Mit dieser Einstellung wird die Mindestdauer einer Bereitschaft konfiguriert, in der die Düse auf Bereitschaftstemperatur abgekühlt wird. Wenn die Düse für eine kürzere Zeitspanne als diese Standby-Zeit eingestellt ist, wird sie nicht abgekühlt, sondern bleibt auf der [Endgültige Drucktemperatur](../material/material_final_print_temperature.md).

Ihre Düse verfügt über einen PID-Regler, der regelt, wie viel Energie zum Aufheizen Ihrer Düse verwendet wird, um die richtigen Temperaturen zu erreichen. Wenn die Düse mit großen Temperaturunterschieden in schneller Folge zum Abkühlen und Aufheizen angewiesen wird, neigt der PID-Regler dazu, die erforderliche Heizleistung falsch vorherzusagen. Dies führt zu starken Schwankungen in der tatsächlichen Düsentemperatur. Damit kann verhindert werden, dass die [Standby-Temperatur](../material/material_standby_temperature.md) erreicht wird, wenn die Düse für eine sehr kurze Zeit inaktiv ist.

Der optimale Wert für diese Einstellung hängt von der Einstellung Ihres PID-Reglers ab. Einige Regler kommen mit schnellen Änderungen der Zieltemperatur besser zurecht als andere, und diese können möglicherweise besser mit einer kurzen Standby-Periode umgehen. Eine niedrigere Einstellung würde dann dazu beitragen, dass sich das Material in der Düse nicht zersetzt.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**