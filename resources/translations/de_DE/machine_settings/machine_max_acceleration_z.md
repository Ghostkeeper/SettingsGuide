Maximum Acceleration Z
====
Diese Einstellung gibt die maximale Beschleunigung an, die der Motor und der Rahmen Ihres Druckers in Z-Richtung gemäß der Firmware des Druckers bewältigen können.

Diese Einstellung wird nur verwendet, um korrekte Zeitschätzungen zu erhalten. Die von Cura eingestellte [Druckbeschleunigung](../speed/acceleration_print.md) hat kein Limit, aber Cura geht davon aus, dass Ihre Firmware ein bestimmtes Limit pro Achse setzt. Wenn die Beschleunigung in der Z-Achse diese Einstellung überschreitet, wird die Zeitschätzung dieser Bewegungen angepasst, um anzunehmen, dass Ihre Firmware die Beschleunigung begrenzt. Die Gesamtbeschleunigung kann immer noch größer sein, wenn mit mehreren Achsen gleichzeitig diagonal beschleunigt wird.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**