Soporte en árbol
====
El soporte en forma de árbol ofrece un enfoque alternativo a la técnica de soporte ordinaria para sostener el modelo. En el soporte en forma de árbol, se genera una estructura ramificada que comienza en la placa de construcción con una base pequeña, pero que crece hacia las partes que necesitan soporte.

<!--screenshot {
"image_path": "support_structure_tree.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.05
},
"colours": 32
}-->
![Una estructura en forma de árbol soporta el voladizo](../images/support_structure_tree.png)

El soporte del árbol puede evitar los obstáculos al crecer hacia las zonas del voladizo. Si es posible, el árbol crecerá desde la placa de construcción hacia arriba para evitar que se marque la superficie sobre la que se apoya el soporte. Si esto no es posible, el árbol se apoyará en la superficie del modelo lo más cerca posible del voladizo para minimizar el tiempo y el uso de material. Las ramas del soporte del árbol están limitadas por el [Ángulo de la rama del soporte del árbol](../support/support_tree_angle.md) para que no produzcan un voladizo demasiado pronunciado de sí mismas. Esto limita la capacidad de crecer alrededor de los obstáculos y también determina la altura a la que los troncos comenzarán a ramificarse.

El soporte del árbol es hueco por defecto. Sin embargo, los ajustes de soporte ordinarios siguen aplicándose al área circunscrita por las ramas del árbol. En particular, la [Densidad del soporte](../support/support_infill_rate.md) puede utilizarse para dar al soporte más fuerza estructural. Debido a la naturaleza del soporte de árbol, que es muy irregular, normalmente tiene mucha fuerza para su propósito.

El soporte de árbol tiene una serie de ventajas sobre el soporte normal, por nombrar algunas:
* El soporte para árboles suele utilizar mucho menos material que el soporte normal. Lo normal es que se utilice entre un 25% y un 50% del material. Esto ahorra mucho tiempo y costes en material.
* Cuando se imprime con el mismo material que la impresión, el voladizo tiende a verse mejor cuando se utiliza el soporte de árbol.
* El soporte de árbol es más fácil de quitar que el soporte normal.
* El soporte en forma de árbol deja menos cicatrices en la superficie que el soporte normal, debido a que puede llegar alrededor del modelo hacia la placa de construcción.

Sin embargo, esto también tiene algunas desventajas:
* El soporte en forma de árbol tarda un orden de magnitud más en cortarse. Será necesario tener paciencia, especialmente con los modelos altos.
* Hay muchas interrupciones en el flujo cuando se imprimen las ramas más pequeñas, lo que hace que el soporte de árbol no sea adecuado para imprimir utilizando materiales que son difíciles de extruir, como PVA o materiales flexibles.
* El soporte de árbol no funciona muy bien para soportar algunos modelos mecánicos. En particular, tiende a colocar muy pocas ramas para soportar voladizos planos e inclinados.

Aunque el soporte de árbol puede activarse al mismo tiempo que el soporte ordinario, generalmente no es deseable. Los dos tipos de apoyo se cruzarán y provocarán una sobreextracción.