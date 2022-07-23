Costura
====
Las paredes de su impresión se imprimen como bucles continuos, pero la impresora debe comenzar ese bucle en algún lugar y cerrarlo bien. Si el bucle no se cierra bien, se creará una costura visible. Estas costuras son difíciles de eliminar por completo, pero se pueden hacer algunas cosas para ocultarlas o reducir su tamaño.

Una costura vertical larga en la superficie](../images/seam.jpg)

Esto no debe confundirse con una "costura en Z", que es una costura que se crea mientras la boquilla se mueve a la altura de la siguiente capa. Este movimiento detiene la boquilla por un breve momento, creando allí una [mancha](blobs.md). La terminología de Cura con los ajustes de costura es históricamente errónea en este sentido, ya que sus llamados ajustes de "costura en Z" son realmente sobre dónde colocar la costura normal.

Colocación de la costura
----
Las costuras son difíciles de evitar, pero a menudo es bastante fácil ocultar la costura en un lugar donde no sea tan visible.

La configuración principal para ajustar la colocación de la costura es la [Alineación de la costura Z](../shell/z_seam_type.md). Para ocultar la costura, colóquela dentro de la esquina más aguda. Con el ajuste [Preferencia de la esquina de la costura](../shell/z_seam_corner.md) puede elegir qué tipo de esquina seleccionar. Para ocultar la costura, preferiblemente elegiría "Ocultar costura" u "Ocultación inteligente", que colocan la costura en una esquina interior. Si su modelo no tiene esquinas interiores que ocultar, puede elegir "Exponer costura" para colocar la costura en una esquina exterior afilada, donde también es menos visible que en una superficie plana.

Si la colocación automática no funciona bien, también puede elegir colocar la costura usted mismo eligiendo "Especificado por el usuario". Esto le permitirá introducir las coordenadas [X](../shell/z_seam_x.md) e [Y](../shell/z_seam_y.md) a las que se dirigirá la costura. Elija una ubicación en la que la costura no se vea.

Si todo lo demás falla, también puede extender la costura por toda la superficie seleccionando "Aleatorio". En lugar de una costura continua a lo largo de la pieza, la costura estará en lugares aleatorios a lo largo de la superficie. La superficie quedará un poco picada, pero ya no hay una costura real.

Cerrar la costura
----
La costura también puede hacerse menos visible cerrando con más cuidado la costura cuando se está creando. Estos son algunos ajustes que se pueden realizar para reducir la visibilidad de las costuras.
* Aumente ligeramente la [Distancia de barrido de la pared exterior] (../shell/wall_0_wipe_dist.md). Este ajuste hace que la boquilla continúe su movimiento alrededor del contorno brevemente después de haber completado un bucle. Esto evita que se cree un hueco donde se cierra el contorno. Aumentar este ajuste demasiado, sin embargo, puede causar que se deposite demasiado material alrededor de donde está la costura, haciéndola visible de nuevo.
* Lo contrario es usar [coasting](../experimental/coasting_enable.md). Esto detiene la extrusión de material poco antes de que se cierre el contorno. Esto reduce la presión dentro de la boquilla. La idea aquí es que no haya demasiada sobreextrusión cuando el contorno se complete, lo que reduce la protuberancia de la costura hacia el exterior. En cuanto la boquilla se desplace sobre el inicio del contorno, el plástico colocado anteriormente bloqueará fácilmente cualquier plástico nuevo, ya que la presión en la boquilla no es capaz de superar la contrapresión de la línea de la pared solidificada.
* Imprima la pared exterior más [lentamente](../velocidad/velocidad_pared_0.md). El material podrá fluir mejor hacia fuera para cerrar la costura al final.