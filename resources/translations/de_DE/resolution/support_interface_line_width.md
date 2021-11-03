Stützstruktur Schnittstelle Linienbreite
====
Die Breiten der Stützstruktur Schnittstellen Linien können getrennt von den Breiten der übrigen Stützstrukturlinien konfiguriert werden.

<!--screenshot {
"image_path": "support_roof_line_width.png",
"models": [
    {
        "script": "trash_bin_lid.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [-47, 79, 110],
"settings": {
    "support_enable": true,
    "support_roof_enable": true,
    "support_roof_line_width": 0.8
},
"layer": 192,
"colours": 64
}-->
![Die Stützstruktur Schnittstelle Linien sind breiter als der Rest der Unterstützungslinien](../../../articles/images/support_roof_line_width.png)

Das Drucken der Stützstruktur Schnittstelle mit etwas dünneren Linien ist oft vorteilhaft für die Qualität der überhängenden Oberfläche, die sie stützt, da die Oberfläche über der Stützstruktur Schnittstelle glatter ist. Allerdings wird dadurch nicht unbedingt die Haftung zwischen der Stützstruktur Schnittstelle und dem Modell erhöht, so dass die Stützstruktur nicht unbedingt schwieriger zu entfernen ist.

Ebenso haftet der Stützstrukturboden gleichmäßiger, wodurch die Spuren an den Stellen, an denen die Stützstruktur auf dem Modell aufliegt, verringert werden, ohne dass die Stützstruktur dadurch schwächer wird.

Werden die Schnittstellenlinien jedoch zu dünn gedruckt, kommt es zu einer ungleichmäßigen Extrusion, wodurch die Stützwirkung der Schnittstelle verringert wird, was zu einer schlechteren Überhangqualität und einer weniger stabilen Stützstruktur führt. Außerdem kann es zu einer starken Veränderung der Durchflussrate durch die Düse kommen, was zu einer Überextrusion führt, wenn mit dem Druck der Stützstrukturschnittstelle begonnen wird, und zu einer Unterextrusion, wenn das gedruckt wird, was nach der Stützstrukturschnittstelle kommt.