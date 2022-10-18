Ventana de distancia mínima de extrusión
====
La rueda del alimentador necesita agarrarse al filamento para poder moverlo correctamente. La retracción del material a menudo tiende a hacer que la rueda de alimentación desgaste el filamento hasta el punto de que ya no puede agarrar el filamento correctamente. Este ajuste limita el número de retracciones dentro de una determinada longitud de filamento para evitar este desgaste.

Las retracciones están limitadas por la combinación de [Recuento máximo de retracciones](retraction_count_max.md) y este ajuste. No se permite que el material se retraiga más que el valor del Recuento Máximo de Retracción dentro de una longitud de filamento indicada por este ajuste de la Ventana de Distancia Mínima de Extrusión.

Una determinada longitud de filamento a lo largo de la cual se limita el número de retracciones](../images/retraction_count_max.svg)

La longitud del filamento durante la cual se limita el número de retracciones es una ventana deslizante. Por ejemplo, con una longitud de ventana de 3mm y un recuento máximo de retracciones de 10, esto significa que se permite una nueva retracción tan pronto como la décima retracción anterior se haya realizado más allá de 3mm en el filamento.

Aumentar la longitud de la ventana de extrusión reduce efectivamente el número de retracciones. Esto hace que la impresión sea más fiable, pero aumenta la cantidad de hilos y manchas en la superficie. Esto es especialmente útil para materiales más blandos que son más sensibles a la molienda.