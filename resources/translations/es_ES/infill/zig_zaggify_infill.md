Conectar líneas de relleno
====
Este ajuste conecta los puntos finales del patrón de relleno, donde el relleno se encuentra con la pared interior o la piel, utilizando una línea que sigue el borde del área de relleno.

<!--screenshot {
"image_path": "infill_pattern_grid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "grid"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "zig_zaggify_infill_enabled.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "grid",
    "zig_zaggify_infill": true
},
"colours": 64
}-->
![Líneas de relleno no conectadas](../images/infill_pattern_grid.png)
![Líneas de relleno conectadas](../images/zig_zaggify_infill_enabled.png)

Esto convierte todo el patrón de relleno en una sola o muy pocas líneas. Convertirlo en una sola línea no siempre es posible. El punto de partida de esta línea es arbitrario, por lo que podría no ser el mismo para cada capa, especialmente si la forma que contiene el relleno es diferente de una capa a otra.

Conectar el relleno tiene un par de ventajas, pero también algunos inconvenientes:
* Su pieza será más fuerte al final, ya que prácticamente hay medio contorno extra.
* El relleno se adherirá mejor a las paredes debido al aumento de la superficie, lo que también hace que la pieza sea más fuerte.
* La velocidad de flujo se mantendrá más constante, lo que le permitirá imprimir el relleno a mayor velocidad sin problemas de flujo. Esto es especialmente importante para los materiales que son difíciles de extruir correctamente.
* Se realizarán significativamente menos retracciones durante la impresión del relleno, lo que evita que el material se desbaste.
* El efecto del ajuste [Infill Overlap](infill_overlap.md) se amplifica, ya que una mayor parte de las líneas de relleno se hará para solapar las paredes.
* Se necesitará más material para imprimir el relleno.
* Normalmente se necesitará más tiempo para imprimir el relleno, ya que los movimientos de desplazamiento son normalmente más rápidos que la impresión de las líneas de relleno.
* El relleno normalmente brillará más a través de las paredes, ya que es empujado en una mayor porción de las paredes.