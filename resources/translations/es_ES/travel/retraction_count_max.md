Recuento máximo de retracciones
====
La rueda del alimentador necesita agarrarse al filamento para poder moverlo correctamente. La retracción del material a menudo tiende a hacer que la rueda del alimentador desgaste el filamento hasta el punto de no poder agarrarlo correctamente. Este ajuste limita el número de retracciones dentro de una determinada longitud de filamento para evitar este desgaste.

El ajuste indica la frecuencia con la que se permite retraer el filamento durante la longitud de filamento indicada por el ajuste [Ventana de distancia mínima de extrusión](retraction_extrusion_window.md). Cualquier otra retracción durante esta ventana no se retraerá, sino que se desplazará sin retraerse.

Visualización de las retracciones durante una determinada longitud de filamento](../images/retraction_count_max.svg)

La longitud del filamento durante la cual se limita el número de retracciones es una ventana deslizante. Por ejemplo, con una longitud de ventana de 3mm y un recuento máximo de retracciones de 10, esto significa que se permite una nueva retracción tan pronto como la décima retracción anterior se haya realizado más allá de 3mm en el filamento.

Si se reduce el número máximo de retracciones, se reducirá el desgaste del filamento. Esto es útil para materiales más blandos, como el PVA. Sin embargo, también aumentará el encordado, porque ya no se retraerá en una posición en la que aparentemente se deseaba.