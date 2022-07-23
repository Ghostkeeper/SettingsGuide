Ángulo de poda de relleno del rayo
====
El patrón de relleno del rayo produce una estructura en forma de árbol en el interior de la impresión que comienza siendo pequeña, pero se ramifica para alcanzar todas las partes de la parte superior de la impresión que necesitan ser apoyadas desde el interior. Este ajuste indica hasta dónde pueden sobresalir las ramas del árbol en los extremos.

<!--screenshot {
"image_path": "lightning_infill_prune_angle_40.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [112, 15, 9],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 40,
    "lightning_infill_prune_angle": 40
},
"colours": 32
}-->
<!--screenshot {
"image_path": "lightning_infill_prune_angle_70.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [112, 15, 9],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 40,
    "lightning_infill_prune_angle": 70
},
"colours": 32
}-->
![A 40°, el relleno del rayo es bastante estable](../images/lightning_infill_prune_angle_40.png)
![A 70° las ramas sobresalen mucho](../images/lightning_infill_prune_angle_70.png)

Aumentar el ángulo de poda significa que el relleno podrá empezar más pequeño en la parte inferior y seguir alcanzando toda la superficie superior. En muchos casos ni siquiera es necesario que comience en la parte inferior, sino que simplemente puede colgarse de los lados. Los efectos destacados de aumentar este ángulo son:

* Reducción del tiempo de impresión y del uso de material.
* Paredes más lisas, porque no habrá tanto relleno tocando las paredes desde el interior.
* Reducción de la resistencia.
* Más posibilidades de que la impresión falle. Si el voladizo es demasiado pronunciado, habrá un voladizo importante en el extremo de cada línea, que se combará y podría aflojarse.

En la práctica, el ángulo de poda puede ser mayor que los ángulos de voladizo normales o que los otros ángulos de voladizo del relleno de rayos. Dado que las líneas se apoyan bien en la capa inferior, tener un poco más de voladizo no es realmente un problema.