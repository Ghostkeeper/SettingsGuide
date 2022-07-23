Dividir umbral de línea media
====
Cuando se imprimen piezas finas, Cura ajusta el ancho de las líneas de pared para que se ajusten al ancho exacto del modelo. Cura también puede decidir utilizar menos líneas de pared en su lugar. Este ajuste es el umbral a partir del cual Cura dividirá una sola línea en el centro en dos, cuando el ancho de la pieza aumente. Se puede ajustar por separado del [umbral al que se añade una nueva línea central](wall_add_middle_threshold.md).

Este ajuste es el mismo que el [Ancho mínimo de la línea de pared uniforme](min_even_wall_line_width.md), pero utiliza una unidad diferente. La unidad de este ajuste está en fracciones de ancho de línea que el ancho de una pieza necesita aumentar para dividir la línea central en dos. Dado que la diferencia de ancho se divide entre las dos líneas del centro después de la división, un Ancho mínimo de línea de pared par menor equivale a un Umbral de línea central de división mucho menor que en el caso de eliminar una pared impar.

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
"image_path": "min_wall_line_width_even_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_even_wall_line_width": 0.1,
	"min_wall_line_width": 0.34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![La línea central se hace más ancha para que quepa](../images/min_wall_line_width_0_34.png)
![Reduciendo este ajuste, utiliza dos líneas en su lugar](../images/min_wall_line_width_even_0_1.png)

Líneas pares e impares
----
Esta configuración permite ajustar el umbral para añadir líneas específicamente cuando se convierte en un número par de líneas. Esto es cuando hay dos líneas en el centro en lugar de una sola línea. Determina cuándo una línea del centro se divide en dos líneas.

El umbral para dividir una línea del centro puede ser diferente del umbral para añadir una línea del centro debido a la forma en que se unen. Las líneas pares se unen en sus extremos haciendo que éstos se acerquen. Ahí hay un cierto solapamiento con estas líneas, lo que provoca una sobreextracción. Esto es diferente de cuando hay un número impar de paredes: La línea del medio simplemente se detiene, dejando un hueco en la impresión. Reduciendo el Umbral de línea media dividida se reduce la sobreextrusión en las transiciones de las líneas pares a las impares. Reducir el Umbral de añadir línea central reduce el tamaño del hueco en las transiciones de las líneas pares a las impares.

Los huecos que se dejan al añadir una línea central son más visibles en el resultado final que un poco de sobreextrusión en una unión, por lo que podría ayudar establecer el Umbral de línea media dividida un poco más alto que el Umbral de línea media añadida.

La reducción de este ajuste conduce a:
* Reducción del área de superposición donde dos líneas se unen para fusionarse en una sola línea.
* Reducción del ancho máximo de las líneas centrales simples.
* Líneas más finas, que pueden no extruirse bien.
* Más líneas, que tardan más en imprimirse.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes de revestimiento adicional, los soportes, las paredes de relleno y los patrones concéntricos.**