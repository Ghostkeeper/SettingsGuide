Estrategia en IA
====
La preocupación más crítica para la fiabilidad de la impresión por cable son los puntos de conexión donde las capas del marco se conectan entre sí. Hay varias estrategias disponibles para hacer estas conexiones más fuertes. Este ajuste le permite elegir la estrategia que la impresora utilizará.

Compensar
----
Cuando se utiliza esta estrategia, la impresora tratará de compensar los factores de flacidez en el material. Como el material sale fundido por la boquilla, caerá un poco antes de solidificarse y será arrastrado por los movimientos de la boquilla. Esta estrategia deforma el patrón de dientes de sierra que conecta las capas de la estructura de tal manera que se espera que termine en la ubicación correcta de nuevo.

Existen dos factores de compensación: Uno que deforma el patrón de dientes de sierra sólo verticalmente para [compensar el hundimiento](wireframe_fall_down.md), y otro que deforma el patrón de dientes de sierra en dirección diagonal para [compensar que el material sea arrastrado](wireframe_drag_along.md) con la boquilla.

Nudo
----
Cuando se selecciona esta estrategia, se hará un pequeño movimiento hacia arriba y hacia atrás en la parte superior de cada diente de la sierra para formar un "nudo" de material allí. El propósito del nudo es dar al anillo horizontal en la parte superior de la misma un área para unirse al patrón de dientes de sierra. El nudo variará un poco de un lado a otro, por lo que si el anillo horizontal no está colocado con mucha precisión todavía hay una mayor posibilidad de que se adhieran el uno al otro. Además, el nudo hará que la línea ascendente se extienda un poco más hacia arriba, haciendo que el anillo horizontal sea empujado por encima de él. Y por último, el nudo también producirá algún rezago debido a la falta de retracción en este movimiento de desplazamiento. Esto produce una mancha sobre la que el anillo horizontal puede apoyarse mejor.

Dónde se dibuja el nudo y lo que implica su tamaño](../images/wireframe_top_jump.svg)

El movimiento para este "nudo" es una serie de movimientos de desplazamiento:
1. Primero, la boquilla se moverá hacia arriba y hacia atrás ligeramente.
2. Si hay algún [retardo](wireframe_top_delay.md) en la parte superior, la boquilla hará una pausa por la cantidad de retardo establecida. Esta pausa se realiza en la punta del movimiento del nudo.
3. En tercer lugar, la boquilla volverá a bajar a la altura ordinaria. Al mismo tiempo, la boquilla se moverá hacia adelante y se alejará de la línea vertical.

Retraer
----
Cuando se selecciona esta estrategia, el material se retraerá después de cada movimiento hacia arriba mientras se imprime el patrón de dientes de sierra. La idea es que al retraer el material, el hilo se rompe. Esto reduce el efecto de que el material es arrastrado junto con el movimiento de la boquilla, porque la línea anterior ya no está unida a la boquilla. Después, la boquilla da un pequeño salto de 1 milímetro y continúa con el movimiento diagonal hacia la capa inferior.

Una de las principales desventajas de esta estrategia es que la línea diagonal hacia abajo tampoco está ya unida. Esto hace que la extrusión durante esa línea sea inútil. El material simplemente termina como una mancha en la capa inferior. El material también está sujeto a más molienda ya que el material se retrae hacia adelante y hacia atrás sin mucha extrusión en el medio. Todo esto también lleva mucho tiempo.