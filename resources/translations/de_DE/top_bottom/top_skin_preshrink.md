Breite für das Entfernen der Außenhaut oben
====
Entfernt dünne Teile der vollständig gefüllten oberen Schichten und druckt sie stattdessen mit Füllmaterial. Dies spart Druckzeit und Material.

Bei steilen Oberflächen werden die oberen Schichten oft sehr dünn. Sie sind nicht notwendig, da die horizontale Festigkeit der Wände mehr als ausreichend ist, wenn die Oberfläche fast vollständig senkrecht ist.

<!--screenshot {
"image_path": "skin_preshrink_original.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_preshrink": 0,
    "top_skin_preshrink": 0
},
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_preshrink_shrunk.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_preshrink": 1,
    "top_skin_preshrink": 1
},
"colours": 32
}-->
![Vor der Entfernung](../images/skin_preshrink_original.png)
![Nach der Entfernung](../images/skin_preshrink_shrunk.png)

Eine zu hohe Einstellung kann dazu führen, dass die Oberseite von kleinen Objekten offen ist, weil sie mit Füllmaterial anstelle von Außenhaut gefüllt wird.