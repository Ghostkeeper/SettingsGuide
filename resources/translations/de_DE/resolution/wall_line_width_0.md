Breite der äußeren Wandlinien
====
Die Breite der äußeren Wandlinien kann getrennt von den inneren Wandlinien eingestellt werden. Diese Einstellung gibt an, wie breit die äußere Wandlinie sein wird.

<!--screenshot {
"image_path": "wall_line_width_0.png",
"models": [{"script": "hive.scad"}],
"camera_position": [-31, -31, 147],
"settings": {
    "wall_line_count": 2,
    "wall_line_width_0": 0.8
},
"colours": 64
}-->
![Die Kontur der Außenwand ist viel breiter als der Rest](../../../articles/images/wall_line_width_0.png)

Die Reduzierung der äußeren Wandlinienbreite, ein klein wenig unterhalb der Düsengröße, ist bekanntermaßen vorteilhaft für die Festigkeit. Die Düse wird etwas weniger Material extrudieren, aber ihre Öffnung wird sich mit den angrenzenden Wandlinien überlappen. Dies führt dazu, dass das Material von der zuvor platzierten Wand an die gewünschte Stelle gedrückt wird. Das führt aber auch dazu, dass der Kunststoff besser mit den angrenzenden Wänden verschmilzt. Dadurch können die Wände besser miteinander verschmelzen, so dass sie ihre Stärke verbinden können. Dadurch wird die Festigkeit der Wände erheblich verbessert.

Die Reduzierung der Breite der Außenwandlinie ermöglicht es der Düse auch, feinere Details zu drucken, da die dünnere Linie sich besser in kleine Details einfügt.

Die Erhöhung der Breite der Außenwandlinien kann die Druckzeit verkürzen. Sie können eine Wand mit ähnlicher Dicke und weniger Innenwänden erreichen. Die Festigkeit wird dennoch etwas verringert, da die Außenwände nicht so gut mit den Innenwänden verschmelzen.

Linien passend machen
----
Beim Drucken von dünnen Objekten ist die Anpassung der Wandlinienbreite ein wichtiges Werkzeug, um genaue und stabile Modelle zu erhalten. Cura zeichnet immer nur vollständige Konturen, wenn also eine Kontur nicht passt, entsteht eine Lücke in den Wänden, was die Festigkeit und Genauigkeit des Objekts stark beeinträchtigt.

Cura wird versuchen, solche Lücken zwischen den Wänden zu füllen, wenn [Lücken zwischen Wänden füllen](../../../articles/shell/fill_perimeter_gaps.md) aktiviert ist, aber diese Technik ist nicht ideal für jede beliebige Form und benötigt oft viel Druckzeit. Wenn sich zwei Wände überlappen, reduziert die Funktion [Wandüberlappungen ausgleichen](../../../articles/shell/travel_compensate_overlapping_walls_enabled.md) die Breite der Wandlinien, um sicherzustellen, dass das Bauteil maßhaltig ist, was jedoch Veränderungen des Flusses zur Folge hat, die ebenfalls die Qualität und Festigkeit des Drucks verringern.

Für eine ideale Passform sollte das Bauteil ein exaktes Vielfaches der Wandlinienbreite haben, damit die Wände genau in das Bauteil passen. Wenn Sie wissen, wie breit Ihr Bauteil ist, lässt sich dies durch Anpassen der Wandbreite leicht bewerkstelligen. Zuerst sehen Sie, wie viele Konturen Sie einpassen wollen, damit die Linien noch eine vernünftige Breite haben. Dann können Sie feststellen, wie stark Sie die Breite der Wandlinien anpassen müssen, damit die Linien richtig passen. Denken Sie daran, dass Sie die [Breite der äußeren Wandlinien](wall_line_width_0.md) und die [Breite der inneren Wandlinien](wall_line_width_x.md) separat einstellen können. Zählen Sie sorgfältig, wie oft jede Art von Wand gezeichnet wird, um die Auswirkungen einer Änderung der Wandlinienbreite vorherzusagen.

Das Anpassen von Wandlinien ist eine wichtige Fähigkeit beim 3D-Druck, die erfahrene 3D-Druckeranwender von anderen unterscheidet. Es bedarf etwas Übung.