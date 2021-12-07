Abstand zum Brim-Element
====
Bei dieser Einstellung entsteht eine Lücke zwischen dem Modell und dem Brim. Die Brim-Linien liegen nicht mehr fest am Modell an.


<!--screenshot {
"image_path": "brim_gap.png",
"models": [
    {
        "script": "arrow.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [-22, 32, 133],
"settings": {
    "adhesion_type": "brim",
    "brim_gap": 1
},
"colours": 32
}-->
![Der Brim hält einen gewissen Abstand zum Modell](../../../articles/images/brim_gap.png)

Diese Lücke soll das Abziehen des Brims vom Modell erleichtern. Indem man die Brim-Linien etwas vom eigentlichen Modell entfernt (in der Größenordnung einer halben Linienbreite), wird die Verbindung zwischen dem Brim und dem Modell schwächer als eine Schicht, was das Abreißen des Brims von Hand erleichtert. Außerdem wird dadurch die Narbe oder der Elefantenfuß, den der Brim nach dem Entfernen hinterlässt, verringert. Dies ist besonders effektiv bei einer größeren [Dicke der ersten Schicht](../resolution/layer_height_0.md), da der dicke Brim dann schwerer zu entfernen ist.

Auf der anderen Seite verringert sich dadurch auch die Wirksamkeit des Brims, um das Modell auf der Bauplatte zu halten. Durch eine dünnere Kontaktfläche wird der Brim nicht in der Lage sein, eine große Kraft auf das Modell auszuüben, um es gegen die Wirkung von [Warping](../troubleshooting/warping.md) unten zu halten.