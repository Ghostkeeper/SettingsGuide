Tipo de g-code
====
Aunque el g-code es un formato estandarizado para comunicar instrucciones a máquinas CNC como las impresoras 3D, todavía hay algunas diferencias en los g-codes que soporta cada impresora, cuál es su estado inicial y, a veces, en cómo interpretan los comandos. Con el tipo de g-code puedes indicar en gran medida qué conjunto de comandos acepta tu impresora.

La diferencia entre los tipos de g-code suele se bastante pequeña. Los comandos más importantes, como el movimiento y el calentamiento de la boquilla, suelen ser los mismos.

Para seleccionar el tipo de g-code correcto, consulta la documentación del firmware de su impresora, donde se indica qué funciones son compatibles y cuáles no. Estos son los tipos disponibles en Cura, y sus diferencias.

Marlin
----
Marlin se considera la variante de código g por defecto. Está pensado para la línea principal [Marlin firmware](https://marlinfw.org/) que es el firmware de impresión 3D más popular y la base de la mayoría de los firmwares alternativos que existen.

Marlin (volumétrico)
----
Se trata de una variante de Marlin en la que los comandos de extrusión especifican la cantidad que extruyen en milímetros cúbicos, en lugar de en longitudes de filamento. Estos son los cambios notables:
* El parámetro `E` del comando `G1` se calcula en milímetros cúbicos, el volumen del plástico alimentado, en lugar de la longitud del filamento a alimentar durante este movimiento.
* Las estadísticas al inicio del código g también mencionan el filamento utilizado en milímetros cúbicos.

RepRap
----
Esta es una variante centrada en el apoyo a las impresoras que evolucionó a partir del [proyecto RepRap](https://reprap.org/wiki/RepRap). Tiene una serie de excepciones notables:
* Mencionar siempre el extrusor cuando se establece la temperatura de la capa inicial, incluso si sólo hay un extrusor.
* Revertir a la extrusión relativa después de la impresión.
* Cambiar las aceleraciones utilizando los parámetros `P` y `T` del comando `M204`, para la aceleración de impresión y la aceleración de desplazamiento respectivamente, en lugar del parámetro `S`.
* Cambiar el tirón utilizando el comando `M566`, en lugar del comando `M205`.

Ultimaker 2
----
Esta variante de g-code está destinada a la familia Ultimaker 2. El firmware de esta familia tuvo la extraña idea de dejar que la impresora controle los ajustes relacionados con el material en lugar de la cortadora. Estas son las excepciones:
* No habrá comandos de temperatura de impresión en el g-code.
* No habrá comandos de temperatura de la placa de impresión en el g-code.
* No habrá comandos de temperatura del volumen de impresión en el g-code.
* Se asume que la primera boquilla tiene la [temperatura de impresión de la capa inicial](../material/material_print_temperature_layer_0.md) cuando la impresión comienza.
* Se asume que la placa de impresión tiene la [temperatura de la placa de impresión de la capa inicial](../material/material_bed_temperature_layer_0.md) cuando se inicia la impresión.
* El parámetro `E` del comando `G1` se calcula en milímetros cúbicos, el volumen del plástico alimentado, en lugar de la longitud del filamento a alimentar durante este movimiento.
* Las estadísticas al inicio del código g mencionan el filamento utilizado en milímetros cúbicos.

Griffin
----
Esta es la variante del g-code para las impresoras Ultimaker modernas, la Ultimaker 3 y las más nuevas. Estas impresoras requieren un montón de metadatos en un determinado formato al comienzo del g-code. Las diferencias en este variante g-code son:
* Hay una gran cabecera al comienzo del g-code que contiene información de metadatos como la duración de la impresión, el nombre del trabajo de impresión, y alguna información práctica como la temperatura de inicio y el cuadro delimitador de la impresión.
* No habrá comandos de temperatura de volumen de construcción en el g-code.
* Se asume que la primera boquilla tiene la [temperatura de impresión de la capa inicial](../material/material_print_temperature_layer_0.md) cuando la impresión comienza.
* Se supone que la placa de impresión tiene la [temperatura de la placa de impresión de la capa inicial](../material/material_bed_temperature_layer_0.md) cuando se inicia la impresión.
* Se asume que la impresora no comienza en el primer extrusor, por lo que siempre cambiará al extrusor inicial al comienzo de la impresión utilizando un comando `T`.
* Se imprime un blob primario con `G280` para cada extrusor cuando comienza a imprimir por primera vez, en lugar de una retracción.

Makerbot
----
Esta es una variante de g-code destinada al firmware basado en [Sailfish](https://www.sailfishfirmware.com/). Este firmware se utiliza en la descendencia de las impresoras Makerbot originales. Algunas diferencias notables son:
* Cuando se cambia la temperatura de impresión, `M109` (fijar temperatura y esperar) no es soportado. En su lugar, utiliza `M104`, que no espera hasta que se alcanza la temperatura. Entonces utiliza `M116` para ordenar a la impresora que espere hasta que se alcance esta temperatura.
* La dimensión `E` del comando de extrusión `G1` no se restablece durante la impresión. En otros modelos, este parámetro se restablece después de cada 10 metros de filamento utilizando un comando `G92 E0`, para evitar errores de redondeo en coma flotante en el firmware, pero no en este caso.
* El cambio de extrusores se realiza con el comando `M135` y no con los comandos `T`.
* La velocidad del ventilador no se muestra. El ventilador está completamente encendido o apagado. Cura ordenará a la impresora que encienda el ventilador si desea una velocidad del ventilador del 50% o más.

Bits from Bytes
----
Esta es una versión de g-code dirigida a las impresoras Bits from Bytes que tienen su propio firmware personalizado. Su versión de g-code difiere considerablemente de las demás. Estos son los cambios que hará Cura:
* La cantidad de extrusión se escribe usando las RPM del alimentador en vez del parámetro `E`.
* Las retracciones se escriben con `M101` o `M201`, dependiendo del extrusor activo.
* La velocidad de retracción se escribe con un comando separado `M108`.
* Los movimientos de desplazamiento se indican con el comando `M103`, en lugar de cambiar `G1` por `G0`. No habrá comandos `G0`.
* La impresora está configurada para usar la retracción automática con el comando `M227`.
* Cura imprimirá líneas nuevas al estilo de Windows con un retorno de carro delante, en lugar de un símbolo de línea nueva.
* La dimensión `E` del comando de extrusión `G1` no se restablece durante la impresión. En otros modelos, este parámetro se restablece después de cada 10 metros de filamento utilizando un comando `G92 E0`, para evitar errores de redondeo en coma flotante en el firmware, pero no en este caso.

Mach3
----
Esta es una variante de g-code que se acerca más a la forma en que las fresadoras CNC esperan que sea el g-code. Sólo hay una diferencia notable:
* La cantidad de extrusión se escribe con el parámetro `A` del comando `G1`, en lugar del parámetro `E`.

Repetier
----
Esta es una variante de g-code dirigido a las impresoras 3D de Repetier. Imita la salida del slicer de Repetier. Estas son las diferencias notables con este variante de g-code:
* Si las retracciones del firmware están habilitadas, las retracciones para un interruptor del extrusor utilizan `G10 S1` para indicar que se trata de una retracción para un interruptor del extrusor.
* Los cambios de aceleración se hacen usando los comandos `M201` y `M202` (para la aceleración de impresión y la aceleración de desplazamiento respectivamente) en lugar de `M204`.
* Los cambios en la aceleración se realizan utilizando el comando `M207`, en lugar del comando `M205`.

**Dado que este es un ajuste de la máquina, normalmente no aparecerá en la lista normal de ajustes. Sin embargo, hay un menú de selección para este ajuste en el diálogo de ajustes de la impresora, que se puede encontrar en la lista de impresoras añadidas en el diálogo de preferencias.**