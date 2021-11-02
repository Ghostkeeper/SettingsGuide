Schichtstart X
====
Wenn mehrere Teile auf eine Schicht gedruckt werden sollen, optimiert Cura die Reihenfolge, in der diese Teile gedruckt werden. Damit das Teil abkühlen kann, bevor die nächste Schicht gedruckt wird, wird jede Schicht in etwa in der gleichen Reihenfolge gedruckt. Die Einstellungen Schichtstart X und [Schichtstart Y](layer_start_y.md) bestimmen, welches Teil zuerst gedruckt wird: Das Teil, das den angegebenen Koordinaten am nächsten ist. Diese Einstellung bestimmt die X-Koordinate dieses Teils.

Dies ist eine andere Einstellung als die der Z-Naht. Die Einstellungen für die Z-Naht-Ausrichtung legen nur fest, wo der Drucker mit dem Druck der Kontur eines Teils beginnt, während diese Einstellung bestimmt, mit welchem Teil er beginnt.

Wenn Ihr Drucker beim Starten einer neuen Schicht oder beim Wechsel des Extruders etwas Bestimmtes tut, ist es eine gute Idee, diese Koordinaten auf die Position einzustellen, an der der Druckkopf endet, wenn er bereit ist, weiter zu drucken. Dadurch werden Fahrwege und Verschmutzungen minimiert.

Diese Koordinaten sind im G-Code-Koordinatensystem, das sich von dem Koordinatensystem unterscheidet, das Cura verwendet, um die Position von Objekten darzustellen.