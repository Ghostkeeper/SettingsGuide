Capa Inicio X
====
Si hay varias piezas para imprimir en una capa, Cura optimizará el orden de impresión de estas piezas. Para permitir que la pieza se enfríe antes de imprimir la siguiente capa, imprimirá cada capa aproximadamente en el mismo orden. Los ajustes Layer Start X y [Layer Start Y](layer_start_y.md) determinan qué parte se imprimirá primero: La parte que está más cerca de las coordenadas especificadas. Este ajuste determina la coordenada X de la misma.

Este es un ajuste diferente al de la costura Z. La configuración de la alineación de la costura Z sólo determina dónde la impresora comenzará a imprimir el contorno de una parte, mientras que esta configuración determina con qué parte comenzará.

Si tu impresora hace algo específico cuando comienza con una nueva capa o cuando cambia de extrusor, es una buena idea establecer estas coordenadas en la ubicación donde el cabezal de impresión termina cuando está listo para seguir imprimiendo. Esto minimiza los movimientos de desplazamiento y el rezumado.

Estas coordenadas están en el sistema de coordenadas de g-code, que es diferente del sistema de coordenadas que utiliza Cura para mostrar la ubicación de los objetos.