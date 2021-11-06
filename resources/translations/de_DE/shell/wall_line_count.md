Anzahl der Wandlinien
====
Diese Einstellung legt fest, wie viele Konturen in jeder Schicht um den Druck herum erzeugt werden sollen.

<!--screenshot {
"image_path": "wall_thickness_0.8.png",
"models": [
    {
        "script": "rotary_tumbler_lid.scad",
        "transformation": ["scale(0.4)"]
    }
],
"camera_position": [50, 50, 124],
"settings": {
    "skin_outline_count": 0,
    "wall_line_count": 2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "wall_thickness_1.6.png",
"models": [
    {
        "script": "rotary_tumbler_lid.scad",
        "transformation": ["scale(0.4)"]
    }
],
"camera_position": [50, 50, 124],
"settings": {
    "skin_outline_count": 0,
    "wall_line_count": 4
},
"colours": 32
}-->
![Zwei Wände](../../../articles/images/wall_thickness_0.8.png)
![Vier Wände](../../../articles/images/wall_thickness_1.6.png)

Nur eine der Wände ist eine Außenwand und wird mit den Einstellungen für Außenwände gedruckt. Die übrigen Wände werden mit den Einstellungen für die Innenwände gedruckt.

Die Anzahl der Wände ist ein wichtiger Faktor dafür, wie stark der Druck sein wird. Da die Wände nebeneinander liegen, können sie sich gegenseitig verstärken, was zu einem stärkeren Teil führt. Bei größeren Drucken kann dies, abhängig von der Form, ein viel effektiverer Weg sein, um ein starkes Objekt zu erhalten, als die Füllung anzupassen.

Die Erhöhung der Anzahl der Wände wird:
* Die Festigkeit des Drucks wird deutlich erhöht.
* Verringerung des Durchscheineffekts an den Stellen, an denen das Füllmuster von außen sichtbar ist.
* Verbesserung der Überhänge, da die Wandlinien in der Regel stärker auf den nächstgelegenen Auflagerpunkt ausgerichtet sind.
* Das Modell leichter wasserdicht machen.
* Deutliche Erhöhung der Druckzeit und des Materialverbrauchs des Drucks.