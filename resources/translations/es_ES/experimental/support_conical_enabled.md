Activar el soporte cónico
====
Si se activa esta opción, la estructura de soporte ya no será completamente vertical en los lados. El soporte tendrá una forma cónica, haciéndose más pequeño o más grande hacia la parte inferior.

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_neg10.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": -10
},
"colours": 64
}-->
![El soporte se hace más pequeño hacia abajo](../images/support_conical_enabled.png)
![El soporte se hace más grande hacia abajo](../images/support_conical_angle_neg10.png)

El propio soporte se inclinará con un determinado [ángulo](support_conical_angle.md). Con ángulos negativos, el soporte se hará más grande hacia la parte inferior, haciendo que el soporte sea significativamente más estable. Con ángulos positivos, se hará más pequeño hacia la parte inferior. Esto ahorra mucho material y tiempo de impresión. Para evitar que el soporte se vuelva inestable, también se puede definir un [ancho mínimo] (support_conical_min_width.md) para el soporte.

El soporte cónico es el parámetro más potente para la ponderación entre el tiempo de impresión y la estabilidad del soporte. Hay dos casos principales de uso para el soporte cónico:
* Para ahorrar material y tiempo de impresión. El soporte cónico puede ahorrarle fácilmente la mitad del material necesario para el soporte y, por extensión, la mitad del tiempo de impresión. Esto es especialmente efectivo si hay grandes volúmenes de soporte, para impresiones grandes y altas.
* Hacer el soporte más estable utilizando un ángulo negativo. Si su impresión tiene pequeñas características en lo alto que necesitan apoyo, normalmente producirán [torres] muy altas (../soporte/soporte_uso_torres.md) que son propensas a caerse durante la impresión. Con el soporte cónico, estas estructuras de soporte altas y delgadas pueden hacerse más anchas en la parte inferior. Esto les da una mayor estabilidad. Sin embargo, se tardará más en imprimir este soporte ya que requiere más material.

Cuando la [Colocación del soporte](../support/support_type.md) está configurada para colocar el soporte sólo en la placa de construcción, el soporte cónico permite llegar alrededor del modelo para seguir apoyando el modelo en lugares que están por encima de otras partes del modelo. El soporte seguirá descansando sólo en la placa de construcción, pero debido a su forma ahora puede alcanzar las áreas que sobresalen en las esquinas que de otra manera no serían soportadas.

Esta característica es una versión algo más simple y menos extrema de <!--if cura_version >= 4.7-->[Tree Support](../support/support_structure.md)<!--endif--><!--if cura_version < 4.7:[Tree Support](support_tree_enable.md)-->. El soporte de árbol tiene muchas de las mismas ventajas que el soporte cónico. Sin embargo, el soporte arbóreo utiliza un algoritmo completamente diferente y se permite más libertad en la construcción del soporte, mientras que el soporte cónico se mantiene más fiel al algoritmo de generación de soporte ordinario. Esto significa que los ajustes para el soporte ordinario tienden a funcionar mejor cuando se usa con el soporte cónico, pero tendrán que ser ajustados significativamente para el soporte de árbol. El soporte en forma de árbol tiende a ahorrar más material y tiempo de impresión, al tiempo que mantiene la fiabilidad de la impresión.