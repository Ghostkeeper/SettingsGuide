Abwechselnde Zusatzwände
====
Bei dieser Einstellung wird in jeder zweiten Schicht eine zusätzliche Wand hinzugefügt. Auf diese Weise wird die Füllung vertikal zwischen den Wänden eingeklemmt, was zu einem stärkeren Druck führt.

Wenn Sie z. B. die Anzahl der Wandlinien auf zwei Wände einstellen und die zusätzliche Wand aktivieren, werden auf geradzahligen Schichten zwei Wände und auf ungeradzahligen Schichten drei Wände gedruckt.

<!--screenshot {
"image_path": "alternate_extra_perimeter.gif",
"models": [
    {
        "script": "gear.scad",
        "transformation": ["scale(0.7)"]
    }
],
"camera_position": [0, 30, 123],
"settings": {
    "zig_zaggify_infill": true,
    "alternate_extra_perimeter": true
},
"layer": [15, 16, 17, 18],
"minimum_layer": [15, 16, 17, 18],
"colours": 32
}-->
![Dieses Bild zeigt die Wände, die von der Änderung dieser Einstellung betroffen sind.](../../../articles/images/alternate_extra_perimeter.gif)

Die Aktivierung dieser Einstellung kostet zusätzliche Zeit, etwa halb so viel wie das Hinzufügen einer zusätzlichen Wand. In mancher Hinsicht ist diese alternierende zusätzliche Wand fast so gut wie eine vollständige zusätzliche Wand, in mancher Hinsicht ist sie es nicht:
* Sie erhöht den Verbund zwischen der Füllung und den Wänden erheblich, da die Füllungslinien auch senkrecht an der zusätzlichen Wand über und unter ihnen haften können. In dieser Hinsicht übertrifft die zusätzliche Wand ihre eigene Gewichtsklasse. Sie ist sehr effizient. 
* Sie erhöht die Steifigkeit des Drucks um mehr als die Hälfte einer zusätzlichen Wand. Indem sie sich an die angrenzende Wand bindet, verteilt sie die Spannung auf mehr Stränge und bietet einen größeren Schutz gegen Kräfte in horizontaler Richtung. Die alternierende zusätzliche Wand hat dabei weder einen besonderen Vorteil noch einen besonderen Nachteil.
* Eine echte zusätzliche Wand würde auch die Festigkeit des Schichtverbundes erhöhen. Wände werden langsam gedruckt und sind daher eine wichtige Quelle für die Stärke des Schichtverbunds. Die alternierende zusätzliche Wand verbindet sich jedoch nicht mit den angrenzenden Schichten, da sie nur in jeder zweiten Schicht auftritt.

Folglich ist die alternierende Zusatzwand ein effizienter Weg, um die horizontale Steifigkeit zu erhöhen, aber kein effizienter Weg, um die vertikale Zähigkeit zu erhöhen.