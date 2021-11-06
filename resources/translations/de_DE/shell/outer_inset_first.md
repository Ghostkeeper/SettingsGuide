Außenwände vor Innenwänden
====
Diese Einstellung legt fest, welche Wände zuerst gedruckt werden, die Außen- oder die Innenwände.

<!--screenshot {
"image_path": "outer_inset_first_disabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "outer_inset_first": false
},
"layer": 2,
"line": [0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 23, 29, 35, 45, 51, 57, 63, 67, 68, 69, 70, 71, 72, 73, 74, 84, 90, 96, 102, 113, 119, 125, 131],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "outer_inset_first_enabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "outer_inset_first": true
},
"layer": 2,
"line": [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 24, 30, 36, 47, 53, 59, 65, 70, 71, 72, 73, 74, 75, 76, 77, 86, 92, 98, 104, 114, 120, 126, 132],
"delay": 125,
"colours": 32
}-->
![Die Innenwand wird zuerst gedruckt](../../../articles/images/outer_inset_first_disabled.gif)
![Die Außenwand wird zuerst gedruckt](../../../articles/images/outer_inset_first_enabled.gif)

Die Aktivierung dieser Einstellung hat eine geringe Auswirkung auf die Qualität und die Maßhaltigkeit:
* Sie verbessert die Maßgenauigkeit. Benachbarte Wände verschieben sich im Allgemeinen ein wenig, vor allem wenn die Breite der Wandlinie kleiner ist als die Düsengröße. Die Wand, die zuerst gedruckt wird, ist bereits verfestigt und wird daher nicht mehr so stark verschoben. Wenn Sie also die äußere Wand zuerst drucken, befindet sich die äußere Wand in einer genaueren Position.
* Wenn die Füllung vor den Wänden gedruckt wird, ist die Füllung auf der Oberfläche nicht so stark sichtbar. Andernfalls wird zuerst die Füllung gedruckt, dann die Innenwände, welche durch die Füllung nach außen gedrückt werden, und dann die Außenwand, welche durch die Innenwände nach außen gedrückt wird. Infolgedessen könnte auf der Außenseite ein Muster sichtbar sein. Wenn die Außenwand zuerst gedruckt wird, kann die Außenwand erstarren, bevor die Innenwand auf sie drücken kann.
* Es ist generell schlechter für den Überhang, wenn die Außenwand zuerst gedruckt wird. Die Außenwand ist weiter von der vorherigen Schicht entfernt als die Innenwand. Wenn die Außenwand zuerst gedruckt wird, hat die Außenwand noch nichts, woran sie sich festhalten kann. Wenn die Innenwand zuerst gedruckt wird, kann die Außenwand seitlich an der Außenwand anhaften.