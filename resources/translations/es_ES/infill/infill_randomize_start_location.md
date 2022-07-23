Comienzo de relleno aleatorio
====
Si esta opción está activada, la posición en la que la impresora comenzará a imprimir el relleno en una capa será aleatoria.

El inicio de la pista de relleno suele ser un poco más débil que el resto del relleno. Esto ocurre cuando el relleno se imprime más rápido, con líneas más gruesas o tiene una mayor altura de capa. El flujo de material tiene que acelerarse de repente, y esto no ocurre instantáneamente, por lo que habrá una subextrusión durante un tiempo. Si esto sucede en el mismo lugar en cada capa, esto debilita la estructura de relleno. El lugar en el que ocurre esto será el eslabón más débil, y el relleno que lo rodea estará sometido a más tensión. Si la huella se somete a una fuerza, es ahí donde es más probable que se rompa.

Normalmente el relleno se inicia con la línea que está más cerca de la posición en la que estaba la boquilla cuando se inicia con el relleno, para reducir el tiempo de recorrido. Si esta opción está activada, esa posición de inicio se aleatoriza en su lugar. Esto repartirá los puntos débiles. Ya no habrá un eslabón más débil en la cadena, por lo que el relleno será más fuerte al final.

Sin embargo, esto aumenta ligeramente el tiempo de viaje y conduce a una mayor exudación dentro del modelo, ya que la distancia a la ubicación inicial del relleno ya no se minimiza.

**Aunque la ubicación inicial se distribuye de forma aleatoria, sigue siendo determinista. Si se repite dos veces el mismo corte, se obtendrán los mismos puntos de partida.