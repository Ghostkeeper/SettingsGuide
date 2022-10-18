Evitar soportes al desplazarse
====
Normalmente, Cura no se molesta en hacer que la boquilla evite también las estructuras de soporte cuando [evita otras partes](travel_avoid_other_parts.md). Con esta configuración, Cura evitará golpear las estructuras de soporte mientras se desplaza.

Los soportes no tienen por qué ser bonitos, así que no es un problema si una mancha acaba en un soporte. De hecho, esto puede evitar que la mancha aparezca en la pared. Además, una cicatriz en el soporte no es un problema para su función. Sin embargo, si el material rezuma mucho y la mancha de ese rezago se aplica en el mismo lugar del soporte en cada capa, entonces esta mancha puede acumularse en grande, haciendo que eventualmente la boquilla derribe la estructura del soporte. En ese caso, puede ser beneficioso evitar el soporte durante el desplazamiento.

Algunas ventajas y desventajas de habilitar esta configuración son:
* Mayor fiabilidad, ya que hay una menor probabilidad de derribar el soporte al golpear la misma mancha repetidamente.
* Movimientos de desplazamiento ligeramente más largos y más rezuma como resultado.
* El rezume no se limpiará en el soporte, sino que acabará en la pared de la pieza a la que viaja la boquilla.
* Es posible que no haya ningún recorrido que evite el soporte, en cuyo caso la impresora recurrirá a una retracción y a un desplazamiento en línea recta, lo que supone un tiempo extra y puede dejar cicatrices adicionales en las paredes.