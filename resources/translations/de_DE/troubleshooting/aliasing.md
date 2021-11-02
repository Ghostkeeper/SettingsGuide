Aliasing
====
Schrittmotoren drehen sich in diskreten Schritten. Ihre Fähigkeit, in einer Position zwischen diesen Schritten zu ruhen, ist begrenzt. Die Schrittgröße der Motoren stellt eine Grenze für die Auflösung dar, die der Drucker erreichen kann. Beim Drucken von Wänden, die fast, aber nicht ganz an der X- oder Y-Achse ausgerichtet sind, zeigt sich diese Auflösung manchmal als ein Muster von Linien.

![Das Aliasing-Muster, das an den Seiten dieses Objekts zu sehen ist](../../../articles/images/aliasing.jpg)

Die Auflösung eines Schrittmotors in einem typischen Consumer-3D-Drucker liegt im Bereich von 50 bis 200 Schritten pro Millimeter. Das bedeutet, dass die Größe jedes Schritts in der Größenordnung von 10 Mikrometern liegt. Wenn eine Linie fast parallel zur anderen Achse gezogen wird, sagen wir 0,5° weg von der Orthogonalen, dann wird ein solcher Schritt alle 1,15 mm entlang der Linie auftreten. Dieser Schritt selbst ist zu klein, um sichtbar zu sein, aber die Schwingungen sind sichtbar, besonders wenn sie mit der Eigenfrequenz des Rahmens mitschwingen.

Vorbeugung
----
Schrittmotoren können zwischen mehreren Strategien wählen, um ihre Welle zu drehen, aber es ist ein Kompromiss zwischen Auflösung, Drehmoment und Geräusch. Einige Firmware passt dies automatisch basierend auf der Bewegungsgeschwindigkeit an. Manche Firmware erlaubt es Ihnen, dies auch über den G-Code einzustellen. Zum Beispiel kann der g-code Befehl `M350` im Start g-code platziert werden, um dies manuell zu konfigurieren. Cura hat (derzeit) keine Methode, dies automatisch auf Basis der Geschwindigkeit oder Struktur zu konfigurieren.

Der zuverlässigste Weg, dieses Phänomen zu verhindern, ist jedoch, das Modell so einzustellen, dass das Aliasing nicht sichtbar ist. Drehen Sie Ihr Modell so, dass der Aliasing-Effekt nicht auftritt. Wenn Ihr Modell eine (fast) gerade Wand hat, stellen Sie sicher, dass diese entweder komplett mit den Achsen ausgerichtet ist oder um einige Grad davon abgewinkelt ist.