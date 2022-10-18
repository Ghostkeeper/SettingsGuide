Ángulo de las ramas del soporte en árbol
====
Este ajuste determina el ángulo máximo de voladizo que se permite a las ramas del soporte del árbol. Si se aumenta el ángulo, las ramas pueden imprimirse más horizontalmente, lo que les permite llegar más lejos.

<!--screenshot {
"image_path": "support_tree_angle_20.png",
"models": [{"script": "over_t.scad"}],
"camera_position": [-23, 124, 45],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.02,
    "support_tree_angle": 20
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_tree_angle_40.png",
"models": [{"script": "over_t.scad"}],
"camera_position": [-23, 124, 45],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.02,
    "support_tree_angle": 40
},
"colours": 64
}-->
![Un ángulo de ramificación de 20°](../images/soporte_árbol_ángulo_20.png)
![Un ángulo de ramificación de 40°](../images/soporte_árbol_ángulo_40.png)

Si se reduce el ángulo de las ramas, éstas serán más verticales. Aumentarlo hará que sean más horizontales. Como las ramas pueden tener mayores ángulos de voladizo, pueden llegar más lejos alrededor de los obstáculos, permitiendo que el soporte se apoye en la placa de impresión más a menudo, en lugar de en el modelo. También permitirá que las ramas se separen en un punto posterior.

Los efectos más importantes de aumentar el ángulo de las ramas para el soporte de los árboles incluyen:
* Reducción de las cicatrices, debido a la menor necesidad de soporte en el modelo en lugar de la placa de impresión. Si [Support Placement](../support/support_type.md) se establece en Touching Buildplate, se puede apoyar más del modelo.
* Reducción del tiempo de impresión y del uso de material, debido a que las ramas se separan a mayor altura. Las ramas se separan justo a tiempo para poder alcanzar todo el voladizo.
* Reducción de la fiabilidad. Si el ángulo del voladizo es demasiado grande, el soporte se debilitará en gran medida, aumentando la posibilidad de que el soporte se rompa o se caiga.

Los ángulos grandes de las ramas se combinan mejor con valores bajos para el ajuste [Resolución de colisión del soporte en árbol](support_tree_collision_resolution.md). Esto reducirá los desplazamientos en las posiciones del árbol debido a la evitación de colisiones. Así se evita que la distancia del voladizo crezca demasiado cuando se ajusta la distancia de colisión.