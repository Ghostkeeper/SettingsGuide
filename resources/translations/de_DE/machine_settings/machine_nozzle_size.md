Düsendurchmesser
====
Mit dieser Einstellung wird der Durchmesser der Düsenöffnung gemessen, durch die das Material fließt.

![Abmessungen des Druckkopfes](../../../articles/images/head_dimensions.svg)

Dies ist ein wichtiges Maß, auf das sich andere Einstellungen beziehen können. Vor allem die [Linienbreite](../resolution/line_width.md) wird normalerweise auf der Grundlage der Düsengröße angepasst. Einige Druckerprofile begrenzen auch die Schichthöhe auf der Grundlage der Düsengröße, da die Düsengröße der wichtigste Faktor dafür ist, wie schnell das Material extrudiert werden kann.

Die Düsengröße wird auch direkt für ein Detail verwendet: Beim Füllen von [Lücken zwischen den Wänden](../shell/fill_perimeter_gaps.md) werden Linienstücke, die weiter als zwei Düsengrößen voneinander entfernt sind, nicht zusammengeführt.

Passen Sie die Düsengröße nicht an, es sei denn, Sie ändern die physische Düse tatsächlich. Einige Slicer (einschließlich Cura 15.04 und früher) verwenden den Begriff "Düsengröße" für die Breite der zu druckenden Linien. Cura verwendet dafür die Einstellung [Linienbreite](../resolution/line_width.md).

**Da es sich hierbei um eine Geräteeinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar. Wenn Ihr Drucker über spezifische Profile für die verfügbaren Düsen verfügt, können Sie diese im Menü "Druckereinrichtung" oben in der Mitte des Bildschirms auswählen. Andernfalls können Sie den Düsendurchmesser im Dialogfeld "Druckereinstellungen" einstellen, das Sie in der Liste der hinzugefügten Drucker im Dialogfeld "Einstellungen" finden.**