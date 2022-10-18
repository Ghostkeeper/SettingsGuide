Velocidad de la capa inicial
====
Esta configuración ajusta la velocidad a la que se imprime la capa inicial del modelo.

Toda la capa inicial se imprimirá normalmente con esta velocidad, aunque las paredes, la piel y el soporte puedan imprimirse normalmente a velocidades distintas. No es el caso de la capa inicial. Para la capa inicial, la [velocidad de impresión](speed_print_layer_0.md) se puede ajustar por separado de la [velocidad de desplazamiento](speed_travel_layer_0.md). También se puede ajustar la velocidad de impresión del [borde y falda](skirt_brim_speed.md). Por defecto, este ajuste afecta a todas ellas. Sin embargo, la [velocidad de la capa base de la balsa](../platform_adhesion/raft_base_speed.md) no se ve afectada.

La reducción de la velocidad de la capa inicial mejorará la adherencia entre el modelo y la placa de construcción. Esto se debe a que el material se mantiene caliente durante más tiempo y puede fluir durante más tiempo. Esto reduce las tensiones internas en el material y aumenta el área de contacto, lo que aumenta la adhesión.