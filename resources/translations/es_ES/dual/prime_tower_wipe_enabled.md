Limpiar la boquilla inactiva de la torre de purga
====
Si esta opción está activada, la impresora limpiará la boquilla anterior después de cebar la siguiente en la torre de purga.

El orden de los eventos será el siguiente si esto está activado:
1. La impresora cambia al nuevo extrusor.
2. El nuevo extrusor se ceba imprimiendo una torre de purga.
3. La boquilla que estaba activa antes del cambio de extrusor se limpia en la torre de purga.
4. La impresora continúa imprimiendo la pieza con el nuevo extrusor.

Tenga en cuenta que esto hace que la impresora limpie la boquilla que estaba activa antes del cambio de extrusor, no la boquilla actualmente activa. Si tu impresora tiene múltiples boquillas con una cierta distancia entre ellas, puede que veas un movimiento de desplazamiento en la vista de capas que parece inútil. Esto se debe a que el movimiento a esa ubicación hace que la boquilla anterior se mueva sobre la torre de purga (que no aparece en la vista de capas).

Después de que una boquilla se ponga en espera, seguirá estando bastante caliente durante un tiempo. Mientras está caliente, algo de material tiende a rezumar. Mientras se ceba la siguiente boquilla en la torre de cebado, habrá tenido la oportunidad de enfriarse un poco, por lo que el rezumado ha disminuido. Este ajuste hace que el rezumado se limpie en el centro de la torre de purga, para que no acabe en el lateral de tu modelo impreso.