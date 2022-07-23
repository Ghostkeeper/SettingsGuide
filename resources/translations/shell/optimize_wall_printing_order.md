Optimizar el orden de impresión de paredes
====
Si esta opción está activada, Cura empleará un tiempo extra de corte para optimizar el orden de impresión de las paredes. El objetivo es reducir el número de desplazamientos y retracciones imprimiendo las paredes que rodean la misma pieza una tras otra.

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
"line": [0, 5, 9, 13, 17, 25, 29, 33, 37, 47, 54, 61, 71, 89, 106, 122, 142, 156, 160, 164, 169, 176, 183, 188, 194, 225, 241, 262, 282, 293, 297, 302, 309, 319, 326, 332, 343, 353, 358, 363, 368],
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
"line": [0, 4, 7, 11, 17, 25, 31, 36, 41, 47, 51, 55, 60, 67, 71, 76, 83, 92, 99, 106, 114, 123, 130, 136, 147, 165, 181, 197, 217, 239, 256, 278, 299, 312, 316, 320, 325, 331, 336, 343, 350],
"delay": 125,
"colours": 32
}-->
![Optimización desactivada](../images/optimize_wall_printing_order_disabled.gif)
![Optimización activada](../images/optimize_wall_printing_order_enabled.gif)

Si esta optimización está activada, la boquilla imprimirá primero todas las paredes alrededor de una pieza antes de pasar a la siguiente, en lugar de imprimir primero todas las paredes interiores antes de imprimir las exteriores. La optimización suele ser positiva, pero con algunas piezas puede afectar a la precisión dimensional porque la pared anterior no se ha solidificado todavía al colocar la siguiente junto a ella.

Si la pared interior y la exterior tienen caudales muy diferentes, esta optimización también provoca muchos más cambios en el caudal. Esto se manifiesta con una mayor [costura](../troubleshooting/seam.md) o algunas [gotas](../troubleshooting/blobs.md). El ancho de la línea tiene un mayor impacto en la impresión que esta optimización del recorrido, por lo que es mejor desactivar la optimización si este podría ser el problema en su impresión.