Extrusoras comparten boquilla
====
Con esta configuración, puede indicar que su impresora sólo tiene una boquilla, y todo el filamento es empujado a través de esa misma boquilla. Cura cambiará entonces su estrategia de cebado.

Normalmente Cura asume que después de ejecutar el [start g-code](machine_start_gcode.md), todos los extrusores tienen su filamento en la punta de la boquilla, listo para imprimir. Cuando los extrusores comparten una boquilla, esto no es posible ya que sólo un filamento puede estar dentro de la boquilla a la vez. En lugar del procedimiento normal de cebado con un [prime blob](../platform_adhesion/prime_blob_enable.md) o líneas de faldón adicionales, la boquilla debe cebarse como si se tratara de un cambio de extrusor completo. Esto implica imprimir en la [torre de cebado](../dual/prime_tower_enable.md), si está activada.

Si todos los extrusores comparten una sola boquilla, es lógico que también [compartan un calentador](machine_extruders_share_heater.md). Sin embargo, Cura no hace ningún vínculo entre los dos por sí mismo, así que asegúrese de activar ambos si su impresora tiene una sola boquilla y un solo calentador para todos los extrusores.

**Como este es un ajuste de la máquina, normalmente no aparecerá en la lista normal de ajustes. Sin embargo, hay una casilla de verificación para este ajuste en el diálogo de configuración de la impresora, que se puede encontrar en la lista de impresoras añadidas en el diálogo de preferencias.**