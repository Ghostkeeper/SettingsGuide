Maximale Beschleunigung Filament
====
Diese Einstellung gibt die maximale Beschleunigung an, die die Feedermotoren Ihres Druckers gemäß der Firmware des Druckers bewältigen können.

Diese Einstellung wird nur verwendet, um korrekte Zeitschätzungen zu erhalten. Die von Cura eingestellte [Druckbeschleunigung](../speed/acceleration_print.md) hat keinen Grenzwert, aber Cura nimmt an, dass Ihre Firmware einen bestimmten Grenzwert pro Achse festlegt. Wenn die Beschleunigung für den Feeder diese Einstellung überschreitet, wird die Zeitschätzung dieser Bewegungen angepasst, um anzunehmen, dass Ihre Firmware die Beschleunigung begrenzt. Die Gesamtbeschleunigung kann immer noch größer sein, wenn mit mehreren Achsen gleichzeitig diagonal beschleunigt wird.

Es kommt häufig vor, dass die Beschleunigungsgrenzen für den Feeder erreicht werden, da (je nach Firmware) die von Cura eingestellte Beschleunigung auch den Feeder beeinflusst. Es ist also entscheidend, dass diese Einstellung korrekt konfiguriert ist, um korrekte Zeitschätzungen für Rückzüge zu erhalten.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**