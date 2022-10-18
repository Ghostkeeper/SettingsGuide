Contornos espiralizados suaves
====
Si [Espiralizar el contorno exterior](magic_spiralize.md) está activado, este ajuste activa o desactiva la característica más distintiva del modo Spiralize: En lugar de imprimir cada capa una tras otra a intervalos de altura, la altura se incrementa gradualmente a lo largo de la capa.

Dado que el modo espiralizado hace que sólo se impriman las paredes de la mayoría de las capas con un único contorno, este único contorno adoptará la forma de una espiral, lo que da nombre a la función espiralización. Las primeras y últimas capas de la impresión ven reducido su caudal gradualmente para evitar la sobreextrusión y conseguir la altura correcta.

Debido a que la boquilla se mueve gradualmente hasta la altura de la siguiente capa a través de la capa, ya no habrá ninguna costura donde la boquilla se mueve a la siguiente capa. Efectivamente, esto elimina la costura Z.

Por otro lado, la capa se mueve hacia arriba o hacia abajo en media altura de capa. Esto es menos preciso. Puede tener un efecto borroso en los detalles finos de la impresión.

Este ajuste no es eficaz para eliminar las costuras si hay más de un contorno para imprimir en una capa. Todavía tendrá que detener la extrusión después del contorno para pasar a la siguiente pieza impresa. Esto deja una costura de todos modos.

**Este efecto no es visible en la vista de capas debido a las limitaciones de renderizado.**