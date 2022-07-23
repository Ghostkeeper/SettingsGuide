Orden de paredes
====
Este ajuste determina qué paredes se imprimen primero, imprimiéndolas de fuera a dentro, o de dentro a fuera.

<!--screenshot {
"image_path": "outer_inset_first_disabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "inset_direction": "inside_out"
},
"layer": 2,
"line": [0, 6, 12, 18, 25, 35, 41, 47, 54, 57, 61, 64, 65, 68, 72, 74, 77, 79, 80, 82, 86, 96, 102, 108, 114, 125, 131, 137, 144],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "outer_inset_first_enabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "inset_direction": "outside_in"
},
"layer": 2,
"line": [0, 6, 12, 18, 25, 35, 41, 47, 54, 58, 61, 63, 64, 66, 70, 72, 76, 79, 80, 83, 88, 97, 103, 109, 116, 125, 131, 137, 144],
"delay": 125,
"colours": 32
}-->
![La pared interior se imprime primero](../images/outer_inset_first_disabled.gif)
![La pared exterior se imprime primero](../images/outer_inset_first_enabled.gif)

Este ajuste tiene un pequeño efecto sobre la calidad y la precisión dimensional:
* La impresión desde el exterior hacia el interior mejorará la precisión dimensional. Las paredes adyacentes generalmente se empujan un poco, especialmente si el ancho de la línea de la pared es menor que el tamaño de la boquilla. La pared que se imprime primero se habrá solidificado y entonces no se empuja tanto. Por lo tanto, imprimir la pared exterior primero hará que su pared exterior esté en una ubicación más precisa.
* Si el relleno se imprime antes que las paredes, la impresión de afuera hacia adentro reducirá la cantidad de relleno que se ve en la superficie. De lo contrario, el relleno se imprime primero, luego las paredes interiores que son empujadas hacia afuera por el relleno, y luego la pared exterior que es empujada hacia afuera por las paredes interiores. Como resultado, podría ser visible un patrón en el exterior. Si se imprime primero la pared exterior, ésta puede solidificarse antes de que la pared interior pueda empujarla.
* La impresión de adentro hacia afuera es mejor para el voladizo. La pared exterior está más alejada de la capa anterior que la pared interior. Si se imprime primero la pared exterior, ésta aún no tiene nada a lo que agarrarse. Cuando se imprime primero la pared interior, la pared exterior puede adherirse lateralmente a la pared exterior.