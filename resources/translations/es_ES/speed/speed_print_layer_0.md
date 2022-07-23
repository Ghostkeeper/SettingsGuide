Velocidad de impresión de la capa inicial
====
Esta configuración ajusta la velocidad a la que se imprime la capa inferior del modelo.

Ajustando esta configuración se ajustará la velocidad de los movimientos de extrusión en la primera capa, pero no los movimientos de desplazamiento. Para ello, ajuste la configuración [Velocidad de desplazamiento de la capa inicial](speed_travel_layer_0.md). Aunque las paredes, la piel y el soporte pueden imprimirse normalmente a diferentes velocidades, no pueden hacerlo para la capa inicial. Todas se imprimirán a la velocidad de este ajuste. Por defecto, este ajuste influye en el ajuste [Velocidad de falda/borde](skirt_brim_speed.md), pero puede ajustarse por separado. La [velocidad de la capa base de la balsa](../platform_adhesion/raft_base_speed.md) no se ve afectada.

La reducción de la velocidad de impresión de la capa inicial mejorará la adhesión entre el modelo y la placa de construcción. Esto se debe a que el material se mantiene caliente durante más tiempo y puede fluir durante más tiempo. Esto reduce las tensiones internas en el material y aumenta el área de contacto, lo que aumenta la adhesión.