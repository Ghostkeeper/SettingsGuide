Zonas no permitidas para la boquilla
====
Este ajuste indica las áreas de su placa de impresión donde no se permite que vaya la boquilla activa. El usuario no puede colocar ningún objeto en esas áreas, o lo suficientemente cerca como para que se imprima algo allí (como un borde).

![Las zonas grises indican las áreas no permitidas alrededor de los clips en la placa de construcción](../images/machine_disallowed_areas.png)

Esta configuración sólo se aplica a la boquilla *activa*, lo que significa que todavía puede imprimir objetos junto a estas áreas no permitidas, incluso si eso causaría que otras boquillas se muevan sobre esas áreas no permitidas. Por lo tanto, este ajuste sólo es útil para las impresoras que levantan las boquillas inactivas o las aparcan fuera del volumen de construcción cuando están inactivas. Al contrario de lo que ocurre con las [Áreas no permitidas] ordinarias (machine_disallowed_areas.md), estas áreas no permitidas no se mueven en función del desplazamiento entre las boquillas.

Estas áreas prohibidas son necesarias para evitar que la boquilla colisione con cosas. Por ejemplo, puede haber algunos clips en la placa de construcción, o una pegatina o un logotipo. Si el usuario imprimiera demasiado cerca de estos objetos, la boquilla colisionaría con ellos. En el mejor de los casos se obtendría un [desplazamiento de capa] (../troubleshooting/layer_shift.md). En el peor de los casos, se dañaría la tobera o el objeto con el que colisiona.

Las áreas no permitidas se dibujan como una sombra gris en la placa de construcción, indicando al usuario que no puede colocar ningún objeto allí. Estas sombras pueden expandirse en todas las direcciones para evitar que el borde o el faldón choquen con ellas y por otras razones diversas. También hay otras sombras en la placa de impresión, por ejemplo para limitar el rango de movimiento si las boquillas tienen un desplazamiento.

**Puesto que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**