Ancho mínimo de la línea perimetral uniforme
====
Cuando se imprimen piezas finas, Cura ajusta el ancho de las líneas de pared para que se ajusten al ancho exacto del modelo. Cura también puede decidir utilizar menos líneas de pared en su lugar. Este ajuste es el umbral en el que Cura combinará dos líneas en una. Se puede ajustar por separado del [umbral en el que se elimina la línea del medio] (min_odd_wall_line_width.md).

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
Esta configuración permite ajustar el umbral para eliminar líneas específicamente cuando hay un número par de líneas. Esto es, cuando hay dos líneas en el centro en lugar de una sola. Determina cuándo estas dos líneas en el centro se combinan en una sola línea.

El ancho mínimo de la pared par puede ser diferente del ancho mínimo de la pared impar debido a la forma en que se unen. Las líneas pares se unen en sus extremos haciendo que éstos se acerquen. Allí hay un cierto solapamiento de estas líneas, lo que provoca una sobreextracción. Esto es diferente de cuando hay un número impar de paredes: La línea en el centro se detiene, dejando un hueco en la impresión. La reducción del ancho mínimo de la línea de pared par reduce la sobreextrusión en las transiciones de las líneas pares a las impares. Al reducir el ancho mínimo de la pared impar se reduce el tamaño del hueco en las transiciones de las líneas pares a las impares.

Los huecos que quedan cuando termina una línea impar son más visibles en el resultado final que un poco de sobreextrusión en una junta, por lo que podría ayudar establecer el Ancho mínimo de línea de pared par un poco más alto que el Ancho mínimo de línea de pared impar.

La reducción de este ajuste conduce a:
* Reducción de la zona de solapamiento donde dos líneas se unen para formar una sola línea.
* Reducción del ancho máximo de las líneas centrales simples.
* Líneas más finas, que pueden no extruirse bien.
* Más líneas, que tardan más en imprimirse.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes de revestimiento adicional, los soportes, las paredes de relleno y los patrones concéntricos.**