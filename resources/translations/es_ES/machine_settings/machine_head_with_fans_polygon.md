Polígono de la máquina y del ventilador
====
Este ajuste le dice a Cura cuál es la forma de su cabezal de impresión, visto desde arriba. Esto es necesario para evitar colisiones cuando se imprime en el modo [one-at-a-time](../blackmagic/print_sequence.md).

![Dimensiones del cabezal de impresión](../images/head_dimensions.svg)
![Visto desde arriba, la forma del cabezal de impresión es relativa a la posición de la boquilla](../images/machine_head_with_fans_polygon.png)

Este ajuste contiene una lista de coordenadas que forman un polígono. Las coordenadas son relativas a la "posición" de la cabeza, con respecto a la cual las boquillas también se posicionan relativamente.

Cura utiliza esto para crear un área de colisión alrededor de los objetos que está imprimiendo en el modo uno a uno. Esta área de colisión evita que coloques los objetos demasiado cerca unos de otros de forma que no puedan imprimirse sin que el cabezal de impresión golpee el modelo previamente impreso. Sin embargo, el área de colisión no tiene la misma forma que el propio cabezal de impresión: será un casco convexo alrededor del cabezal de impresión para evitar también las colisiones durante los movimientos de desplazamiento. También se reducirá para que sea simétrica. Por ejemplo, si la boquilla está más hacia el lado izquierdo del cabezal de impresión (como en la imagen de arriba) entonces el área de colisión se encogerá de tal manera que otro objeto puede ser colocado cerca del lado derecho de los objetos previamente impresos. El orden en que se imprimen estos objetos se ajustará entonces para que puedan imprimirse sin colisiones.

**Como este es un ajuste de la máquina, normalmente no aparecerá en la lista normal de ajustes. Sin embargo, el tamaño del cabezal de impresión se puede anotar de forma rudimentaria en el diálogo de configuración de la impresora, que se encuentra en la lista de impresoras añadidas en el diálogo de preferencias. Allí sólo se puede especificar la posición izquierda, derecha superior e inferior del cabezal de impresión.**