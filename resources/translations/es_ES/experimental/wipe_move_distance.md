Distancia de movimiento de limpieza
====
Con este ajuste puede definir la distancia de los movimientos de barrido. La boquilla se moverá esta distancia para [cada movimiento de limpieza](wipe_repeat_count.md).

Inicialmente la boquilla se situará justo detrás del cepillo de limpieza en una [coordenada X determinada](wipe_brush_pos_x.md). La distancia indicada en este ajuste debe ser tal que al moverla se coloque al otro lado del cepillo. Moverse demasiado introduce movimientos innecesarios y puede hacer que la boquilla se mueva hacia el volumen de construcción, lo que puede hacer que golpee innecesariamente el modelo si [Z hops are not enabled](wipe_hop_enable.md). Si no se mueve lo suficiente puede impedir que golpee el pincel correctamente.

La distancia también puede ser negativa. La boquilla limpiará en la otra dirección entonces. Dependiendo de su elección de [coordenada X](wipe_brush_pos_x.md), esto puede ser necesario para limpiar en la dirección correcta.