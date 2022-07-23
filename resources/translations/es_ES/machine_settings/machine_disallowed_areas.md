Zonas no permitidas
====
Este ajuste indica las áreas en su placa de construcción donde el cabezal de impresión no puede ir. El usuario no puede colocar ningún objeto en esas áreas, o lo suficientemente cerca como para que se imprima algo allí (como un borde).

Los parches grises indican las áreas no permitidas alrededor de los clips en la placa de construcción](../images/machine_disallowed_areas.png)

Estas áreas prohibidas son necesarias para evitar que el cabezal de impresión colisione con cosas. Por ejemplo, puede haber un cepillo de limpieza al alcance del cabezal de impresión en algún lugar, o una bahía de conmutación, o una cámara que sobresale ligeramente demasiado dentro del volumen de construcción. Si el usuario imprimiera demasiado cerca de estos objetos, el cabezal de impresión colisionaría con ellos. En el mejor de los casos, se obtendría un [cambio de capa] (../troubleshooting/layer_shift.md). En el peor de los casos, se dañaría el cabezal de impresión o lo que sea que colisione con él.

Las áreas no permitidas se dibujan como una sombra gris en la placa de construcción, indicando al usuario que no puede colocar ningún objeto allí. Estas sombras pueden expandirse en todas las direcciones para evitar que el borde o la falda choquen con ellas y por otras razones diversas. También hay otras sombras en la placa de construcción, por ejemplo para limitar el rango de movimiento si las boquillas tienen un desplazamiento.

Si sólo la boquilla activa pudiera colisionar con los obstáculos, entonces el ajuste similar [Nozzle Disallowed Areas](nozzle_disallowed_areas.md) puede evitar que la boquilla colisione con ella mientras sigue permitiendo que el cabezal de impresión se mueva sobre ella.

**Como se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**