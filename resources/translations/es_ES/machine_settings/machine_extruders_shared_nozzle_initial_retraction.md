Retracción inicial de la boquilla compartida
====
Si los extrusores de una impresora [comparten una boquilla](machine_extruders_share_nozzle.md), Cura no asume que todos los extrusores comienzan con el filamento en la punta de la boquilla. Este ajuste indica a qué distancia de la boquilla comienza el filamento. El filamento puede comenzar a una distancia diferente de la [Distancia de retracción del interruptor de la boquilla](../dual/switch_extruder_retraction_amount.md) porque el filamento puede estar almacenado más lejos mientras la impresora estaba inactiva que cuando el extrusor está parado durante la impresión.

Distancia del filamento inactivo antes de la impresión](../images/machine_extruders_shared_nozzle_initial_retraction.svg)

Cura utilizará esto para asegurarse de que el filamento está en la punta de la boquilla antes de iniciar su procedimiento de cebado para el primer cambio de extrusor.