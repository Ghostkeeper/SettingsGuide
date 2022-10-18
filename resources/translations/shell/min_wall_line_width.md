Ancho mínimo de la línea perimetral
====
Cuando se imprimen piezas finas, Cura ajusta el ancho de las líneas de pared para que se ajusten al ancho exacto del modelo. Cura también puede decidir utilizar menos líneas de pared en su lugar. Este ajuste decide el umbral en el que Cura decide eliminar una pared en lugar de hacer las paredes existentes más finas.

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
"image_path": "min_wall_line_width_0_1.png",
"models": [{"script": "moon_sickle.scad"}],
"camera_position": [0, 0, 63],
"settings": {
	"min_wall_line_width": 0.1,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"layer": 14,
"colours": 32
}-->
![Normalmente las líneas se hacen más anchas para que quepan](../images/min_wall_line_width_0_34.png)
![Al reducir el ancho mínimo de las líneas, se opta por utilizar más líneas](../images/min_wall_line_width_0_1.png)

Diferentes números de paredes
----
Si hay una sola línea central y el [Recuento de distribución de paredes](wall_distribution_count.md) está ajustado a 1, este ajuste funciona exactamente como dice. Si la línea central se hace más fina que un determinado ancho, se elimina en favor de hacer más anchas otras líneas. En otros casos, el cálculo es más complejo.

El cálculo preciso es complejo, pero una comprensión intuitiva puede ser útil. En efecto, basta con dividir el ancho total del modelo entre el [ancho de línea ordinario] (../resolution/wall_line_width.md) para llegar a un determinado número de paredes. Sin embargo, esto puede ser una fracción (como 5,3 anchos de línea de muro). El ancho mínimo de línea de muro toma sólo esa parte fraccionaria (0,3 anchos de línea) y añade una pared extra si supera el ancho mínimo de línea de muro. Conocido el número de paredes, determina entonces el ancho de cada una de las líneas según el Recuento de Distribución de Paredes.

El ancho mínimo de la línea de muro desplaza el umbral de adición de una nueva línea a la izquierda o a la derecha](../images/min_wall_line_width.svg)

Efectivamente, esto significa que si hay más líneas que obtienen su ancho ajustado, el ancho de la línea nunca será tan extremo como lo permitiría el Ancho Mínimo de Línea de Pared. Por ejemplo, si se ajustan las dos líneas del medio, el ancho de la línea no caerá por debajo del promedio del ancho de la línea normal y del Ancho mínimo de la línea de la pared.

El ajuste puede realizarse por separado para el número [par](min_even_wall_line_width.md) e [impar](min_odd_wall_line_width.md) de paredes. Tener 0 paredes es también un caso aparte, que puede ajustarse utilizando el ajuste [Minimum Feature Size](min_feature_size.md).

Ajustar
----
En teoría, establecer esto al 50% del ancho de la línea asegura que el ancho de la línea se mantenga lo más cercano al ancho de la línea ordinaria. Sin embargo, es mejor quedarse un poco por encima de eso. Es más fácil para una impresora imprimir líneas más anchas que el tamaño de la boquilla que imprimir líneas más finas, y tener menos líneas también significa que la impresión será más rápida.

Con materiales muy viscosos o cuando se imprime más rápido, el Ancho mínimo de la línea de la pared debe disminuirse para evitar crear líneas demasiado anchas. Estas son difíciles de imprimir si el material no tiene tiempo de fluir hacia los lados lo suficiente. Si el Ancho mínimo de la línea de la pared es demasiado alto, las paredes no se adhieren bien, lo que hace que la impresión sea frágil.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes extra skin, paredes de soporte, paredes de relleno y patrones concéntricos.