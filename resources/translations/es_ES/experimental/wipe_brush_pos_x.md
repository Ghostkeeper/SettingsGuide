Posición X del Cepillo de limpieza
====
Este ajuste configura hacia dónde se mueve la boquilla cuando se limpia.

El procedimiento de limpieza sólo admite la limpieza en la dirección X. Esto significa que el cepillo de limpieza debe abarcar todo el eje Y. El barrido se hará directamente a la izquierda o a la derecha desde el punto en el que la boquilla termina en la capa. El movimiento de barrido en sí mismo también se hará únicamente en la dirección X.

El cepillo de limpieza puede estar en la dirección X negativa o en la dirección X positiva. Si se utiliza la dirección X positiva, lo más probable es que necesite que la boquilla se mueva un poco más allá del borde del volumen de construcción. Si el pincel está en la dirección X negativa, lo más probable es que esta coordenada tenga que ser negativa.

La boquilla nunca se moverá más allá de este punto para el procedimiento de barrido. El barrido se realiza desde este punto hacia el modelo. No se limpiará más allá de este punto.

Esta coordenada está en el sistema de coordenadas de g-code, que es diferente de las coordenadas que Cura muestra en la herramienta de movimiento para la colocación de objetos.