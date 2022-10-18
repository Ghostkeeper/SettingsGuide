Extrusión relativa
====
Cura escribe instrucciones para que la impresora imprima su objeto en g-code. Estas instrucciones mueven el cabezal de impresión a ciertas posiciones y el engranaje del alimentador. Cura normalmente registra tanto las coordenadas para que el cabezal de impresión se mueva como la rotación del alimentador como coordenadas absolutas. Sin embargo, si este ajuste está activado, las coordenadas del alimentador se registrarán de forma relativa.

Si se desactiva (es decir, la extrusión absoluta) la posición del filamento al inicio de la impresión se mantiene como coordenada cero. La posición del filamento aumentará a lo largo del archivo a medida que se extruya más material y el filamento tenga que moverse más y más lejos del punto de partida al principio de la impresión.

Sin embargo, si esto está activado, cada línea separada en el g-code tendrá su extrusión escrita por separado, en relación con la posición de la línea anterior. Cada línea contiene entonces sólo la cantidad de material extruido para esa línea en particular.

La extrusión relativa facilita la edición del g-code una vez generado. Si es necesario extruir material extra en algún punto intermedio (para añadir o eliminar segmentos de línea o para ajustar los caudales), la nueva extrusión simplemente tiene que escribirse en la parte que se edita. Si se utiliza la extrusión absoluta, la posición del alimentador necesita ser reajustada utilizando `G92` después para asegurarse de que todos los comandos posteriores son correctos.

Sin embargo, si se introduce algún error de redondeo en cualquier momento durante el procesamiento del código g (en Cura, el firmware o el movimiento) la extrusión absoluta lo corregirá automáticamente en la siguiente línea. En la extrusión relativa, esto conducirá a una sobreextrusión o a una subextrusión, aunque de muy poca importancia.

No todos los firmware de las impresoras soportan la extrusión relativa.

**Cuando se utiliza la extrusión absoluta, Cura restablecerá la posición del filamento cada 10 metros para evitar errores de redondeo en coma flotante en el firmware.