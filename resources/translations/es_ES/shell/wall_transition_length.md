Longitud de transición de la pared
====
En las piezas delgadas, no todas las paredes caben dentro de la forma. Si la pieza es más delgada en algunos lugares que en otros, Cura necesita utilizar diferentes números de paredes en algunos lugares. Este ajuste controla la anchura de la zona de transición donde se añade o elimina una de las paredes.

<!--screenshot {
"image_path": "wall_transition_length_0_2.png",
"models": [{"script": "wedge.scad"}],
"camera_position": [-7, 0, 75],
"settings": {"wall_transition_length": 0.2},
"colours": 64
}-->
<!--screenshot {
"image_path": "wall_transition_length_1_5.png",
"models": [{"script": "wedge.scad"}],
"camera_position": [-7, 0, 75],
"settings": {"wall_transition_length": 1.5},
"colours": 64
}-->
![Una transición muy corta](../images/wall_transition_length_0_2.png)
![Una transición más larga](../images/wall_transition_length_1_5.png)

La zona de transición entre diferentes números de paredes siempre tiene algunos problemas leves. Esto es más visible cuando una sola línea en el centro termina y las dos paredes circundantes tienen que llenar el espacio. No llenan inmediatamente el espacio, y queda un hueco. Esto da lugar a pequeños orificios en la parte superior e inferior de las impresiones. Lo contrario ocurre cuando dos paredes se combinan en una sola, lo que hace que se superpongan por un momento hasta que se juntan. La sobreextrusión puede dar lugar a inexactitudes dimensionales, especialmente cuando esto ocurre en la pared exterior. Todo esto puede evitarse haciendo la transición lo más corta posible.

Sin embargo, una transición corta también hace que la boquilla dé unos giros muy bruscos para rellenar rápidamente ese hueco. Esto da lugar a más anillamiento, en particular si esto ocurre para la impresión de la pared exterior. Hacer la transición más larga reduce las aceleraciones en la boquilla, en particular si esto las reduce por debajo del límite [jerk](../speed/jerk_print.md).

Ajustar esta longitud a una o dos veces el ancho de la línea es un punto de partida razonable. Las impresoras con marcos más débiles o cabezales de impresión más pesados pueden necesitar aumentarlo, mientras que las impresoras que pueden acelerar rápidamente sin que suene el timbre pueden afotar para acortar la transición para mejorar la calidad visual.

**Este ajuste no sólo se aplica a las paredes normales, sino también a las paredes de piel extra, paredes de soporte, paredes de relleno y patrones concéntricos.**