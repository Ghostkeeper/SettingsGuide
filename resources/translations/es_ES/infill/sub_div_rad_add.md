Cáscara de subdivisión cúbica
====
Este ajuste hace que el patrón de subdivisión cúbica empiece a reducir el relleno un poco más hacia el interior, para mejorar la resistencia de la impresión.

<!--screenshot {
"image_path": "sub_div_rad_add_small.png",
"models": [
    {
        "script": "cylinder.scad",
        "transformation": ["scale(3)"]
    }
],
"camera_position": [0, 0, 275],
"settings": {
    "infill_sparse_density": 70,
    "infill_pattern": "cubicsubdiv",
    "sub_div_rad_add": 0
},
"layer": 500,
"colours": 32
}-->
<!--screenshot {
"image_path": "sub_div_rad_add_large.png",
"models": [
    {
        "script": "cylinder.scad",
        "transformation": ["scale(3)"]
    }
],
"camera_position": [0, 0, 275],
"settings": {
    "infill_sparse_density": 70,
    "infill_pattern": "cubicsubdiv",
    "sub_div_rad_add": 5
},
"layer": 500,
"colours": 32
}-->
![Subdivisión cúbica sin carcasa adicional](../images/sub_div_rad_add_small.png)
![Carcasa adicional de 5mm](../images/sub_div_rad_add_large.png)

La Subdivisión Cúbica funciona eliminando los bordes entre ocho cubos adyacentes si ninguno de los cubos toca el borde del volumen de relleno. Este ajuste mueve ese borde más adentro, evitando que se eliminen los bordes entre los cubos.

Efectivamente, esto hace que el patrón de Subdivisión Cúbica dibuje la máxima densidad más a menudo. Esto aumenta la fuerza del objeto, pero también aumenta la cantidad de tiempo y material que se necesita para imprimirlo. En el extremo, aumentar esta configuración lo suficiente hará que el patrón de Subdivisión Cúbica sea el mismo que el patrón Cúbico simple.

También puede ajustar esto a un número negativo. Esto hace que los bordes entre cubos se eliminen más a menudo, reduciendo efectivamente la cantidad de relleno alrededor de los bordes.