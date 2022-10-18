Ángulo del umbral de transición de pared
====
Este ángulo indica el ángulo en el que Cura comienza a crear transiciones para rellenar adecuadamente el espacio. Cualquier esquina que sea más aguda que este ángulo se rellenará con líneas de ancho variable.

<!--screenshot {
"image_path": "wall_transition_angle.png",
"models": [{"script": "sharpening_corners.scad"}],
"camera_position": [0, 11, 106],
"settings": {
	"wall_transition_angle": 11,
	"wall_line_count": 4
},
"colours": 64
}-->
![Más allá de 10°, ya no crea transiciones](../images/wall_transition_angle.png)

En efecto, esto activa o desactiva los anchos de línea variables para ciertas esquinas. Si dos paredes opuestas son casi paralelas, más pequeñas que el ángulo especificado en este ajuste, el área entre ellas se rellena con líneas que pueden variar en su ancho. Si están en un ángulo mayor, el espacio entre ellas se rellena con paredes de ancho constante.

Como siempre, se trata de un compromiso. El uso de un ancho variable tiene algunas ventajas, como:
* No deja huecos entre las líneas.
* No rellena el mismo espacio varias veces.
* Las dimensiones de la impresión serán más exactas allí.

Sin embargo, también tiene algunas desventajas:
* Introduce esquinas en las piezas finas que pueden aparecer como ondulaciones en la superficie.
* Crea movimientos de desplazamiento adicionales.
* La impresora puede no cambiar con precisión el ancho de la línea en una sucesión rápida.

En la práctica, es bueno hacer este ángulo lo suficientemente grande como para reducir el tamaño de los huecos en las esquinas afiladas, como se puede ver en la vista de capa, pero tan pequeño como sea posible por lo demás. Un ángulo más pequeño generalmente hace que la superficie parezca más suave.

No es posible reducir el ángulo a 0° para eliminar por completo los anchos de línea variables. Las paredes paralelas opuestas siempre tendrán su ancho de línea ajustado para adaptarse al espacio.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes de revestimiento adicional, los soportes, los muros de relleno y los patrones concéntricos.