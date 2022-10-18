Impresión inacabada
====
A veces una impresión no se termina completamente. Puede haber una serie de razones por las que esto sucede, y algunas de ellas se pueden solucionar ajustando la configuración de Cura.

![El filamento dejó de fluir a mitad de esta impresión](../images/unfinished_print.jpg)

Fallos de la impresora
----
A veces la causa de una impresión inacabada es un fallo de la impresora, donde la impresora no está haciendo lo que se espera que haga. Por lo general, es muy poco lo que Cura puede hacer con estos problemas. Estas son algunas de las causas más comunes.
* Fallo de alimentación. Hay muy poco que Cura pueda hacer al respecto, aparte de imprimir más rápido para reducir las probabilidades de un fallo de alimentación durante la impresión.
* Fallo de la fuente de alimentación. Si alguna de las temperaturas (ya sea la [placa de impresión](../material/material_bed_temperature.md) o la [boquilla](../material/material_print_temperature.md)) son demasiado altas, algunas impresoras tienen un modo de fallo en el que la fuente de alimentación se quema o los sensores de temperatura dan errores. Esto hará que la impresora se apague y no termine la impresión.
* El firmware se congela. Debido a fallos en el firmware la impresora puede acabar sin responder. Si puedes rastrear en qué parte del g-code se congela (la mayoría de las veces al principio o al final de la impresión) entonces podrías ver qué g-code está causando esto. Tal vez el g-code de inicio o el g-code de finalización necesita ser ajustado.
* La bobina de filamento está enredada. Es una buena idea *sujetar siempre* el extremo del filamento si no está bien colocado en el alimentador o insertado en uno de los agujeros de la bobina (si tu bobina tiene esos agujeros). Si lo sueltas y el extremo del filamento salta de nuevo a la bobina, podría deslizarse por debajo de una de las otras bobinas y enredarse. Dado que el filamento suele tener cientos de metros de longitud, este nudo puede ser muy difícil de desenredar si se introduce.

Erosionado del filamento
----
El alimentador a veces empuja muy fuerte el filamento para hacerlo pasar por el tren de extrusión. Esto daña el filamento. Cuando el alimentador empuja y tira del mismo trozo de filamento con mucha frecuencia, puede dañarse tanto que el alimentador ya no puede agarrar el filamento. El material dejará de fluir entonces y el resto de la impresión se imprimirá en aire en lugar de plástico.

El filamento ha sido erosionado por el alimentador](../images/grinding.jpg)

Puedes sentir que esto sucede durante la impresión colocando un dedo en la abertura donde el filamento entra en el alimentador. Durante la impresión, deberías sentir que se mueve. Si no se mueve, lo más probable es que haya erosionado el material y no consiga agarrarlo. También puedes sacar el filamento de la impresora y ver dónde está dañado.

Para evitar este problema, puedes hacer los siguientes ajustes en la configuración de Cura:
* Reducir el [Recuento máximo de retracción](../travel/retraction_count_max.md) o aumentar la [Ventana de distancia mínima de extrusión](../travel/retraction_extrusion_window.md). Esto limitará el número de retracciones realizadas durante la extrusión de una longitud determinada de filamento. En efecto, esto limita la frecuencia con la que el alimentador puede rodar hacia adelante y hacia atrás a través de cada pieza de filamento.
* Reduzca la [Distancia de Retracción] (../travel/retraction_amount.md). De nuevo, esto limitará el número de veces que el alimentador va hacia adelante y hacia atrás a través del mismo trozo de filamento.
* Reduzca la [Velocidad de retracción](../travel/retraction_speed.md). Si el material se mueve rápido pero se obstruye en cualquier parte del camino, el alimentador triturará el material. Si el material se mueve más lentamente, hay menos posibilidades de que esto ocurra.
* Imprima más lentamente, reduciendo la [Altura de la capa](../resolution/layer_height.md), el [Ancho de línea](../resolution/line_width.md) o las [velocidades](../speed/speed_print.md). Esto reduce la fuerza que el alimentador tiene que poner en el filamento, reduciendo la posibilidad de erosión.