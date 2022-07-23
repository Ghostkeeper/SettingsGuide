Aplicar compensaciones del extrusor a g-code
====
Este ajuste decide si Cura debe escribir coordenadas para que el cabezal de impresión se mueva, o para que la boquilla se mueva.

Si su impresora tiene una sola boquilla, lo más probable es que el sistema de coordenadas de su impresora esté alineado con su boquilla. Esto significa que al moverse a la posición [50,50] realmente se mueve la punta de la boquilla a esa posición. Sin embargo, si su impresora tiene múltiples boquillas, y esas boquillas están una al lado de la otra en el cabezal de impresión, entonces sí importa.

Algunas impresoras mueven el cabezal de impresión a la misma posición independientemente de la boquilla que esté activada. Mientras que el g-code podría ordenar a la impresora que se mueva a la posición [50,50], la punta de la boquilla actualmente activa podría moverse a la posición [68,50] en su lugar, ya que está, por ejemplo, 18 mm a la derecha de la primera boquilla. Si este es el caso, este ajuste debe ser activado.

Otras impresoras ajustan automáticamente la posición del cabezal de impresión de forma que la boquilla activa se desplaza a la posición indicada en el g-code. Esto significa que si el g-code ordena a la impresora moverse a la posición [50,50], el extrusor actualmente activo se movería a esa posición. El propio cabezal de impresión se movería un poco hacia un lado para posicionar el extrusor activo allí. Si tu impresora se comporta de esa manera, este ajuste debería estar desactivado.

**Como se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**