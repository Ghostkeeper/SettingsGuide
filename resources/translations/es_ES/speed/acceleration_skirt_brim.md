Aceleración de la falda/del borde
====
Este ajuste controla la velocidad con la que la boquilla acelera en diferentes direcciones mientras se imprime el faldón o el borde. La aceleración durante el faldón o el borde puede establecerse a una velocidad diferente a la del resto de la impresión. Aunque el faldón y el borde son siempre exclusivos de la capa inicial, este ajuste anula el ajuste [Aceleración de impresión de la capa inicial](acceleration_print_layer_0.md). Se imprimen utilizando la aceleración determinada con este ajuste, no el ajuste de la capa inicial en general.

El borde es crucial para la adhesión de la cama, por lo que la reducción de las tasas de aceleración durante la impresión del borde puede reducir las vibraciones mientras se imprime el borde y luego hacer que la adhesión del borde a la placa de construcción sea mejor, aumentando la eficacia del borde a un costo menor de tiempo de impresión.

Sin embargo, el efecto de la aceleración en el borde y el faldón suele ser extremadamente pequeño, ya que estos consisten en líneas con curvas suaves. La aceleración suele ser asumida por completo por el ajuste [Impulso en falda/borde](jerk_skirt_brim.md).