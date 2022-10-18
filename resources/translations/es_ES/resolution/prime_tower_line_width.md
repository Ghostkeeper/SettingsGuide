Ancho de línea de la torre auxiliar
====
Este ajuste determina la anchura de las líneas con las que se dibuja la torre auxiliar.

<!--screenshot {
"image_path": "prime_tower_line_width.png",
"models": [
    {"script": "cube.scad"},
    {
        "script": "cube.scad",
        "object_settings": {"extruder_nr": 1},
        "transformation": ["translateX(40)"]
    }
],
"camera_position": [475, -419, 131],
"camera_lookat": [475, -465, 20],
"settings": {
    "prime_tower_enable": true,
    "[1]prime_tower_line_width": 0.8
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![El material azul tiene un ancho de línea mayor que el material amarillo](../images/prime_tower_line_width.png)

La elección de un ancho de línea mayor hace que la torre auxiliar se imprima a veces más rápido. Si el volumen extruido por un contorno es lo suficientemente grande, aumentar el ancho de línea hace innecesario otro bucle. Sin embargo, aumentar el ancho de línea demasiado puede hacer que la torre auxiliar sea más débil porque no se puede extruir suficiente material con la rapidez necesaria.