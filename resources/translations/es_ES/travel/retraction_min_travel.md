Desplazamiento mínimo de retracción
====
Este ajuste evita que el material se retraiga en movimientos de recorrido muy cortos. Durante esos movimientos de desplazamiento hay muy poco tiempo para que el material rezume fuera de la boquilla de todos modos, por lo que la retracción haría más daño que bien.

<!--screenshot {
"image_path": "retraction_min_travel.png",
"models": [{"script": "spike_curve.scad"}],
"camera_position": [0, -31, 79],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_min_travel": 12},
"minimum_layer": 303,
"layer": 550,
"line": 334,
"colours": 64
}-->
![El movimiento de menor recorrido en el centro no está retraído](../images/retraction_min_travel.png)

La retracción del material tiene como objetivo evitar el encordamiento. Los movimientos de desplazamiento muy cortos no producen encordamiento, porque el material aún no ha tenido tiempo de fluir fuera de la boquilla. Los movimientos extremadamente cortos de un ancho de línea o así serán incluso líneas completamente superpuestas, por lo que no habrá espacio para ningún encordamiento. Por otro lado, la retracción hace que la boquilla se quede quieta durante un corto periodo de tiempo, mientras el material se mueve. Esto permite que fluya algo de material y produce una mancha allí. Por estas razones tiende a ser mejor no retraer cuando se recorren distancias cortas, incluso si esas vías están en partes visibles del modelo.

Aumentar este ajuste demasiado causará encordamiento en partes detalladas del modelo o donde las partes están cerca unas de otras.