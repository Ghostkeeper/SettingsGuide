Desplazamiento de capas
====
Un desplazamiento de capa se produce cuando las capas de una impresión no se apilan correctamente unas sobre otras. Si el cabezal de impresión se desplaza durante la impresión de una capa por alguna razón, la impresora continúa imprimiendo con un desplazamiento. Como resultado, la parte superior de la impresión se desplaza con respecto a la parte inferior.

Desplazamiento de una capa debido a una obstrucción](../images/layer_shift_single.jpg)

Causas
----
Hay dos tipos de desplazamiento de la capa.

Un tipo de desplazamiento de capa se produce cuando el cabezal de impresión se obstruye en algún punto del recorrido. Esto provoca un desplazamiento de la capa en un punto a mitad de la impresión. Esto puede ocurrir cuando el usuario coloca algo dentro del pórtico mientras imprime, o cuando el cabezal de impresión choca con otro objeto mientras imprime en modo [uno a la vez] (../blackmagic/print_sequence.md). Si el cabezal de impresión choca con algo y no puede moverse, los motores se saltarán algunos pasos. Si la impresora no es capaz de detectar que esto ha ocurrido, continuará sin ese movimiento, desplazando el resto de la impresión.

Otro tipo de desplazamiento de la capa se produce cuando el propio trabajo de impresión impone demasiada fuerza sobre el cabezal de impresión, haciendo que los motores paso a paso de la impresora pierdan pasos. Cada vez que se pierden pasos, la impresión se desplaza a partir de ahí. Normalmente, la pérdida de pasos se produce en el mismo lugar en cada capa debido a una esquina especialmente afilada. El resultado es que toda la impresión o una parte de ella aparece torcida.

Prevención
----
El primer tipo de desplazamiento de capa no se previene normalmente ajustando Cura. Cura está diseñado para evitar que se golpeen los lados del volumen de impresión. Si el tamaño del volumen de impresión se introduce correctamente en Cura, no debería generar ningún g-code que se desplace fuera del volumen imprimible. Si se genera dicho código g, el cuadro de diálogo Configuración de la máquina en la gestión de la impresora le permitirá ajustar el tamaño del volumen de impresión para realizar una corrección. También debe asegurarse de que no hay obstrucciones en el volumen de impresión que el cabezal de impresión o el sistema de movimiento puedan golpear durante la impresión. Las impresoras no suelen detectar que esto ocurre, por lo que seguirán imprimiendo desde una posición desplazada. Busque cables que estén en el camino y asegúrese de que todos los cables son lo suficientemente largos para permitir el rango completo de movimiento de la impresora. Comprueba también que los controladores de los pasos de la placa de circuitos de la impresora no se estén sobrecalentando, lo que podría hacer que dejaran de funcionar temporalmente.

El otro tipo de desplazamiento de la capa, el que ocurre continuamente durante la impresión, es probablemente causado por tener demasiada fuerza en su sistema de movimiento. Hay varias soluciones posibles.

En primer lugar, debería examinar su hardware. ¿Están apretadas las correas? Si no es así, puedes buscar la manera de tensarlas. Algunas impresoras tienen posiciones de motor ajustables que le permiten apretar las correas. ¿Se deslizan las poleas? Aprieta los tornillos de las poleas para estar seguro. Por último, un problema eléctrico común es que los motores no reciben suficiente corriente para generar fuerzas lo suficientemente fuertes como para hacer un giro brusco. En ese caso, comprueba si la fuente de alimentación es suficiente.

Si el hardware funciona bien, también puedes ajustar que Cura sea un poco más suave con el hardware. Estos son algunos de los ajustes que puedes realizar:
* Bajar los [índices de impulso](../speed/jerk_print.md). Esto hará que el cabezal de impresión se ralentice antes de hacer las esquinas. Esto hace que la curva sea más suave, facilitando la entrada en la curva en lugar de hacer un giro brusco.
* Bajar los [índices de aceleración](../speed/acceleration_print.md). Esto hará que el cabezal de impresión reduzca su velocidad con más cuidado y durante más tiempo antes de tomar una curva (aunque la velocidad a la que el cabezal de impresión pasará por el ápice de la curva no se verá afectada; ese es el propósito del ajuste del impulso).
* Bajar la [velocidad de desplazamiento](../speed/speed_travel.md). Esto reduce la fuerza con la que la boquilla patina sobre las piezas previamente impresas.
* Activar [z hops](../travel/retraction_hop_enabled.md). Esto evita que el cabezal de impresión golpee las piezas previamente impresas si sobresalen un poco hacia arriba debido a las manchas o a la deformación.