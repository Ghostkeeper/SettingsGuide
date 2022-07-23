Altura del puente
====
Este ajuste mide la distancia entre la plataforma y el sistema de puente al que se suspende el cabezal de impresión. Esta altura es un techo cuando se imprime [un objeto a la vez](../blackmagic/print_sequence.md), ya que el objeto previamente impreso podría colisionar contra el puente.

![Dimensiones del cabezal de impresión](../images/head_dimensions.svg)

La mayoría de las impresoras 3D tienen el cabezal de impresión colgado de una o dos barras transversales. La forma de este puente no está modelada por Cura: si son dos barras cruzadas, un solo brazo que entra desde una dirección o una sola barra cruzada a lo largo de la cual el cabezal de impresión puede moverse en una dirección. Cura ve este puente como un techo duro cuando se imprime de uno en uno, independientemente del orden en que se impriman los modelos. Cuando se imprime de uno en uno, la altura del volumen de impresión se reduce a esta altura del puente, para indicar que no se permiten modelos más altos que la altura del puente.

Una excepción es cuando sólo se carga un objeto en la plataforma. Se permite que este objeto sea más alto que la altura del puente ya que no habrá nada más en la plataforma que pueda colisionar luego con el puente.

**Dado que este es un ajuste de la máquina, normalmente no aparecerá en la lista normal de ajustes. La altura del puente se puede cambiar en el diálogo de configuración de la impresora, que se puede encontrar en la lista de impresoras añadidas en el diálogo de preferencias.**