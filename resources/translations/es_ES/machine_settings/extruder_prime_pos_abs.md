Posición inicial absoluta del extrusor
====
Si se utiliza el procedimiento [prime blob](../platform_adhesion/prime_blob_enable.md), la posición de este prime puede ajustarse con una posición [X](../platform_adhesion/extruder_prime_pos_x.md) y [Y](../platform_adhesion/extruder_prime_pos_y.md). Este ajuste determina si se trata de la posición en la placa de impresión o de una posición relativa a la posición actual de la impresora.

Si este ajuste está activado, las coordenadas X e Y se refieren a una determinada posición fija en la placa de impresión. El extrusor siempre se moverá allí para crear una mancha de primera.

Si este ajuste está desactivado, las coordenadas X e Y son relativas a la posición que tiene la boquilla al cambiar a ese extrusor por primera vez. Para el primer extrusor, esa sería la coordenada [0,0]. Para los otros extrusores, esta sería su posición inicial tal y como se define en el archivo de definición del extrusor. Esta posición inicial también puede ser relativa.

Se recomienda encarecidamente utilizar una posición inicial absoluta. Una posición inicial absoluta está garantizada para estar libre de colisiones con otras partes de la impresión, ya que no puedes colocar objetos en ese lugar de la placa de impresión. Una posición de imprimación relativa puede acabar en cualquier lugar de la placa de impresión y, por lo tanto, puede acabar imprimiendo en algún lugar de la primera capa. El uso de una posición de imprimación relativa podría ahorrar algo de tiempo de viaje, pero esto realmente no vale la pena el riesgo.

**Dado que este es un ajuste de la máquina, este ajuste no es normalmente visible en la lista de ajustes.**