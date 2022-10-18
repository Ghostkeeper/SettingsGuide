Relleno antes que las paredes
====
Esto afecta al orden en que se imprimen los elementos. Con este ajuste activado, el relleno de una pieza se imprimirá antes de que se impriman las paredes de esa pieza en esa capa.

<!--screenshot {
"image_path": "infill_before_walls_disabled.gif",
"models": [
    {
        "script": "cube.scad",
        "transformation": ["scale(0.25)"]
    }
],
"camera_position": [0, 0, 100],
"settings": {
    "top_layers": 0,
    "infill_before_walls": false
},
"layer": 162,
"line": [0, 1, 2, 3, 4, 7, 8, 9, 10, 12, 15, 18, 21, 24, 27],
"colours": 32,
"delay": 250
}-->
<!--screenshot {
"image_path": "infill_before_walls_enabled.gif",
"models": [
    {
        "script": "cube.scad",
        "transformation": ["scale(0.25)"]
    }
],
"camera_position": [0, 0, 100],
"settings": {
    "top_layers": 0,
    "infill_before_walls": true
},
"layer": 162,
"line": [0, 1, 4, 7, 10, 13, 16, 20, 21, 22, 23, 26, 27, 28, 29],
"colours": 32,
"delay": 250
}-->
![La configuración está desactivada, por lo que las paredes se imprimen primero](../images/infill_before_walls_disabled.gif)
![La configuración está activada, por lo que el relleno se imprime primero](../images/infill_before_walls_enabled.gif)

Este ajuste es un compromiso entre la precisión y la fuerza:
* Si las paredes se imprimen antes que el relleno, las paredes podrían no tener nada a lo que adherirse, causando que se hundan más. Sin embargo, las paredes se habrán solidificado primero y no serán empujadas por el relleno, lo que evita que el relleno brille a través de las paredes.
* Si el relleno se imprime antes que las paredes, las paredes serán empujadas donde el relleno está unido a las paredes, lo que hace que las paredes sean menos precisas y puede hacer que el relleno brille a través de la superficie, creando un patrón visible en el exterior. Sin embargo, el relleno mantendrá las paredes en su sitio mientras se imprimen.