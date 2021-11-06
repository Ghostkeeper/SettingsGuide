Reihenfolge des Wanddrucks optimieren
====
Wenn diese Option aktiviert ist, verwendet Cura zusätzliche Zeit für das Slicing, um die Reihenfolge zu optimieren, in der die Wände gedruckt werden. Ziel ist es, die Anzahl der Fahrwege und Einzüge zu reduzieren, indem Wände, die das gleiche Teil umgeben, nacheinander gedruckt werden.
<!--screenshot {
"image_path": "optimize_wall_printing_order_disabled.gif",
"models": [
    {
        "script": "plate_with_indent.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "optimize_wall_printing_order": false
},
"layer": 37,
"line": [0, 7, 14, 21, 28, 34, 38, 42, 46, 64, 78, 91, 105, 120, 124, 128, 132, 140, 144, 148, 152, 162, 170, 178, 186, 194, 198, 202, 206, 224, 237, 251, 265, 281, 285, 289, 293, 302, 306, 310, 314],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "optimize_wall_printing_order_enabled.gif",
"models": [
    {
        "script": "plate_with_indent.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "optimize_wall_printing_order": true
},
"layer": 37,
"line": [0, 4, 8, 12, 16, 21, 25, 29, 33, 42, 46, 50, 54, 59, 63, 67, 71, 97, 110, 123, 138, 153, 166, 179, 194, 204, 208, 212, 216, 221, 225, 229, 233, 245, 252, 259, 265, 273, 281, 289, 297],
"delay": 125,
"colours": 32
}-->
![Optimierung deaktiviert](../../../articles/images/optimize_wall_printing_order_disabled.gif)
![Optimierung aktiviert](../../../articles/images/optimize_wall_printing_order_enabled.gif)

Wenn diese Optimierung aktiviert ist, druckt die Düse zuerst alle Wände um ein Teil herum, bevor sie zum nächsten Teil übergeht, anstatt zuerst alle Innenwände zu drucken, bevor sie die Außenwände druckt. Die Optimierung ist in der Regel positiv, kann sich aber bei einigen Teilen auf die Maßgenauigkeit auswirken, da die vorherige Wand noch nicht verfestigt ist, wenn die nächste Wand daneben abgelegt wird.