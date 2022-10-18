Velocidad regular del ventilador en altura
====
La velocidad del ventilador comenzará con el valor del ajuste [Velocidad inicial del ventilador](cool_fan_speed_0.md) al principio de la impresión. Durante las primeras capas de la impresión hasta que haya alcanzado la altura especificada en este ajuste, la velocidad del ventilador se incrementará gradualmente hasta la [Velocidad regular del ventilador](cool_fan_speed_min.md).

![Qué velocidad del ventilador se utiliza donde](../images/cool_fan_speed.svg)

Normalmente, la velocidad del ventilador inicial se reduce considerablemente porque la capa inicial debe permanecer caliente durante la impresión. Si la capa inicial se enfría, el material comenzará a [deformarse](../troubleshooting/warping.md). Esto arranca la primera capa de la placa de impresión, lo que hace que la impresión falle. Sin embargo, si la segunda capa se enfría demasiado rápido, todavía se encogerá y a través de la fricción tirará de la primera capa hacia arriba, deformando la impresión también. El propósito de este ajuste es permitir la impresión de múltiples capas con una velocidad de ventilador más baja. De esta manera, se puede evitar el alabeo hasta que la impresión tenga la suficiente rigidez para resistir el alabeo.

La simple reducción de la velocidad del ventilador durante las primeras capas crearía un cambio brusco en la velocidad del ventilador que sería visible en la calidad de la superficie de la impresión final. Esto crea bandas. En su lugar, la velocidad del ventilador se cambia gradualmente hacia la velocidad regular del ventilador.

* Aumentar este ajuste puede mejorar la [adherencia de la cama](../troubleshooting/bed_adhesion_problems.md).
* Si la placa de impresión se calienta a una temperatura alta, es posible que tenga que reducir este ajuste con el fin de evitar la [pata de elefante](../troubleshooting/elephants_foot.md) o la exudación.