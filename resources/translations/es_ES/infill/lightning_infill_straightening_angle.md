Ángulo de enderezamiento del relleno del rayo
====
Este ajuste determina la inclinación del patrón de Lightning infill que puede sobresalir internamente.

El relleno de rayo produce las líneas en zigzag titulares donde necesita apoyar la parte superior de la impresión, pero estos toman mucho tiempo para imprimir debido a las esquinas afiladas en las líneas. Así que abajo, intentará enderezar esas líneas dentadas para reducir el tiempo de impresión. Este enderezamiento provoca salientes. El ajuste determina la cantidad de voladizo que se permite.

<!--screenshot {
"image_path": "lightning_infill_straightening_angle_40.png",
"models": [
    {
        "script": "cylinder.scad",
        "transformation": ["scaleZ(0.5)"]
    }
],
"camera_position": [36, 44, 19],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 40,
    "lightning_infill_prune_angle": 10,
    "lightning_infill_straightening_angle": 40
},
"colours": 32
}-->
<!--screenshot {
"image_path": "lightning_infill_straightening_angle_10.png",
"models": [
    {
        "script": "cylinder.scad",
        "transformation": ["scaleZ(0.5)"]
    }
],
"camera_position": [36, 44, 19],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 40,
    "lightning_infill_prune_angle": 10,
    "lightning_infill_straightening_angle": 10
},
"colours": 32
}-->
![A 40°, las líneas de relleno convergen rápidamente en líneas rectas](../images/lightning_infill_straightening_angle_40.png)
![A 10°, ya no hay salientes pronunciados en el relleno](../images/lightning_infill_straightening_angle_10.png)

Enderezar rápidamente (aumentar el voladizo) reduce un poco el tiempo de impresión, pero también reduce la fiabilidad de la impresión, especialmente con un ancho de línea fino. Si el voladizo es demasiado pronunciado, se produce una división de la capa. La división estará en el interior de la impresión y a menudo no será un problema, pero podría resultar en que esa parte del relleno fallara completamente, resultando en una parte de la cara superior sin soporte. Esto será visible como un parche áspero o una almohadilla en la parte superior, o incluso un lío de plástico desordenado en el peor de los casos.