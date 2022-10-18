Underextrusión
====
Uno de los problemas más comunes en la impresión 3D es que la impresora no extruye suficiente material para producir un objeto bonito y sólido. Cuando esto ocurre, se habla de "subextrusión": La boquilla extruye menos material del previsto.

Un caso extremo de subextrusión, en el que incluso se puede ver el interior del objeto](../images/underextrusion.jpg)

La subextrusión también puede manifestarse de muchas maneras. En el caso más extremo, el objeto es muy frágil y se puede ver el interior a través de la superficie. A veces es visible porque el ancho de las líneas es demasiado pequeño, de modo que no se conectan con las líneas adyacentes. A veces sólo se manifiesta como pequeños agujeros en la superficie superior o pequeñas fracturas en las paredes.

Las causas de la subextrusión son innumerables, por lo que es muy difícil solucionar el problema. El resto de este artículo describe algunas de las causas más probables y cómo remediarlas.

Boquilla obstruida
----
Si tu impresora estaba imprimiendo bien, y de repente muestra una subextrusión sin ningún cambio significativo en el objeto impreso o en los ajustes, es probable que el problema esté en alguna parte del tren de extrusión. Normalmente el eslabón más débil es la boquilla.

Las boquillas obstruidas son algo habitual en cualquier impresora 3D. Esto puede ocurrir cuando el filamento se contamina con cosas que no se funden bien y se introduce en la boquilla. También puede ocurrir cuando el propio filamento se quema en la boquilla. Esto puede ocurrir cuando el plástico se calienta demasiado o se mantiene a una temperatura alta durante demasiado tiempo. El material se degradará, los polímeros se cristalizarán y te quedarás con un trozo de plástico duro que no se fundirá fuera de la boquilla. Para remediarlo, hay que sacar los restos de la boquilla.

Hay varias técnicas para sacar los restos de la boquilla. Si tienes una aguja de acupuntura o algún otro alfiler metálico fino, puedes empujarlo desde el fondo. Sin embargo, la técnica más común es la conocida como "tirón atómico". Para ejecutar esta técnica, coge un trozo de filamento de al menos 50 cm de largo, preferiblemente de algún material con un punto de fusión alto. Calienta la boquilla hasta el punto de fusión de ese filamento (por ejemplo, 190°C para el PLA), luego empuja el filamento con unas pinzas hasta que salga algo de material por la boquilla. A continuación, deja que la boquilla se enfríe hacia su temperatura de transición vítrea (por ejemplo, 60°C para el PLA), mientras empujas el filamento hacia abajo en la boquilla. Justo antes de que se alcance la temperatura de transición vítrea, saca el filamento rápidamente. Si la punta del filamento está sucia de plástico ennegrecido, corta la punta y vuelve a intentarlo hasta que esté limpia. Intenta imprimir algo de nuevo y espero que ahora extruya mejor.

Deslizamiento del alimentador
----
A veces el alimentador no agarra lo suficiente el filamento para empujarlo con fuerza a través de la boquilla. Durante la impresión, se puede escuchar el filamento resbalar periódicamente entonces, con un suave clack cada pocos segundos. Esto es el alimentador tratando de empujar el filamento hacia adentro, pero el filamento se desliza de nuevo de vez en cuando.

La mayoría de los alimentadores tienen puntos de ajuste para regular la fuerza que ejercen sobre el filamento. Intenta ajustar el alimentador con un poco más de fuerza sobre el filamento. Si el alimentador está presionando demasiado contra el filamento, podría romper el filamento o causar demasiada fricción y empezar a moler. Si está demasiado suelto, a menudo verás algo de subextrusión.

Diámetro de filamento inconsistente
----
Aunque la mayoría de los filamentos están bien, a veces se produce un lote en el que el filamento es demasiado fino. Esto puede tener grandes consecuencias en la cantidad de extrusión en su impresión. Los filamentos más baratos suelen ser más propensos a mostrar este problema. Puedes utilizar calibradores para medir el diámetro real de tu filamento. Asegúrate de medir en varios puntos diferentes a lo largo del filamento, y no midas donde el alimentador ha molido el filamento.

Si el diámetro del filamento está demasiado lejos (una diferencia de 50μm comienza a verse en la impresión), entonces puedes ajustar el diámetro de tu filamento en el gestor de material. Si estás utilizando un material incorporado de Cura, tendrás que duplicar ese material antes de editarlo. Cura compensará entonces el nuevo diámetro ajustando la velocidad del alimentador.

Fusión de materiales
----
Aparte de que tu impresora 3D esté en plena forma, los ajustes con los que imprimes también tienen que coincidir con las propiedades del material que estás utilizando. La más importante es la temperatura de impresión.

Si la [temperatura de impresión](../material/material_print_temperature.md) es demasiado baja, verá la subextrusión muy rápidamente. Si el material está demasiado frío, será muy viscoso, haciendo más difícil que fluya correctamente fuera de la boquilla. Cuando se combina con una alta velocidad de impresión, el material no tiene tiempo para fundirse correctamente y tampoco tiene tiempo para fluir en su posición. Algunos materiales, como el PVA o el Nylon, son propensos a absorber la humedad del aire. Esta humedad se evapora cuando el material se imprime, lo que enfría el plástico. Para compensar ese efecto, esos materiales deben imprimirse a una temperatura más alta si han estado expuestos al aire durante un tiempo.

Si la temperatura es demasiado alta, el material puede degradarse muy rápidamente. El filamento degradado también puede no fundirse correctamente, lo que obstruirá la boquilla. El calor añadido también puede hacer que el material se funda más arriba en el tren de extrusión. Esto puede causar fricción en el tren de extrusión, lo que dificulta la salida del material. Mira cuidadosamente las especificaciones de temperatura en la etiqueta de tu filamento para ver a qué rango de temperatura se puede imprimir.

En lugar de ajustar la temperatura, también puede optar por ajustar la [velocidad del ventilador] (../cooling/cool_fan_speed.md). Si el ventilador está ajustado demasiado alto, la boquilla puede enfriarse más rápido mientras se extruye el material, haciendo que esté más frío de lo que el sensor de temperatura está midiendo realmente. Especialmente para los materiales que se imprimen naturalmente a una temperatura alta, como el policarbonato, la reducción de la velocidad del ventilador es a menudo necesaria para evitar la subextrusión.

Si se imprime demasiado rápido también se producirá una subextrusión, ya que el material no tiene tiempo de fundirse dentro de la cámara de boquillas. Reducir la [velocidad de impresión] (../speed/speed_print.md) también puede ayudar a combatir la subextrusión.

Conseguir que el material fluya
----
Siempre hay una cierta latencia entre el momento en que la impresora alimenta el material hacia adelante y cuando realmente comienza la extrusión. Esta latencia puede causar subextrusión si no se tiene en cuenta. Cuando la impresora empuja el material hacia delante, la presión en la cámara de la boquilla aumentará gradualmente hasta que sea suficiente para empujar el material fundido hacia fuera en el otro extremo. El material puede tardar hasta un segundo en alcanzar su caudal normal. Si la impresora tiene un tubo Bowden entre el alimentador y la boquilla, este retardo puede ser incluso mucho mayor, del orden de 10 segundos.

Cuando la impresora necesita empezar a extruir más material que antes, alimentará el material más rápido, pero tardará un poco en llegar a la punta de la boquilla. Mientras tanto, la boquilla tratará de dibujar una línea, pero esta línea será sub-extruida. Especialmente cuando la impresión es muy detallada, esto puede causar una considerable subextrusión.

Hay dos ajustes que puede hacer para solucionar esto: El cebado y los ajustes de velocidad.

El cebado del material consiste en expulsar un poco de material antes de que comience la parte importante de la impresión. A menudo esto se hace al principio de la impresión en una rutina separada, imprimiendo una pequeña línea o gota de plástico en una esquina de la placa de impresión. Alternativamente, se puede utilizar un [faldón o un borde] (../platform_adhesion/adhesion_type.md), que imprimirá una serie de líneas alrededor de la propia impresión. Cuando el material está fluyendo correctamente y todo el aire está fuera de la cámara de la boquilla, extruirá de forma más consistente.

Cuando el material se retrae, el flujo de material se interrumpe. Cuando el material es empujado de nuevo a la boquilla, puede tomar un tiempo para que vuelva a fluir. Reduciendo la [velocidad a la que empuja hacia atrás](../travel/retraction_prime_speed.md) permite que el material se funda mejor antes de ser extruido, lo que ayuda un poco. Si no, también puedes intentar empujar el material un poco más lejos que antes de la retracción, [cebando un poco más](../travel/retraction_extra_prime_amount.md) para compensar la subextrusión. Sin embargo, el ajuste es muy delicado.

Igualar las velocidades
----
Si usted está viendo la subextrusión sólo en ciertas estructuras de la impresión, como el relleno y el apoyo, mira a igualar la velocidad de flujo en su impresión más. Siempre hay un retraso entre el alimentador que alimenta el material y este material realmente fluye fuera de la boquilla. Si la velocidad de impresión se incrementa para alguna parte de la impresión, entonces el cabezal de impresión se acelerará relativamente rápido, pero el flujo de material se retrasará hasta que la presión en la cámara de la boquilla se incremente para hacer frente a la mayor tasa de extrusión. Esto provoca también una subextrusión. Del mismo modo, cuando se reduce la velocidad de extrusión, siempre hay algo de sobreextrusión.

Algunos programas son capaces de compensar este efecto. Marlin tiene una función llamada [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) en la que empieza a aumentar la presión dentro de la cámara de la boquilla con antelación para que pueda salir antes de la boquilla. Sailfish tiene una [característica similar](https://www.sailfishfirmware.com/doc/tuning-jkn-advance.html) que llaman JKN Advance. Para ajustar los parámetros de estas características, mira qué g-code necesitas escribir en el g-code de inicio.

Si estas características no están disponibles o no son efectivas, tendrás que asegurarte de que no hay grandes y repentinos cambios de flujo en la impresión. Reduce el [Espesor de la capa de relleno](../infill/infill_sparse_thickness.md) y el [Espesor de la capa de soporte](../support/support_infill_sparse_thickness.md). Estos ajustes multiplicarán la tasa de extrusión para lograr una mayor altura de la capa.<!--if cura_version>=5.0--> Para imprimir anchos de línea variables con mayor precisión, también considere el uso de [flow equalization](../speed/speed_equalize_flow_width_factor.md) para reducir los cambios de flujo allí.<!--endif-->

Lo más importante es asegurarse de que el relleno, las paredes interiores, la pared exterior, el forro y el soporte se imprimen con una tasa de extrusión similar. La tasa de extrusión de una línea es el producto de su ancho de línea, la altura de la capa, el flujo y la velocidad (media). Multiplique estos cuatro factores y asegúrese de que el resultado es aproximadamente el mismo para el relleno ([altura de capa](../infill/infill_sparse_thicknes.md), [ancho de línea](../resolution/infill_line_width.md), [flujo](.. /material/infill_material_flow.md) y [velocidad](../speed/speed_infill.md)), skin ([line width](../resolution/skin_line_width.md), [flow](../material/skin_material_flow.md) y [velocidad](../speed/speed_topbottom.md), pared exterior ([ancho de línea](.. /resolution/wall_line_width_0.md), [flujo](../material/pared_0_material_flow.md) y [velocidad](../velocidad/velocidad_pared_0.md), pared interior ([ancho de línea](../resolución/ancho_de_línea_de_pared_x.md), [flujo](../material/pared_x_material_flow.md) y [velocidad](. ./speed/speed_wall_x.md)) y soporte ([altura de capa](../support/support_infill_sparse_thickness.md), [ancho de línea](../resolution/support_line_width.md), [flujo](../material/soporte_material_flujo.md) y [velocidad](../speed/speed_support.md)). Si [compensar el solapamiento de las paredes](../shell/travel_compensate_overlapping_walls_enabled.md), asegúrese de activar [ecualización del flujo](../speed/speed_equalize_flow_enabled.md) para que se ajuste la velocidad en lugar del flujo.

Límites de la boquilla
----
Extruir demasiado material a través de una boquilla pequeña también puede causar subextrusión. Cuando se imprime a grandes alturas de capa, anchos de línea o velocidades utilizando una boquilla pequeña, el material físicamente no será capaz de fluir fuera de la boquilla a tiempo. Aumentar la temperatura puede ayudar a que el material sea más fluido hasta cierto punto, pero sigue habiendo límites a lo que una boquilla puede extruir. Más allá de este límite, considere la posibilidad de comprar una boquilla más grande.

Por otro lado, extruir demasiado poco material también puede provocar una subextrusión. Si la presión en la cámara de la boquilla es muy baja, la tensión superficial del plástico líquido puede mantener el material en la cámara de la boquilla. Ocasionalmente será empujado hacia fuera con una gran gota, dejando aire en otros lugares. Esto puede dar un efecto similar a la subextrusión.

Ajustar el flujo directamente
----
Si todo lo demás falla, Cura también tiene una configuración para ajustar el flujo directamente: [Flujo](../material/material_flow.md). Este método provisional puede compensar un fallo desconocido en alguna parte del sistema.

No funcionará si se impide físicamente que el material fluya más rápido (por ejemplo, debido a una boquilla obstruida). En otros casos, es probable que provoque una sobreextrusión en algunos lugares. Sin embargo, es una forma sencilla de ajustar la impresión según sea necesario.