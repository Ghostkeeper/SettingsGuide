Velocidad mínima de alimentación
====
El firmware de Marlin para impresoras 3D, del que deriva la mayoría del firmware de las impresoras, tiene una velocidad mínima para todos sus movimientos. Este ajuste indica cuál es esa velocidad mínima para el firmware de tu impresora.

La velocidad mínima es un ajuste para evitar errores en el firmware debido a las divisiones por cero. El firmware necesita calcular los intervalos de tiempo entre pasos para enviar una señal a los motores con la sincronización correcta. Si el motor necesita moverse con una velocidad de 0 (es decir, estar parado) esto sería un intervalo de tiempo infinito, que el firmware no puede manejar bien. Esto sólo se aplica si ninguno de los motores de la impresora gira realmente. Por ejemplo, cuando se mueve en la dirección X el motor que controla el eje Y todavía no gira, pero debido a las complejidades de los motores paso a paso el avance mínimo no se aplica aquí.

Cura utiliza este avance mínimo para producir estimaciones de tiempo correctas. Se aplica cuando se acelera al principio de la impresión o después de una pausa, y cuando se desacelera hasta detenerse al final de una impresión o antes de una pausa.

**Dado que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**