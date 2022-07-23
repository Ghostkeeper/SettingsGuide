Secuencia de impresión
====
Cuando se colocan varios modelos en la placa de impresión, esto determina el orden en que se imprimen las capas de estos objetos. Hay dos opciones.

Todas a la vez
----
Todos los objetos se imprimirán al mismo tiempo, lo que significa que las capas se imprimirán de abajo a arriba para todos los objetos al mismo tiempo. Se imprimirá una capa de cada objeto antes de pasar a la siguiente.

Esto tiene dos grandes ventajas:
* La capa anterior tiene más tiempo para enfriarse, lo que permite una mejor calidad en la impresión de objetos pequeños.
* Se puede utilizar todo el volumen de construcción para su impresión.

De uno en uno
----
Los objetos se imprimirán uno a uno, lo que significa que imprimirá todas las capas de un objeto y luego volverá a bajar a la placa de construcción para imprimir el siguiente objeto.

Las principales ventajas de este modo son:
* Si la impresión falla por cualquier razón, todos los objetos que fueron completados antes de la falla están completamente bien para ser usados.
* Se requieren menos movimientos de desplazamiento para ir y venir entre los modelos. Esto ahorra algo de tiempo de impresión y reduce el número de cicatrices en la superficie donde la boquilla salió y entró en el objeto.

Sin embargo, este modo viene con algunas restricciones para evitar que el cabezal y el pórtico colisionen con el modelo.
* No puede imprimir ningún objeto más alto que la altura del pórtico de su impresora. La altura del pórtico puede ajustarse en el cuadro de diálogo Configuración de la máquina de la impresora. Esta altura del pórtico indica la distancia vertical que hay entre la punta de la boquilla y el sistema que lleva el cabezal de impresión. La razón de esta limitación es que el cabezal de impresión tendrá que bajar hasta la placa de construcción para imprimir el segundo objeto. Esto significa que el primer objeto puede ser golpeado por el pórtico mientras se imprime el segundo objeto. En teoría se puede permitir que el último objeto impreso esté más alto que el pórtico, pero por simplicidad Cura no lo permitirá de todos modos.
* Los objetos deben estar más alejados unos de otros, para evitar que el cabezal de impresión golpee los modelos impresos anteriormente en el lateral.
* El orden de impresión de los objetos está fijado y optimizado para permitir que los objetos se impriman más juntos. Si su cabezal de impresión no es simétrico, esto puede ahorrar mucho espacio en la placa de impresión.

**Uno a la vez sólo está disponible en una sola extrusión. Si utilizas una impresora de extrusión múltiple, debes desactivar todos los extrusores menos uno para que aparezca este ajuste.**