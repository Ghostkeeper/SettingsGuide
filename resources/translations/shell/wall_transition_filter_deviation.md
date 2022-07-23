Margen del filtro de transición de pared
====
Algunos modelos tienen piezas finas que rondan el umbral donde se utilizan diferentes números de paredes. Esto puede hacer que el número de paredes se altere de un lado a otro aunque el ancho real de la pieza no varíe mucho. La alternancia arruina la calidad de la impresión, requiriendo muchos cambios de flujo y añadiendo más movimientos de desplazamiento. Utilizando esta función, se eliminan las transiciones si se hubiera hecho una transición hacia adelante y hacia atrás.

Cuando se elimina una transición, entonces temporalmente algunas de las líneas pueden quedar demasiado anchas o demasiado finas. Este ajuste pone un límite a las transiciones que se filtran, limitando cuánto más ancha o fina puede ser la línea.

<!--screenshot {
"image_path": "wall_transition_filter_off.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 0,
	"wall_transition_filter_margin": 0,
	"wall_line_count": 3
},
"colours": 64
}-->
<!--screenshot {
"image_path": "wall_transition_filter_on.png",
"models": [{"script": "signet.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_filter_distance": 100,
	"wall_transition_filter_margin": 0.2,
	"wall_line_count": 3
},
"colours": 64
}-->
![Con un margen bajo, alterna entre 2 y 3 paredes](../images/wall_transition_filter_off.png)
![Con un margen más alto, ya no se alterna](../images/wall_transition_filter_on.png)

Para ser precisos, se permite que las líneas se vuelvan más finas que el [Ancho mínimo de la línea de la pared](min_wall_line_width.md) por este margen si eso impide ir y venir entre diferentes números de paredes. Del mismo modo, también se permite que las líneas se vuelvan ligeramente más anchas por este margen, incluso si una pared adicional del Ancho de Línea de Pared Mínimo podría haber encajado también.

Este filtro pretende resolver un problema común con las piezas delgadas que utilizan mallas 3D de baja resolución. El modelo 3D, formado por triángulos planos, no puede representar una curva exactamente, sino que sólo se aproxima a ella. La curva tendrá aristas, con superficies planas entre ellas. Al modelar una pieza curva con un ancho constante, es importante que las aristas del exterior se alineen con las del interior. Si no lo hacen, el ancho del anillo varía ligeramente, lo que puede causar el efecto mostrado arriba. Si lo hace, el filtro de transición debería evitar que tenga demasiado efecto.

Aumentar el margen evita crear pequeños segmentos de línea en algunos casos. Esto es más rápido de imprimir y puede hacer que la superficie parezca más suave. Sin embargo, también permite anchos de línea más extremos, que pueden no salir bien de su boquilla. Cuando se imprimen modelos de baja resolución con piezas finas, aumentar el margen puede ayudar a mejorar la calidad. Con materiales difíciles, es mejor quedarse en el lado seguro.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes de piel extra, paredes de soporte, paredes de relleno y patrones concéntricos.**