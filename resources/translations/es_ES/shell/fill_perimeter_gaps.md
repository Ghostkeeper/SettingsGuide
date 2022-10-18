Rellenar huecos entre paredes
====
Muchas impresiones contienen piezas más finas que el grosor de pared deseado. En la mayoría de los casos esto está bien, pero para algunas impresiones esto dejaría un hueco entre las paredes. Si esta opción está activada, los huecos entre las paredes se rellenarán con un punto de material extra.

![Se muestra un hueco largo y delgado entre las paredes opuestas en la parte izquierda y derecha de la imagen](../images/fill_perimeter_gaps_disabled.png)
![Los huecos entre paredes se rellenan con material](../images/fill_perimeter_gaps_enabled.png)

Hay dos casos comunes en los que el relleno de huecos es útil:
* Entre dos paredes opuestas en impresiones que son delgadas (como se muestra en las imágenes de arriba). Rellenar estos huecos aumenta la resistencia de la pieza en esos lugares, porque las dos paredes opuestas ya no pueden moverse por separado la una de la otra.
* En las esquinas muy agudas, habrá un hueco dentro de la pared exterior donde la pared interior es demasiado gruesa para llegar a la esquina. Rellenar estos huecos aumenta la resistencia, pero también hace que la pared exterior parezca más consistente.

**Es aconsejable tener mucho cuidado para ver qué movimientos de desplazamiento son necesarios si esto está habilitado. El relleno de los huecos se hace después de que las paredes hayan terminado de imprimirse.**