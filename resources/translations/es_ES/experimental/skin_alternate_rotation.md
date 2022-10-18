Rotación alternativa de la piel
====
Cuando la parte superior e inferior se imprimen con las líneas o el [patrón] en zigzag (../top_bottom/top_bottom_pattern.md), las líneas se orientan normalmente en las direcciones diagonales, alternando las dos direcciones cada vez. Si se activa este ajuste, se alternarán en su lugar cuatro direcciones: dos direcciones diagonales, la vertical y la horizontal.

![Alternar cuatro direcciones](../images/skin_alternate_rotation.gif)

Esta configuración anula la configuración de [Direcciones de la línea superior/inferior](../top_bottom/skin_angles.md). Sin embargo, el comportamiento es el mismo. De hecho, este ajuste puede ser emulado completamente introduciendo los ángulos `[45, 135, 0, 90]`.

Generalmente, su impresión será la más rígida en la dirección longitudinal a la dirección de las líneas. Si este ajuste no está activado, será en las dos direcciones diagonales, haciéndola más débil en las direcciones ortográficas. Estas direcciones diagonales se eligen porque los mecanismos de pórtico más comunes para las impresoras 3D utilizan más motores para el movimiento diagonal, lo que les permite acelerar más rápido en esas direcciones.

Si se activa este ajuste, las direcciones de las líneas se reparten de forma más uniforme. Esto hace que la fuerza del objeto se distribuya de manera más uniforme. Esto hace que el objeto sea más fuerte en las direcciones verticales y horizontales, pero ligeramente más débil en las direcciones diagonales. También tardará un poco más en imprimir el objeto.