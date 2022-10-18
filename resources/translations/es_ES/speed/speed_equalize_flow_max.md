Velocidad máxima para la ecualización del flujo
====
Si el ajuste [Igualar flujo de filamento](speed_equalize_flow_enabled.md) está habilitado, entonces la técnica de llenado de huecos pequeños ajustará su velocidad de tal manera que el flujo que sale de la boquilla será igual al de la piel, incluso si las líneas son mucho más delgadas.

Un problema con esto es que las líneas muy finas podrían resultar en velocidades extremadamente altas. Tales velocidades pueden no ser alcanzadas por la impresora, resultando en pasos perdidos y en última instancia en un cambio de capa. Este ajuste pone un máximo a esas velocidades.

Dado que los huecos pequeños tienden a ser pequeños por naturaleza, las líneas dibujadas a estas altas velocidades suelen ser también cortas. Esto significa que, debido a los límites de aceleración, la boquilla no podrá alcanzar las altas velocidades de todos modos. Este ajuste normalmente sólo tiene efecto en las impresiones mecánicas rectas en las que la técnica de llenado de huecos rellena largas rendijas rectas entre dos paredes que son demasiado pequeñas para que la boquilla pueda imprimir.