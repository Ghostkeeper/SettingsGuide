Velocidad del arrastre
====
Durante el arrastre, la boquilla ya no extruye. Sin embargo, no se comporta como un movimiento de desplazamiento. La boquilla sigue desplazándose aproximadamente a la misma velocidad. Con este ajuste, se puede configurar la velocidad exacta a la que la boquilla sigue desplazándose.

La velocidad del arrastre se configura en función de la velocidad de impresión normal. Esto significa que si la [pared exterior](../velocidad/pared_0.md) y la [pared interior](../velocidad/pared_x.md) tienen velocidades diferentes, también se desplazarán por inercia a velocidades diferentes. Normalmente el arrastre se realiza a una velocidad ligeramente inferior a la velocidad normal de impresión, para combatir la subextrusión.

La reducción de la velocidad de arrastre reduce el efecto de subextrusión que el arrastre provoca de forma natural durante la pared, pero aumenta el efecto de subextrusión después de que la boquilla haya pasado a imprimir la siguiente estructura porque la boquilla ha estado rezumando durante más tiempo. La reducción de la velocidad es mejor si se combina con un [volumen] reducido (coasting_volume.md) para el coasting, para que la boquilla no permanezca rezumando durante demasiado tiempo.

Al reducir la velocidad también se reduce el efecto de la inercia en general, ya que la boquilla estará descansando en la costura durante más tiempo también. Esto hace que la costura sea más visible.