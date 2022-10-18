Granos ('Blobs')
====
Los blobs son pequeñas motas en el lateral del modelo. A veces son sólo puntos. A veces son rayas. Son un defecto visual de la superficie y pueden aumentar la fricción entre las superficies que deben deslizarse unas sobre otras en un mecanismo.

Algunas manchas en esta superficie](../images/blobs.jpg)

Hay varias causas posibles para los blobs. Es uno de los defectos más comunes en la impresión 3D. Este artículo enumera algunas causas posibles y sus soluciones.

La boquilla se ralentiza
----
Si la boquilla se mueve más lentamente en una pista determinada que en otras, permitirá que se deposite más material allí. Este material fluye hacia fuera de la superficie de la pared, formando una mancha.

Es probable que la alimentación de material se reduzca con ello. Sin embargo, aunque el alimentador se mueva más despacio, pueden pasar unos segundos hasta que el caudal que sale por la abertura de la boquilla se reduzca en consecuencia. Durante ese tiempo, se extruirá demasiado material, lo que dará lugar a manchas.

Para combatir esto, mire los siguientes ajustes:
* Igualar la velocidad de la [pared exterior](../speed/speed_wall_0.md) para que sea la misma que la de lo que se imprime antes (como las [paredes interiores](../speed/speed_wall_x.md) o [relleno](../speed/speed_infill.md)). Entonces no habrá ralentización.
* Aumentar la [tasa de sacudidas durante la pared exterior](../speed/jerk_wall_0.md). Esto evitará que la boquilla se ralentice en las curvas.
* Reduzca la [resolución](../meshfix/meshfix_maximum_resolution.md) y aumente la [desviación](../meshfix/meshfix_maximum_deviation.md) para evitar que el controlador de movimiento ralentice la boquilla para poder seguir el ritmo de los códigos g que necesita procesar.
<!--if cura_version<5.0:* Desactivar el ajuste [Compensar solapamientos de paredes exteriores](../shell/travel_compensate_overlapping_walls_0_enabled.md). Este ajuste puede crear nuevos comandos de movimiento con diferentes velocidades de avance. Si se desactiva esta función, se reduce el número de comandos de movimiento en la pared.-->

La boquilla se queda parada
----
Si la boquilla hace pequeñas pausas durante la impresión de la pared exterior, lo más probable es que esté esperando a que el procesador de su impresora 3D procese nuevos comandos de movimiento. El software de planificación del movimiento de la impresora suele mantener un búfer con comandos preprocesados listo para estas ocasiones, donde los comandos de movimiento ya han sido procesados para que la impresora conozca con precisión los tiempos de activación de los motores paso a paso u otros movimientos. Si este búfer se agota, se denomina "infrautilización del búfer". Esto hace que aparezcan manchas en la superficie.

Para evitarlo, es necesario reducir la resolución del g-code.
* Aumentar la [Resolución máxima] (../meshfix/meshfix_maximum_resolution.md), lo que hace que Cura produzca segmentos de línea más largos.
* Aumentar el ajuste [Desviación máxima](../meshfix/meshfix_maximum_deviation.md), que permite a Cura reducir la resolución aún más desviándose más de la ruta original.
<!--if cura_version<5.0:* Desactivar el ajuste [Compensate Outer Wall Overlaps](../shell/travel_compensate_overlapping_walls_0_enabled.md). Si la pared exterior se solapa con otras paredes exteriores, daría a parte de la pared un ancho de línea diferente, pero eso necesita un comando de movimiento extra. Para reducir los comandos de movimiento, puede desactivar esto. Sin embargo, esto también podría causar una sobreextrusión en esas paredes, lo que causa manchas también.-->
* Reducir la [velocidad de impresión de la pared exterior](../speed/speed_wall_0.md). Esto reduce la velocidad de ejecución de los comandos de movimiento, permitiendo a la CPU ponerse al día.

Los movimientos de desplazamiento a través de las paredes
----
Mientras que Cura generalmente evitará cruzar la pared exterior tanto como sea posible, a veces esto es inevitable. Si la boquilla lleva algo de material rezumado mientras cruza una pared exterior, este material puede limpiarse allí, dejando una mancha.

Esta causa de las manchas puede evitarse ajustando los siguientes parámetros:
* Asegúrese de que [peinado](../travel/retraction_combing.md) está activado. Esto hace que la boquilla rodee las paredes tanto como sea posible, en lugar de atravesarlas.
* Habilitar [Saltos en Z](../travel/retraction_hop_enabled.md). Si las paredes están cruzadas, esto hará que la boquilla se mueva un poco hacia arriba, para pasar por encima de la pared en lugar de atravesarla. Lo más probable es que el material rezumado no se limpie en la pared, sino donde aterrice la boquilla después del movimiento de desplazamiento. Cura siempre intentará aterrizar en el relleno o la piel si es posible.
* Asegúrese de que [el orden de impresión de la pared está optimizado](../shell/optimize_wall_printing_order.md). Esto reduce el número de movimientos realizados durante la impresión de muros, permitiendo movimientos más eficientes y reduciendo la posibilidad de que algunos de estos movimientos deban atravesar un muro exterior.

Presión acumulada
----
Si la boquilla está sobreextruyendo, la extrusión puede volverse irregular. A veces, esto puede encontrar una salida repentina cuando se imprime un rincón particular de su impresión (en particular en los salientes). A veces esta presión reprimida explota, dejando una gran mancha. Lo normal es que después de la mancha haya una franja de presión que disminuye gradualmente.

Para reducir este efecto, aquí hay un par de ajustes a considerar:
* Reducir la [anchura de la línea de la pared](../resolution/wall_line_width.md). Esto reduce la presión en la cámara de la boquilla en general.
* Reducir el [Outer Wall Inset](../shell/wall_0_inset.md). Este ajuste hace que la pared exterior se superponga con la pared interior adyacente, de modo que la pared se empuja sobre la pared interior con más fuerza, mejorando la resistencia. Sin embargo, este empuje también aumenta la presión dentro de la cámara de la boquilla.

Agua dentro del filamento
----
Si el filamento ha acumulado humedad mientras estaba en la bobina, esta agua se calentará en la boquilla más allá de su punto de ebullición. El vapor de agua explotará fuera de la boquilla cuando sea empujado hacia fuera. Esta pequeña explosión puede hacer volar algo de plástico fuera del camino, resultando en una pequeña mancha en su superficie.

Costuras
----
En el lugar donde se inicia el perímetro de la pared exterior y se cierra, se creará una costura. Esto no es lo que normalmente se llama una mancha, aunque se parece. Consulte el artículo sobre [costuras](seam.md) para saber cómo reducir este efecto.

Si la [Alineación de la costura Z](../shell/z_seam_type.md) se establece en "Aleatorio", la costura se extenderá por todo el modelo, creando pequeñas costuras por todas partes. Esto puede parecer una mancha, aunque en realidad es una costura. Cambie la configuración de la alineación de la costura Z para ocultar estas costuras.