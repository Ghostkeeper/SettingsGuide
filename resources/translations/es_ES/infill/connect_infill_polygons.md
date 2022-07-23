Conectar polígonos de relleno
====
Cuando el relleno está formado por bucles cerrados, estos bucles cerrados pueden fusionarse para formar un único bucle. Activando esta opción se harán pequeñas conexiones donde los polígonos son adyacentes.

Este ajuste sólo está disponible cuando el relleno consiste en bucles que son adyacentes entre sí. Esto significa que:
* El [patrón de relleno](infill_pattern.md) está configurado como Cruz o Cruz 3D.
* Las líneas de relleno están [multiplicadas](infill_multiplier.md) por un número par.
* Hay al menos 2 [paredes adicionales alrededor del relleno](infill_wall_line_count.md).

<!--screenshot {
"image_path": "connect_infill_polygons_disabled.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "triangles",
    "infill_multiplier": 2,
    "zig_zaggify_infill": true,
    "connect_infill_polygons": false
},
"colours": 32
}-->
<!--screenshot {
"image_path": "connect_infill_polygons_enabled.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "triangles",
    "infill_multiplier": 2,
    "zig_zaggify_infill": true,
    "connect_infill_polygons": true
},
"colours": 32
}-->
![Con las líneas de relleno multiplicadas, hay muchos bucles en este patrón de relleno](../images/connect_infill_polygons_disabled.png)
![Activar este ajuste fusiona los bucles](../images/connect_infill_polygons_enabled.png)

El objetivo de esta función es evitar los movimientos de desplazamiento. La línea final será un único bucle para cada parte conectada de relleno, por lo que no habrá movimientos de desplazamiento. Esto facilita el trabajo con filamentos flexibles, ya que estos son más difíciles de retraer y funcionan mejor si pueden seguir fluyendo a través de la boquilla.

La conexión de estos bucles también puede hacer que el relleno sea más fuerte al mejorar la conexión entre los bucles internamente. Sin embargo, cuando se conectan los polígonos, el cabezal de impresión a menudo tiene que hacer giros de 180 grados justo antes de una unión. Estos giros a veces impiden que la unión esté completamente conectada. Esto también puede hacer que el relleno sea más débil en algunos casos. Todo depende de cómo se engranen los bucles a través de la forma de su modelo.