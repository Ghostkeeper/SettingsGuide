Impulso de la capa inicial
====
Este ajuste determina la velocidad a la que la boquilla puede pasar por las esquinas mientras se imprime la capa inicial. Se puede configurar por separado del resto de las capas.

Pasar por las esquinas a gran velocidad no sólo hace que el cabezal de impresión vibre horizontalmente. También puede hacer que la placa de impresión vibre verticalmente. Esto afecta negativamente a la adhesión de la cama. Ir a través de las esquinas con un poco más de cuidado durante la primera capa permite una adhesión más consistente de la cama, pero tomará más tiempo para imprimir.

Además, reducir el impulso normalmente hará que la impresora deposite más material en las esquinas afiladas porque la boquilla se ralentiza mientras el flujo de material tiene un cierto retraso en cuando el flujo se reduce. Estas esquinas afiladas son a menudo donde la impresión se suelta primero de la placa de construcción debido a la deformación. Depositar algo de material extra en esas esquinas es ventajoso entonces, ya que hará que las esquinas se adhieran mejor.

Las estructuras individuales de la impresión pueden tener diferentes valores de impulso. Hay ajustes separados para el relleno, la parte inferior, las paredes exteriores e interiores, el soporte y la torre principal. Este ajuste anulará todos ellos. Sólo el ajuste [Skirt/Brim Jerk](jerk_skirt_brim.md) anulará este impulso, ya que la falda y el borde sólo pueden ocurrir en la primera capa.