Maximale Abweichung der Extrusionsfläche
====
Wenn Sie Linien mit unterschiedlichen Breiten drucken, ist es üblich, dass eine Linie zu einem ihrer Endpunkte hin allmählich dünner wird. Diese Einstellung bestimmt die Schrittgröße, mit der diese Linien dünner oder breiter werden, indem sie steuert, wie nah die Linien an dem Bereich bleiben müssen, den sie idealerweise abdecken sollten.

<!--screenshot {
"image_path": "meshfix_maximum_extrusion_area_deviation_high.png",
"models": [{"script": "twisted_triangular_hole.scad"}],
"camera_position": [0, 0, 60],
"settings": {
	"meshfix_maximum_resolution": 0.5,
	"meshfix_maximum_extrusion_area_deviation": 2000
},
"colour_scheme": "line_width",
"colours": 128
}-->
<!--screenshot {
"image_path": "meshfix_maximum_extrusion_area_deviation_low.png",
"models": [{"script": "twisted_triangular_hole.scad"}],
"camera_position": [0, 0, 60],
"settings": {
	"meshfix_maximum_resolution": 0.05,
	"meshfix_maximum_extrusion_area_deviation": 20
},
"colour_scheme": "line_width",
"colours": 128
}-->
![Geringere Auflösung, wenn eine hohe Abweichung zugelassen wird](../../../articles/images/meshfix_maximum_extrusion_area_deviation_high.png)
![Glatte Linienbreite, wenn geringe Abweichung erforderlich ist](../../../articles/images/meshfix_maximum_extrusion_area_deviation_low.png)

G-Code-Befehle können den Drucker nicht anweisen, eine Zeile mit einer variablen Breite zu drucken. Er muss Zeilen mit einer festen Breite drucken. Cura kann eine Zeile in mehrere Segmente mit allmählich wechselnder Breite aufteilen. Dadurch werden jedoch viele Zeilensegmente beim Drucken hinzugefügt. Die CPU des Druckers ist möglicherweise nicht in der Lage, all diese Anweisungen während des Drucks zu verarbeiten. Mit dieser Einstellung wird der Detailgrad der Liniensegmente mit variabler Breite gewählt. Eine höhere Auflösung (geringere Abweichung) führt theoretisch zu genaueren Linien, erhöht aber auch die Anzahl der Anweisungen erheblich.

Während es in der Schichtansicht schön aussieht, wenn sich die Breite einer Linie allmählich ändert, hat dies praktisch keine Auswirkungen auf den tatsächlichen Druck. Physikalische 3D-Drucker passen ihre Durchflussrate nicht genau genug an, um eine Verbesserung zu sehen, wenn die Auflösung hier erhöht wird. Unter normalen Umständen sollte diese Einstellung so hoch sein, dass sie niemals einen begrenzenden Faktor für die Auflösung des G-Codes darstellt. Auf diese Weise wird die Gefahr eines bufferunderruns minimiert.