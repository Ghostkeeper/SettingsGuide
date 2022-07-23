Ancho mínimo de la línea perimetral impar
====
Cuando se imprimen piezas finas, Cura ajusta el ancho de las líneas de pared para que se ajusten al ancho exacto del modelo. Cura también puede decidir utilizar menos líneas de pared en su lugar. Este ajuste es el umbral en el que Cura eliminará una línea en el centro. Se puede ajustar por separado del [umbral en el que se combinan las dos líneas del centro] (min_even_wall_line_width.md).

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
Esta configuración permite ajustar el umbral para eliminar líneas específicamente cuando hay un número impar de líneas. Esto es, cuando hay una sola línea en el centro en lugar de dos. Determina cuándo se elimina esta única línea en favor de que las dos líneas que la rodean sean ligeramente más anchas.

El ancho mínimo de las líneas impares de la pared puede ser diferente del ancho mínimo de las líneas pares debido a la forma en que hacen la transición. Cuando se elimina una línea impar, se detiene antes de la transición y deja que las paredes circundantes se cierren. Durante la transición hay un pequeño hueco en el que las líneas circundantes aún no se han juntado del todo. Esto es diferente de cuando hay un número par de paredes: Las dos líneas del medio se juntan, superponiéndose ligeramente. Si se reduce el ancho mínimo de las líneas de pared impares, se reduce el tamaño del hueco en las transiciones de las líneas pares a las impares. Si se reduce el ancho mínimo de la pared par, se reduce la sobreextracción en las transiciones de las líneas pares a las impares.

Los huecos que quedan cuando termina una línea impar son más visibles en el resultado final que un poco de sobreextrusión en una junta, por lo que podría ayudar establecer el Ancho mínimo de línea de pared impar un poco más bajo que el Ancho mínimo de línea de pared par.

La reducción de este ajuste conduce a:
* Espacios más pequeños cuando termina una línea central.
* Reducción del ancho máximo de un par de líneas centrales pares.
* Líneas más finas, que pueden no extruirse bien.
* Líneas más largas, que tardan más en imprimirse.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes de forro adicionales, paredes de soporte, paredes de relleno y patrones concéntricos.**