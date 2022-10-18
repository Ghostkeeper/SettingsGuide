Sobreextrusión
====
La sobreextrusión es un término utilizado cuando la impresora extruye demasiado material en un lugar. Esto hace que el material fluya hacia los lados o hacia arriba, lo que hace que la superficie sea muy áspera e irregular. También puede causar [hilos](stringing.md) y muchos [granos](blobs.md).

Se ha producido una sobreextrusión masiva en esta impresión](../images/overextrusion.jpg)

Control de la temperatura
----
La causa más común de la sobreextrusión es la impresión demasiado caliente. Si la [temperatura de impresión](../material/material_print_temperature.md) está ajustada demasiado alta, el material tendrá una menor viscosidad, haciendo que fluya fuera de la boquilla sin control. Normalmente el resultado es la sobreextrusión en algunas áreas como las paredes exteriores, pero la subextrusión en otras como el relleno.

Para remediarlo, hay que reducir la temperatura gradualmente. Mira cuidadosamente la hoja de especificaciones del material con el que estás imprimiendo para ver qué rango de temperatura es aceptable y reduce tu temperatura de impresión hacia el extremo inferior de ese rango.

Diámetro del filamento
----
Hay varios estándares para los diámetros de filamento. Los más comunes son 1,75 mm y 2,85 mm, pero también existe el de 3,00 mm. Aparte de eso, no todos los fabricantes producen su filamento con un diámetro consistente. Si tu filamento es más ancho de lo que espera Cura, extruirás demasiado material, ya que Cura indica a la impresora que extruya una determinada longitud de filamento que tendrá entonces demasiado volumen.

Para solucionarlo, mide primero el diámetro real del filamento con unos calibradores. Es mejor medirlo en varios puntos, por si varía, y en varios ángulos alrededor de la circunferencia. Tome la media de estas mediciones. Este promedio se puede rellenar en Cura en la página de Gestión de Materiales, como una propiedad del material. Si el diámetro no se puede editar porque es un material incorporado, es posible que tenga que duplicar el material primero. Entonces debería permitirle editar el diámetro.

Calibración del extrusor
----
A veces el problema radica en que el hardware no coincide con las expectativas del firmware. Si el motor del extrusor es un motor paso a paso (que es común en las impresoras 3D) entonces el firmware necesita saber cuántos pasos del motor resultarán en una determinada distancia a mover. El firmware tiene un ajuste para esto, midiendo la precisión del alimentador en pasos por milímetro. Si este ajuste está mal configurado, el cargador puede moverse demasiado rápido o demasiado lento. Es mejor ajustar esto en el firmware si se puede. Sin embargo, si eso es imposible, el [caudal](../material/material_flow.md) en Cura se puede ajustar para compensar. También debe compensar todas las [distancias de retracción](../travel/retraction_amount.md) y [velocidades](../travel/retraction_speed.md) entonces.

<!--if cura_version<5.0:
Paredes superpuestas
----
Normalmente, Cura se limitaría a dibujar los contornos de la huella con un determinado ancho de línea. Si las paredes se acercan en ciertos lugares de su impresión, esto llevaría a líneas superpuestas. Estas líneas se vuelven gruesas y producen manchas porque puede poner allí hasta el doble de material del necesario. Cuando hay mucho solapamiento, la segunda línea se verá impedida de extruir, por lo que la presión dentro de la cámara de la boquilla aumenta hasta que se expulsa y produce una mancha.

Esto puede evitarse activando la [compensación de paredes superpuestas](../shell/travel_compensate_overlapping_walls_enabled.md). La extrusión de la segunda línea se reducirá de forma que extruya sólo el material necesario para rellenar el espacio restante de la pared, lo que evita la sobreextrusión.

Si las paredes se superponen debido al [Inset de la pared exterior](../shell/wall_0_inset.md), puede intentar reducir ese inset para evitar la sobreextrusión. También puede intentar imprimir la [pared exterior primero](../shell/outer_inset_first.md). El exceso de material será empujado hacia el interior del modelo, donde es invisible.

Ajustando directamente el caudal
----
Si no se sabe qué es lo que está causando este exceso de extrusión, también puede ajustar directamente la [tasa de flujo](../material/material_flow.md). Reduzca el caudal hasta que su superficie vuelva a ser lisa. Esto puede compensar algún factor desconocido directamente.