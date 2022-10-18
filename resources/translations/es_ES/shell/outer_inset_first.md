Paredes exteriores antes que interiores
====
Este ajuste determina qué paredes se imprimen primero, las exteriores o las interiores.

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
![La pared interior se imprime primero](../images/outer_inset_first_disabled.gif)
![La pared exterior se imprime primero](../images/outer_inset_first_enabled.gif)

Activar esta opción tiene un pequeño efecto sobre la calidad y la precisión dimensional:
* Mejorará la precisión dimensional. Las paredes adyacentes generalmente se empujan un poco, especialmente si el ancho de la línea de la pared es menor que el tamaño de la boquilla. La pared que se imprime primero se habrá solidificado y entonces no se empuja tanto. Por lo tanto, imprimir la pared exterior primero hará que su pared exterior esté en una ubicación más precisa.
* Si el relleno se imprime antes que las paredes, se reducirá la cantidad de relleno que se muestra en la superficie. De lo contrario, el relleno se imprime primero, luego las paredes interiores que son empujadas hacia afuera por el relleno, y luego la pared exterior que es empujada hacia afuera por las paredes interiores. Como resultado, podría ser visible un patrón en el exterior. Si se imprime primero la pared exterior, ésta puede solidificarse antes de que la pared interior pueda empujarla.
* La impresión de la pared exterior primero suele ser peor para el voladizo. La pared exterior está más alejada de la capa anterior que la pared interior. Cuando se imprime primero la pared exterior, ésta no tiene nada a lo que agarrarse. Cuando se imprime primero la pared interior, la pared exterior puede adherirse lateralmente a la pared exterior.