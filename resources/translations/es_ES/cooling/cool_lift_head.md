Elevar cabezal
====
Cuando se alcanza el [Tiempo Mínimo de Capa](cool_min_layer_time.md), el cabezal de impresión se ralentizará para evitar imprimir más rápido que el Tiempo Mínimo de Capa. De esta manera, la capa anterior tiene tiempo para enfriarse y solidificarse antes de que la siguiente capa se ponga encima. El cabezal de impresión se ralentiza hasta que se alcanza la [Velocidad mínima] (cool_min_speed.md).

Si este ajuste está activado y el cabezal de impresión debe moverse más lento que la Velocidad Mínima para mantener el Tiempo Mínimo de Capa, entonces el cabezal de impresión se moverá ligeramente hacia arriba después de imprimir la capa. Entonces esperará un tiempo hasta que se alcance el Tiempo Mínimo de Capa, antes de comenzar con la siguiente capa.

Si este ajuste está desactivado, la impresora continuará inmediatamente con la siguiente capa. No esperará al tiempo mínimo de capa, por lo que las capas se imprimirán encima de las capas que quizás no se hayan solidificado completamente.

Cuando se alcanza el tiempo mínimo de capa, el cabezal puede levantarse](../images/cool_fan_speed.svg)

El cabezal de impresión siempre se moverá hacia arriba 3mm. No hay ningún ajuste para configurar esto por el momento.

Contrapartidas
----
Hay una compensación cuando se ralentiza la boquilla para permitir que la capa se enfríe mejor. El tiempo mínimo de la capa tiene como objetivo dar un poco de tiempo para que el material se enfríe al ralentizar el movimiento del cabezal de impresión. Durante este tiempo, los ventiladores estarán soplando a máxima potencia para que se enfríe más rápidamente, pero la boquilla caliente también está todavía sobre el plástico. En el caso de piezas muy pequeñas, la boquilla caliente puede transferir más calor a la impresión de lo que los ventiladores pueden soplar. Esto hace que el plástico se derrita aún más que si no tuviera un tiempo mínimo de capa.

Con la elevación del cabezal este compromiso se resuelve. Todavía se puede reducir la velocidad hasta un punto, pero para capas muy pequeñas se alejará la boquilla caliente, de modo que no transfiera más calor a la impresión. El cabezal se mantiene lo suficientemente cerca como para que los ventiladores del cabezal sigan soplando sobre la impresión.

La desventaja de esto es que efectivamente hará un [Z hop](../travel/retraction_hop.md), lo que trae algunos [stringing](../troubleshooting/stringing.md). Si bien el levantamiento de la cabeza puede mejorar la flacidez y la hinchazón, provocará otro tipo de desorden. Un poco de post-procesamiento manual con un cuchillo puede limpiar las cuerdas que causa.