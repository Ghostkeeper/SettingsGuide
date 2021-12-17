X-Endanschlag in positiver Richtung
====
Diese Einstellung teilt Cura mit, in welche Richtung sich der Drucker entlang der X-Achse bewegen soll, wenn er den Befehl zum Ausrichten erhält. Wenn diese Einstellung deaktiviert ist, wird angenommen, dass der Endanschlag für die X-Achse an der Null-Koordinate (oder negativen Koordinate) des Bauvolumens liegt. Wenn die Einstellung aktiviert ist, wird davon ausgegangen, dass sich der Endanschlag für die X-Achse an der maximalen X-Koordinate des Druckers befindet. Wenn der Drucker startet, muss er sich in Richtung dieser Endanschläge bewegen, damit der Drucker weiß, wo sich der Druckkopf befindet.

Diese Einstellung wird von Cura überhaupt nicht verwendet. Sie wird jedoch vom X3GWriter-Plugin verwendet, um den G-Code-Befehl für die Referenzfahrt beim Schreiben einer X3G-Werkzeugpfaddatei korrekt umzusetzen.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**