Spaghetti-Füllung
====
Wenn diese Einstellung aktiviert ist, extrudiert Cura alle Füllungen mehrerer Schichten auf einmal in einer höheren Schicht. Dies ist eine extreme Form der Methode [Füllschichtdicke](../infill/infill_sparse_thickness.md), jedoch ohne das Ziel, die Festigkeit der Füllung zu erhalten. Es hat eine gewisse Funktionalität, um mit den extremen Mengen an Extrusion umzugehen.

Diese Funktion ist für normale Materialien nicht geeignet. Normalerweise wollen Sie entweder die Festigkeit gewöhnlicher Füllungsmuster oder Sie lassen die Füllung ganz weg. Es gibt jedoch zwei Anwendungsfälle für diese Funktion.

Anwendungsfälle
----
Bei flexiblen Materialien kann diese Technik sehr weiche Texturen erzeugen. Bei Spaghetti-Füllung entstehen in der Regel lose Ringe, die nicht gut aneinander haften. Diese Ringe sind in alle Richtungen gleichermaßen weich. Um diesen Effekt zu erzielen, darf die Dichte der Füllung jedoch nicht zu gering sein, da sonst alle Spaghetti auf dem Boden des Drucks landen. Es ist ratsam, einen [Spaghetti-Durchfluss](spaghetti_flow.md) zwischen 30% und 60% zu verwenden, je nach Linienbreite und Schichthöhe. Das Ergebnis ist eine Füllung, die in alle Richtungen gleich steif und einigermaßen weich ist.

Die andere Anwendung für die Spaghetti-Füllung ist das Gießen. Wenn Sie einen Drucker haben, der über ein Werkzeug zum Gießen an bestimmten Stellen verfügt, können Sie diese Funktion nutzen, um Ihr Modell mit kontrollierten Materialablagerungen ziemlich gleichmäßig aufzufüllen. In diesem Fall muss die [Fließdichte](spaghetti_flow.md) wahrscheinlich ungefähr 100 % betragen, abhängig vom Schrumpfungs-/Ausdehnungsverhältnis des Gussmaterials.

Anpassen anderer Einstellungen für Spaghetti-Füllung
----
Diese beiden Anwendungen erfordern eine ganz besondere Handhabung der Füllung. Hier sind einige Einstellungen, die Sie höchstwahrscheinlich an Ihre Bedürfnisse anpassen sollten:
* Die [Druckgeschwindigkeit der Füllung](../speed/speed_infill.md) muss massiv reduziert werden. Wenn die Düse die Füllung von 10 Schichten gleichzeitig extrudieren muss, sollten Sie die Druckgeschwindigkeit mindestens um den Faktor 8 verringern.
* Stellen Sie die [Dicke der Füllung](../infill/infill_sparse_thickness.md) so ein, dass sie der Höhe der Schicht entspricht.
* Erhöhen Sie die [Drucktemperatur](../material/material_print_temperature.md) leicht (für den Extruder, der die Füllung druckt). Dadurch kann das Material richtig aus der Düse fließen und die Extrusion wird beschleunigt.
* Setzen Sie die [Justierung der Z-Naht](../shell/z_seam_type.md) auf zufällig, um die Struktur zufällig zu verteilen.

**In der Schichtansicht von Cura wird die Füllung als sehr dicke Linien angezeigt. Das liegt daran, dass Cura davon ausgeht, dass das Material auf der gleichen Schicht bleibt und sich dort ausbreitet. In Wirklichkeit wird es nach unten fallen.**

**Wenn die Spaghetti-Füllung verwendet wird, hat die Einstellung [Breite der Fülllinien](../resolution/infill_line_width.md) keine Wirkung mehr. Die Linienbreite wird an die Anforderungen der Einstellungen [Linienabstand Füllung](../infill/infill_line_distance.md) und [Spaghetti-Durchfluss](spaghetti_flow.md) angepasst.**