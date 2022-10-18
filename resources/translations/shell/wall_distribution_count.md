Recuento de distribución de pared
====
Cura puede ajustar el ancho de las líneas de las paredes para que se ajusten mejor a la forma que está imprimiendo, pero no tiene que ajustar todas las paredes en la misma medida. Prefiere cambiar el ancho de las paredes más hacia el interior del modelo. Este ajuste determina el número de paredes, contando desde dentro hacia fuera, que se ajustan para adaptarse al espacio disponible.

<!--screenshot {
"image_path": "wall_distribution_count_1.png",
"models": [
	{
		"script": "misaligned_ring.scad",
		"transformation": ["scale(2)"]
	}
],
"camera_position": [-11, 0, 111],
"settings": {
	"wall_line_count": 5,
	"wall_distribution_count": 1
},
"colour_scheme": "line_width",
"colours": 128
}-->
<!--screenshot {
"image_path": "wall_distribution_count_5.png",
"models": [
	{
		"script": "misaligned_ring.scad",
		"transformation": ["scale(2)"]
	}
],
"camera_position": [-11, 0, 111],
"settings": {
	"wall_line_count": 5,
	"wall_distribution_count": 5
},
"colour_scheme": "line_width",
"colours": 128
}-->
![Concentrado en el centro, con grandes variaciones en el ancho de las líneas](../images/wall_distribution_count_1.png)
![Repartidas en muchas paredes](../images/wall_distribution_count_5.png)

Las paredes de ancho variable son más difíciles de imprimir que las paredes de ancho constante. Se necesita algo de tiempo para ajustar el flujo de salida de la boquilla, y para la transición también tiene que hacer algunas esquinas afiladas que pueden causar anillos. Todo esto es mejor hacerlo lo más lejos posible del exterior, donde sería visible en la superficie de la impresión. Así que Cura concentrará los ajustes de ancho de línea en las paredes más internas.

Por otro lado, concentrar la variación también significa que esas líneas en el centro tendrán anchos muy divergentes. Repartir eso en más líneas significa que la amplitud de las variaciones puede ser menor, reduciendo el impacto del ancho de línea variable en lugar de ocultarlo en el interior.

Este ajuste selecciona un número de paredes del interior entre las que se puede ajustar el ancho de línea para llenar el espacio disponible. Esto cuenta en ambas direcciones desde el centro, por lo que si se ajusta a 2, se pueden ajustar hasta 4 paredes en el centro. El ajuste tampoco se reparte uniformemente dentro de esas paredes. Las paredes del centro siempre se ajustarán un poco más que las paredes más cercanas al exterior.

La pared exterior se mantiene siempre en el ancho de línea nominal siempre que sea posible. Esta pared influye tanto en la calidad de la impresión que se mantiene con un ancho de línea constante para que la superficie sea lo más lisa posible. Sólo si la pieza se vuelve tan fina que se compone únicamente de paredes exteriores, se ajustarán dichas paredes.

En la práctica, ocultar las imperfecciones en el centro es casi siempre una estrategia mejor que repartir las imperfecciones en varias paredes. Por ello, es mejor mantener este ajuste lo más bajo posible. Cuando se trabaja con materiales que son difíciles de extruir o cambiar el flujo, como los materiales flexibles, ayuda a aumentar este ajuste para reducir los cambios de flujo. Sin embargo, nunca puede evitar esos cambios de flujo por completo.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes de forro adicionales, los soportes, los muros de relleno y los patrones concéntricos.**