Posición Z del extrusor
====
Si el [prime blob](../platform_adhesion/prime_blob_enable.md) está activado, este ajuste indica la coordenada Z en la que comienza el movimiento del prime blob. Cura se desplazará a esa posición antes de que se ejecute la nota principal.

A diferencia de las coordenadas X e Y, este es un ajuste de la máquina. Esto se debe a que se supone que el acto de cebado tiene una coordenada Z fija. Para crear una mancha de imprimación, la boquilla tendrá que moverse hacia la placa de construcción y quizás moverse un poco hacia arriba y hacia abajo. Las coordenadas [X](../platform_adhesion/extruder_prime_pos_x.md) e [Y](../platform_adhesion/extruder_prime_pos_y.md) pueden elegirse con la configuración normal para mover la posición de la mancha de imprimación en caso de que el espacio en la placa de construcción sea limitante, pero la coordenada Z no.

Lo único que cambia es la coordenada Z a la que Cura ordenará que se mueva la boquilla antes de que se ejecute el comando de prime blob.

**Dado que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**