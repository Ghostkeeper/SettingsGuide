Estructura de soporte
====
Con este ajuste puede elegir qué algoritmo utilizar para construir las estructuras de soporte. Estas construcciones tienen propiedades muy diferentes, por lo que la elección de un algoritmo tendrá una gran influencia en la calidad del soporte de su impresión. Hay dos opciones disponibles.

<!--screenshot {
"image_path": "support_type_everywhere.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
    "support_enable": true,
    "support_type": "everywhere"
},
"colours": 32
}-->
Normal
----
![Construcción de soporte normal](../images/tipo_de_soporte_por_todo.png)

Esta es una estructura de soporte tradicional, a la que la mayoría de la gente está acostumbrada. La estructura se genera por debajo de las zonas en voladizo, y normalmente se rellena con un patrón que soporta directamente las zonas en voladizo. A partir de ahí, se deja caer hacia abajo hasta que llega a la placa de impresión o a una parte del modelo que la soporta.

La construcción de soporte normal ha sido la predeterminada durante la mayor parte de la historia de la impresión 3D, y funciona de forma similar en todos los cortadores. Este es el estándar de oro, y no sin razón:
* Debido a su estructura robusta, con grandes áreas de contacto en el modelo y la placa de impresión, es muy fiable. Es muy indulgente con los malos ajustes o con una impresora mal afinada.
* Debido a que la forma es simple, es rápido de cortar.
* La estructura de soporte recta es fácil de personalizar para un usuario, ya que queda inmediatamente claro qué bordes van a ser soportados y cuáles no.

Las desventajas más importantes surgen de las mismas propiedades:
* Debido a las grandes áreas de contacto, el soporte suele ser difícil de eliminar y puede dejar importantes cicatrices en la superficie donde ha tocado.
* Aunque es estable, puede utilizar mucho material y tardar mucho en imprimirse. Esto puede contrarrestarse en cierta medida utilizando [soporte cónico] (../experimental/conical_overhang_enabled.md).

Como el soporte suele ser grande y ancho, se necesita un [patrón de relleno](support_pattern.md) para soportar la superficie adecuadamente. El patrón de relleno en zig-zag se puede utilizar para imprimir el soporte en gran parte de una sola línea, y para permitir una eliminación más fácil. Otros patrones pueden combinarse con un [contorno] adicional(support_wall_count.md) para que el soporte sea más resistente.

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
Árbol
----
![Soporte de árbol](../images/support_structure_tree.png)

Con el soporte en forma de árbol, la estructura de soporte empezará siendo pequeña en la placa de impresión, y crecerá con ramas hacia las partes de la impresión que necesiten soporte.

El soporte en forma de árbol puede evitar los obstáculos cuando crece hacia las zonas que sobresalen, ya que el soporte no tiene que caer directamente hacia abajo. Si es posible, el soporte se apoyará sólo en la placa de impresión, para evitar que la superficie sobre la que se apoya quede marcada. Si no existe un camino desde la placa de construcción hasta el voladizo, se apoyará en una superficie que esté lo más cerca posible del voladizo, para minimizar el uso de material. Las ramas del soporte en forma de árbol están limitadas por el [Ángulo de la rama del soporte en forma de árbol](support_tree_angle.md) para que no produzcan un voladizo demasiado pronunciado. Esto limita la capacidad de crecer alrededor de los obstáculos y también determina la altura a la que los troncos comenzarán a ramificarse.

La construcción del soporte arbóreo tiene una serie de grandes ventajas sobre el soporte normal:
* El soporte para árboles suele utilizar mucho menos material que el soporte normal. Es habitual que se utilice entre un 25% y un 50% del material. Esto ahorra mucho tiempo y reduce el coste de la impresión.
* Debido a su pequeña área de contacto, el voladizo tiende a verse mejor cuando se utiliza el soporte de árbol.
* También debido a la pequeña área de contacto, el soporte será más fácil de quitar.
* Deja menos cicatrices en la superficie que el soporte normal, debido a que puede alcanzar alrededor del modelo desde la placa de impresión hacia el voladizo.

Sin embargo, las principales desventajas son:
* Se tarda mucho más en cortar que el soporte normal. Hay que tener paciencia, sobre todo con los modelos altos.
* Hay muchas interrupciones en el flujo cuando se imprimen las ramas más pequeñas, lo que hace que el soporte de árbol no sea adecuado para imprimir utilizando materiales que son difíciles de extruir, como PVA o materiales flexibles.
* El soporte de árbol no funciona bien para soportar algunos modelos mecánicos. En particular, tiende a colocar muy pocas ramas para soportar voladizos planos e inclinados.

El soporte de árbol es hueco por defecto. Las ramas tendrán una punta pequeña, por lo que un patrón de relleno no proporciona soporte adicional para la superficie que sobresale del elemento impreso. Debido a su forma irregular, el soporte del árbol es normalmente bastante resistente. Sin embargo, los ajustes de soporte ordinarios siguen aplicándose al área circunscrita por las ramas del árbol. La [Densidad del soporte](support_infill_rate.md) puede utilizarse para dar al soporte más fuerza estructural.