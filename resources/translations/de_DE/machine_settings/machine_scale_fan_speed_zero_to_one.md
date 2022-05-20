Skalierung der Lüftergeschwindigkeit auf 0–1
====
Um die Geschwindigkeit, mit der sich die Lüfter des Druckers drehen, zu steuern, fügt Cura in den g-Code Befehle einen Parameter ein, der die Geschwindigkeit steuert. Normalerweise ist dieser Parameter eine Zahl zwischen 0 und 255. Manche Drucker akzeptieren aber auch eine Zahl zwischen 0 und 1 und interpretieren sie dann anders. Diese Einstellung bewirkt, dass Cura die Geschwindigkeit der Lüfter als eine Zahl zwischen 0 und 1 schreibt, anstatt zwischen 0 und 255.

Es gibt 3 verschiedene Verhaltensweisen der Firmware in den verschiedenen Druckern auf dem Markt.
* Die meisten Drucker akzeptieren die Lüftergeschwindigkeit nur als Zahl zwischen 0 und 255. Diese Einstellung sollte dann deaktiviert werden, da sich der Lüfter sonst nie richtig dreht.
* Einige Drucker (insbesondere RepRapFirmware) akzeptieren Zahlen zwischen 0 und 255, interpretieren aber Zahlen zwischen 0 und 1, wenn sie 1 oder niedriger sind. Diese Einstellung sollte dann aktiviert werden, da es sonst zu dem seltenen Fall kommen kann, dass Cura versucht, die Lüftergeschwindigkeit auf 0,4% (1 von 255) einzustellen, der Drucker sie aber stattdessen auf 100% setzt.
* Manche Drucker akzeptieren nur Zahlen zwischen 0 und 1. Diese Einstellung sollte dann ebenfalls aktiviert werden, sonst ist der Lüfter immer entweder ganz aus oder ganz an.