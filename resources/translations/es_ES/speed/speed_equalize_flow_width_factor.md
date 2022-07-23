Relación de ecualización del flujo
====
Esta característica le permite cambiar la forma en que su impresora utilizará para ajustar el ancho de línea: en lugar de cambiar la tasa de flujo de material a través de la boquilla, la impresora cambiará la velocidad a la que se mueve la boquilla.

Las impresoras FFF son notoriamente malas para cambiar la velocidad a la que el material sale de la boquilla. Si la impresora cambia la velocidad del alimentador, pasa una fracción de segundo antes de que esto se traduzca realmente en un cambio de caudal. En ese momento, dependiendo de la velocidad de impresión, la boquilla puede estar ya varios milímetros más allá del punto en el que debería haberse ajustado el caudal. Esto es aún peor si su impresora tiene el alimentador separado del cabezal de impresión con un tubo Bowden en medio.

En lugar de cambiar la velocidad de alimentación, la impresora también puede cambiar la velocidad de movimiento del cabezal de impresión. El cabezal de impresión puede acelerar mucho más rápido y así podría obtener un mejor control sobre el ancho de la línea. Si el cabezal de impresión se acelera mientras se mantiene el mismo caudal, la misma cantidad de material se extiende a lo largo de una mayor longitud, lo que reduce la anchura de la línea. Si el cabezal de impresión se ralentiza, la misma cantidad de material se agrupa en un espacio más pequeño, lo que aumenta la anchura de la línea.

Este ajuste es una relación. Puede ajustar el caudal (0%) o la velocidad de impresión (100%) o una combinación de ambos. La relación puede incluso superar el 100%, lo que significa que el caudal se reduce para producir líneas más gruesas, pero la velocidad se reduce aún más para compensar.

Aumentar esta relación hacia el 100% significa que se utiliza la velocidad en lugar del caudal para cambiar el ancho de línea, lo que tiene los siguientes efectos en la impresión:
* El ancho de línea es probablemente más preciso, mejorando la precisión dimensional de la impresión.
* La velocidad de flujo se mantendrá igual, lo que hace que la impresión sea más fiable, especialmente con materiales exóticos.
* En algunos lugares, el cabezal de impresión se mueve más rápido, lo que resulta en el timbre.

Este ajuste sólo se aplica a las variaciones en la anchura de las líneas causadas por el ajuste de las líneas en la anchura de las piezas finas y las esquinas afiladas. Los cambios en la velocidad de flujo debidos a ajustes como diferentes anchos de línea para el relleno frente a la pared no se compensarán, ni tampoco características como el puenteado o el alisado. Las impresoras que implementan el Avance Lineal o características similares de compensación deben seguir utilizándolas, incluso si este ajuste está establecido al 100%, porque los cambios de flujo pueden seguir ocurriendo debido a esos ajustes.