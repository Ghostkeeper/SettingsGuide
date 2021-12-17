Brückeneinstellungen aktivieren
====
Wenn Ihr Modell einen Überhang hat, der auf beiden Seiten unterstützt wird, wird Cura dies erkennen und den überhängenden Bereich der Außenhaut modifizieren, um besser drucken zu können. Wenn diese Einstellung aktiviert ist, können Sie die Erkennung dieser überhängenden Bereiche und das daraus resultierende Verhalten so einstellen, dass sie besser überbrückt werden.

<!--screenshot {
"image_path": "bridge_settings_enabled_default.png",
"models": [
    {
        "script": "rack_straight.scad",
        "scad_params": ["length=40"]
    }
],
"camera_position": [0, 74, -137],
"colours": 32
}-->
<!--screenshot {
"image_path": "bridge_settings_enabled_enabled.png",
"models": [
    {
        "script": "stairwell.scad",
        "scad_params": ["steps=4", "width=10", "height=20"]
    }
],
"layer": 275,
"settings": {
    "bridge_settings_enabled": true
},
"camera_position": [-12, 28, 63],
"colours": 64
}-->

![Wenn eine Brücke erkannt wird, werden die Linien der Außenhaut so ausgerichtet, dass sie die Lücke so gut wie möglich überbrücken.](../../../articles/images/bridge_settings_enabled_default.png)
![Wenn die Brückeneinstellungen aktiviert sind, werden die Brückenlinien mit unterschiedlichen Einstellungen gedruckt](../../../articles/images/bridge_settings_enabled_enabled.png)

Normalerweise verwendet Cura eine recht rudimentäre Überbrückungstechnik. Cura erkennt überhängende Bereiche der Außenhaut, die an mehreren Seiten unterstützt werden. Die [Richtung dieser Außenhautlinien](../top_bottom/skin_angles.md) wird angepasst, um diese Bereiche automatisch zu überbrücken. Dadurch wird sichergestellt, dass der größtmögliche Teil des überhängenden Bereichs auf mehreren Seiten unterstützt wird, und die Druckqualität wird verbessert.

Wenn diese Einstellung aktiviert ist, können Sie dieses Verhalten jedoch noch genauer auf Ihre Anforderungen abstimmen. So können Sie die Einstellungen optimieren:
* Druckgeschwindigkeit
* Fließgeschwindigkeit
* Dichte (wie bei der Füllung, aber mit den Linien der Außenhaut)
* Lüftergeschwindigkeit
* bei den Wänden auch das Coasting.

Diese Einstellungen können sowohl für die Außenhaut, die eine Lücke überbrückt, als auch für die Wände separat angepasst werden. Wenn [Brücke hat mehrere Schichten](bridge_enable_more_layers.md) aktiviert ist, können sie auch für die zweite und dritte Schicht über dem überbrückten Spalt separat eingestellt werden. Außerdem kann man einstellen, welche Teile des Drucks als Überbrückungsbereiche angesehen werden, indem man den [Schwellenwert Stützstruktur Brücken-Außenhaut](bridge_skin_support_threshold.md) und eine [Mindestlänge für die Brückenwand](bridge_wall_min_length.md) einstellt.

Durch die Aktivierung der Überbrückungseinstellungen erhalten Sie eine bessere Kontrolle darüber, wie Brücken in Ihrem Druck behandelt werden. Wenn Sie die Überbrückungsparameter sehr gut einstellen, können Sie die Qualität Ihrer Überhänge und die Genauigkeit in vertikaler Richtung erheblich verbessern. Der einzige Nachteil ist, dass sich der Druck ebenso verschlechtern kann, wenn Sie die Brückeneinstellungen nicht für Ihren Drucker anpassen.