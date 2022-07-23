Encordado
====
Cuando la impresora termina de imprimir una parte de una capa y necesita pasar a otra parte, tiene que detener temporalmente la extrusión. Si el material sigue fluyendo mientras se desplaza, se dibuja una fina cuerda de plástico entre las dos partes. A esto se le llama encordado.

Se ven finas líneas de plástico donde la boquilla se desplazó de una pieza a otra](../images/stringing.jpg)

A menudo los cordones están alineados uno encima del otro, porque la boquilla completa una parte en el mismo lugar en cada capa. Esto crea una red vertical. El plástico sobrante también puede amontonarse en el encordado de las capas anteriores, lo que da lugar a manchas de plástico desordenadas por todas partes.

El encordado se acompaña a veces de una subextrusión. El cortador generalmente asume que no se pierde material durante los movimientos de desplazamiento, por lo que ordena a la impresora que extruya sólo el material suficiente para imprimir su siguiente pieza. Si algo de material rezuma fuera de la boquilla durante un desplazamiento (lo que da lugar a un encordado) ese material no se utilizará en la impresión de la siguiente pieza, dando lugar a una subextrusión en la misma. El encordado no suele ser un problema si se produce dentro del relleno, pero si el encordado es demasiado extremo puede causar un problema incluso allí porque da lugar a una subextrusión posterior.

Causas
----
El encordado se produce porque el material rezuma fuera de la boquilla durante un movimiento de desplazamiento. Aunque la impresora no alimenta nuevo material durante un movimiento de desplazamiento, el flujo de material no se detiene inmediatamente. Durante la impresión, hay algo de presión dentro de la cámara de la boquilla causada por el filamento que acumula un poco de fuerza como un resorte. Cuando la boquilla se mueve a través del aire, esta presión puede liberarse, empujando involuntariamente el material fuera de la boquilla.

Incluso si el material se retrae antes del movimiento de desplazamiento, seguirá habiendo algo de material dentro de la cámara de la boquilla. Esto ocurre porque el material en esa boquilla está fundido. Si se tira de ella desde un lado, el líquido no vuelve a salir. A menos que se haya solidificado, un cordón de material fundido permanece en la boquilla. Durante un movimiento de desplazamiento, este cordón rezumará fuera de la boquilla si es lo suficientemente líquido.

Prevención
----
La retracción es la principal técnica para prevenir el encordado. Si ve que hay encordamiento en sus impresiones, aquí hay algunas cosas que puede probar:
* Asegúrese de que [la retracción está activada en absoluto] (../travel/retraction_enable.md). Esto requiere un poco más de tiempo de impresión, pero reduce en gran medida el encordado.
* Reduce la [temperatura de impresión](../material/material_print_temperature.md). Esto hace que el material sea menos fluido, lo que hace que rezume menos fuera de la boquilla. También permite retracciones más efectivas, ya que más material será sacado de la cámara de la boquilla.
* Si su material es viscoso, el aumento de la [velocidad de retracción] (../travel/retraction_speed.md) generalmente reducirá el encordamiento para movimientos cortos al colocar una subpresión en la cámara de la boquilla. Esta presión reducida mantiene el material aspirado, de modo que no rezuma.
* Para movimientos largos, aumentar la [distancia de retracción] (../travel/retraction_amount.md) mantiene el material en un lugar más frío mientras se realiza el movimiento, reduciendo la velocidad a la que el material se derrite y sale de la boquilla.
* A veces, Cura intentará evitar el desgaste del filamento limitando el número de retracciones sobre una determinada longitud de filamento. Debido a que no hay retracciones entonces, producirá algo de filamento como un mal necesario en lugar de que la impresión falle. Si su alimentador no está moliendo demasiado el material, puede aumentar el [número de retracciones permitidas](../travel/retraction_count_max.md) o reducir la [longitud de filamento](../travel/retraction_extrusion_window.md) a lo largo de la cual cuenta estas retracciones.
* Permitir [Peinado](../travel/retraction_combing.md) en más lugares hará que la boquilla pase por el interior del modelo en lugar de por el exterior. Esto no evita realmente el encordado, pero lo hará invisible al colocarlo dentro del modelo.
* Si [el orden de impresión de la pared está mejor optimizado](../shell/optimize_wall_printing_order.md) entonces la boquilla se moverá hacia adelante y hacia atrás entre las partes con menos frecuencia, reduciendo la cantidad de encordado.
* Aumentar la [velocidad de desplazamiento] (../speed/speed_travel.md) generalmente hará que los cordones sean más finos durante los movimientos de desplazamiento más largos. Sin embargo, en los movimientos de desplazamiento cortos esto no supone una gran diferencia, ya que los límites de aceleración de las impresoras impedirán que la boquilla alcance esas velocidades de todos modos.
* La impresión con una boquilla más pequeña normalmente también reducirá el encordado. Es más fácil que el plástico rezume de una boquilla más grande.