Formwinkel
====
Ähnlich wie bei der Funktion [Überhänge druckbar machen](../../../articles/experimental/conical_overhang_enabled.md) wird mit dieser Einstellung die Form so verändert, dass sie ohne Unterstützung gedruckt werden kann. Es wird nur die äußere Kontur der Form verändert, so dass die Form Ihres Gusses nicht beeinträchtigt wird.

<!--screenshot {
"image_path": "mold_angle.png",
"models": [
    {
        "script": "star_podium.scad",
        "transformation": ["mirrorZ"]
    }
],
"camera_position": [81, 129, 45],
"settings": {
    "mold_enabled": "True"
},
"colours": 48
}-->
![Bei einem Winkel von 40 Grad kann die Unterseite dieser Form ohne Unterstützung gedruckt werden](../../../articles/images/mold_angle.png)

Wenn Sie diesen Winkel verkleinern, werden die extremen Überhänge reduziert. Dadurch wird der Druck zuverlässiger. Allerdings wird dadurch auch die Basis des Drucks breiter, was die Dauer des Drucks erheblich verlängert und den Materialverbrauch erhöht.

Bei einigen Formen reicht es nicht aus, die äußere Form zu verändern, um sie richtig zu drucken. Sie muss immer noch gestützt werden. Sie können einen ähnlichen Effekt erzielen, indem Sie die [Konische Stützstruktur](../../../articles/experimental/support_conical_enabled.md) aktivieren.

<!--screenshot {
"image_path": "mold_needs_support.png",
"models": [{"script": "basic_overhang.scad"}],
"camera_position": [20, 183, 97],
"settings": {
    "mold_enabled": "True"
},
"colours": 32
}-->
![Diese Form braucht noch Unterstützung](../../../articles/images/mold_needs_support.png)