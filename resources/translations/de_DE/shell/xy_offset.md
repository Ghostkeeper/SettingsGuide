Horizontale Erweiterung
====
Diese Einstellung bewirkt, dass das gesamte Modell etwas breiter oder schmaler wird. Es handelt sich um eine Ausgleichsmaßnahme für Maßungenauigkeiten des Druckprozesses.

<!--screenshot {
"image_path": "xy_offset_neutral.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": 0},
"colours": 32
}-->
<!--screenshot {
"image_path": "xy_offset_wider.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": 1},
"colours": 32
}-->
<!--screenshot {
"image_path": "xy_offset_slimmer.png",
"models": [{"script": "flipper_grip.scad"}],
"camera_position": [62, -91, 176],
"settings": {"xy_offset": -1},
"colours": 32
}-->
![Das originale Modell](../../../articles/images/xy_offset_neutral.png)
![Horizontal erweitert, die Schraubenlöcher sind jetzt kleiner](../../../articles/images/xy_offset_wider.png)
![Ein negativer Wert lässt das Modell schrumpfen und macht die Schraubenlöcher größer.](../../../articles/images/xy_offset_slimmer.png)

Ein positiver Wert macht den Druck fetter. Dadurch wird die Größe der Hohlräume verringert. Ein negativer Wert macht den Druck schlanker und erhöht die Größe der Hohlräume.

Wenn die Toleranz eines Drucks wichtig ist, kann diese Einstellung sehr nützlich sein. Aufgrund einer leichten Verformung von Kunststoffen stimmen die tatsächlichen Abmessungen des Drucks möglicherweise nicht vollständig mit den Abmessungen des digitalen Modells überein. Gain-Fehler können durch einfaches Skalieren des Modells auf der Bauplatte mit dem Skalierungswerkzeug ausgeglichen werden, aber Offset-Fehler aufgrund des Druckverfahrens, können mit dieser Einstellung kompensiert werden.

Wenn Sie wissen, dass Ihr Drucker aufgrund einer Überextrusion oder einer Ungenauigkeit in seiner Bewegung immer zu breit druckt, können Sie dies ebenfalls mit dieser Einstellung kompensieren.