Conectar polígonos superiores/inferiores
====
Cuando utilice un patrón concéntrico superior/inferior (un patrón que consiste en contornos cerrados, también conocidos como polígonos), conecte todos los contornos de manera que formen un solo camino.

<!--screenshot {
"image_path": "connect_skin_polygons_original.png",
"models": [
    {
        "script": "web.scad",
        "scad_params": ["stakes=1", "line_width=4"]
    }
],
"camera_position": [10, 5, 111],
"settings": {
    "top_bottom_pattern": "concentric",
    "connect_skin_polygons": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "connect_skin_polygons_enabled.png",
"models": [
    {
        "script": "web.scad",
        "scad_params": ["stakes=1", "line_width=4"]
    }
],
"camera_position": [10, 5, 111],
"settings": {
    "top_bottom_pattern": "concentric",
    "connect_skin_polygons": true
},
"colours": 64
}-->
![El patrón concéntrico crea contornos separados](../images/connect_skin_polygons_original.png)
![Todos los contornos se conectan para formar una curva](../images/connect_skin_polygons_enabled.png)

Esto evita los movimientos de desplazamiento en su mayor parte. Sin embargo, crea nuevas curvas cerradas en las que la boquilla tendrá que acelerar y desacelerar mucho, lo que compensará la ganancia de tiempo de impresión. El patrón de garabatos también será visible en el exterior, lo que da un efecto visual interesante.

Los contornos creados por [Recuento de paredes adicionales](skin_outline_count.md) no están conectados.