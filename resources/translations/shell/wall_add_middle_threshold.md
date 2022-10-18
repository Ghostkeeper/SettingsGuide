Añadir umbral de línea media
====
Cuando se imprimen piezas finas, Cura ajusta el ancho de las líneas de pared para que se ajusten al ancho exacto del modelo. Cura también puede decidir utilizar menos líneas de pared en su lugar. Este ajuste es el umbral en el que Cura añadirá una línea en el centro. Se puede ajustar por separado del [umbral al que se combinan las dos líneas del centro] (wall_split_middle_threshold.md).

Este ajuste es el mismo que el [Ancho mínimo de la línea de pared impar](min_odd_wall_line_width.md), pero utiliza una unidad diferente. La unidad de este ajuste está en fracciones de ancho de línea que el ancho de una pieza necesita aumentar para añadir una nueva línea media.

<!--screenshot {
"image_path": "min_wall_line_width_0_34.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
<!--screenshot {
"image_path": "min_wall_line_width_odd_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_odd_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![Cuando la línea central es demasiado pequeña, las dos líneas que la rodean se hacen más anchas](../images/min_wall_line_width_0_34.png)
![Al reducir este ajuste, la línea central comienza y termina mucho más pequeña](../images/min_wall_width_odd_0_1.png)

Líneas pares e impares
----
Esta configuración permite ajustar el umbral para añadir líneas específicamente cuando se convierte en un número impar de líneas. Esto es cuando hay una sola línea en el centro en lugar de dos. Determina cuándo se añade una nueva línea entre las dos líneas centrales.

El umbral para añadir una línea central puede ser diferente del umbral para dividir la línea central en dos, debido a la forma en que hacen la transición. Cuando se añade una línea impar, ésta comienza sólo cuando las dos líneas circundantes le han dejado paso. Durante la transición hay un pequeño hueco en el que las líneas circundantes aún no han hecho suficiente espacio. Esto es diferente de cuando hay un número par de paredes: La línea del medio se divide en dos, y esas dos líneas se superponen ligeramente hasta que están lo suficientemente separadas. Reduciendo el Umbral de Añadir Línea Media se reduce el tamaño del hueco en las transiciones de las líneas pares a las impares. Al reducir el Umbral de línea media dividida se reduce la sobreextrusión en las transiciones de líneas pares a impares.

Los huecos que quedan cuando se inicia una línea impar son más visibles en el resultado final que un poco de sobreextrusión en una unión, por lo que podría ayudar establecer el Umbral de Añadir Línea Media un poco más bajo que el Umbral de Dividir Línea Media.

La reducción de este ajuste conduce a:
* Espacios más pequeños cuando termina una línea central.
* Reducción del ancho máximo de un par de líneas centrales pares.
* Líneas más finas, que pueden no extruirse bien.
* Líneas más largas, que tardan más en imprimirse.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes extra piel, paredes de soporte, paredes de relleno y patrones concéntricos.**