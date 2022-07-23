Tiempo mínimo de capa
====
El Tiempo Mínimo de Capa configura la duración más corta de impresión de una capa que se permite. La impresora no puede imprimir capas más rápido que esto.

Esto es necesario para permitir que la capa anterior se enfríe antes de poner la siguiente capa encima. Esto asegura que la capa anterior se haya solidificado completamente, para evitar que se hunda.

![Qué velocidad del ventilador se utiliza donde](../images/cool_fan_speed.svg)

Este ajuste tiene tres efectos:
* Si una capa se imprime más rápido de lo que indica el ajuste [Umbral regular/máximo de velocidad del ventilador](cool_min_layer_time_fan_speed_max.md), la velocidad del ventilador se incrementará hacia la [Velocidad máxima del ventilador](cool_fan_speed_max.md). Una vez que una capa es tan pequeña que tarda en imprimirse el tiempo mínimo de capa, se utilizará la velocidad máxima del ventilador. La velocidad del ventilador se interpola entre las dos.
* Si la capa tarda menos que el Tiempo Mínimo de Capa en imprimirse, la velocidad de impresión se ralentizará de tal manera que todavía tarda el Tiempo Mínimo de Capa.
* Si el cabezal de impresión se ralentiza demasiado (imprimiendo más despacio que la [Velocidad mínima] (cool_min_speed.md)), el cabezal de impresión esperará al final de la capa y, opcionalmente, levantará un poco el cabezal.

Hay una compensación cuando se ralentiza la boquilla para permitir que la capa se enfríe mejor. El Tiempo Mínimo de Capa tiene como objetivo dar algo de tiempo para que el material se enfríe ralentizando el movimiento del cabezal de impresión. Durante este tiempo, los ventiladores estarán soplando a máxima potencia para que se enfríe más rápidamente, pero la boquilla caliente también está todavía sobre el plástico. En el caso de piezas muy pequeñas, la boquilla caliente puede transferir más calor a la impresión de lo que los ventiladores pueden soplar. Esto hace que el plástico se derrita aún más que si no tuviera un tiempo mínimo de capa.

Cuando se imprimen materiales relativamente fríos o si los ventiladores del cabezal de impresión son particularmente potentes, el material tolerará un mayor Tiempo Mínimo de Capa para reducir el hundimiento. Si el Tiempo Mínimo de Capa se ajusta demasiado alto, la boquilla se ralentizará cada vez más, lo que provoca manchas y hundimiento en algunos lugares también.