Distancia del filtro de transición a la pared
====
Algunos modelos tienen piezas finas que rondan el umbral donde se utilizan diferentes números de paredes. Esto puede hacer que el número de paredes se altere de un lado a otro aunque el ancho real de la pieza no varíe mucho. La alternancia arruina la calidad de la impresión, requiriendo muchos cambios de flujo y añadiendo más movimientos de desplazamiento. Utilizando esta función, se eliminan las transiciones si se hubiera hecho una transición hacia adelante y hacia atrás dentro de una determinada distancia.

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
![Sin filtro, alterna entre 2 y 3 paredes](../images/wall_transition_filter_off.png)
![Con filtro, ya no se alterna](../images/wall_transition_filter_on.png)

Cuando se elimina una transición, entonces temporalmente algunas de las líneas pueden quedar demasiado anchas o demasiado finas, excediendo el [Ancho mínimo de línea de la pared](min_wall_line_width.md). Después de todo, había una transición allí para ajustarse mejor al ancho de la pieza. Sin esa transición, utilizará una cantidad de paredes inferior o superior a la que sería ideal, y el ancho de esas paredes se ajustará en consecuencia. Esto se permite hasta el [Margen del filtro de transición de paredes](wall_transition_filter_deviation.md). Si el ancho de las paredes varía demasiado, la transición no se elimina.

Este filtro pretende resolver un problema común con las piezas delgadas que utilizan mallas 3D de baja resolución. El modelo 3D, formado por triángulos planos, no puede representar una curva exactamente, sino que sólo se aproxima a ella. La curva tendrá aristas, con superficies planas entre ellas. Al modelar una pieza curva con un ancho constante, es importante que las aristas del exterior se alineen con las del interior. Si no lo hacen, el ancho del anillo varía ligeramente, lo que puede causar el efecto mostrado arriba. Si lo hace, el filtro de transición debería evitar que tenga demasiado efecto.

Aumentar la distancia evita crear pequeños segmentos de línea en algunos casos. Esto es más rápido de imprimir y puede hacer que la superficie parezca más suave. Sin embargo, también hace que una mayor parte de la impresión tenga anchos de línea extremos, que pueden no salir bien de la boquilla. Cuando se imprimen modelos de baja resolución con piezas finas, aumentar la distancia puede ayudar a mejorar la calidad. Con materiales difíciles, es mejor permanecer en el lado seguro.

**Este ajuste no es actualmente visible para el usuario. El filtro sólo puede ajustarse mediante el [Margen del filtro de transición de la pared](wall_transition_filter_deviation.md). Afecta no sólo a las paredes normales, sino también a las paredes de piel extra, los muros de soporte, los muros de relleno y los patrones concéntricos.**