Pata de Elefante
====
A veces, la parte inferior de la huella es ligeramente más ancha que el resto de la huella, lo que da lugar a un pequeño labio allí. A esto se le llama "pata de elefante", ya que se asemeja a las patas de un elefante donde los dedos son ligeramente más anchos que el resto de la pierna.

Hay varios efectos que la gente llama pie de elefante con causas inherentes completamente diferentes. Estas requerirán también soluciones completamente diferentes. Este artículo le ayudará a encontrar la causa principal.

Pie de elefante causado por la fuerza de las capas de la piel](../images/elephants_foot.jpg)

Borde
----
A veces la pata de elefante es en realidad una parte del borde que no se ha retirado correctamente. Si has arrancado el borde con la mano, puedes saberlo porque la línea del borde es completamente adyacente a la línea normal de la pared, y la línea normal de la pared está directamente debajo del resto de la pared. Para eliminar el borde por completo, lo mejor es utilizar un cuchillo afilado para tallar a lo largo de la parte inferior de la impresión.

Si el modelo no tiene un lado inferior grande, considere establecer el [método de adhesión](../platform_adhesion/adhesion_type.md) a una falda en su lugar. Si esto da demasiados problemas con la adhesión de la cama, puede probar métodos alternativos para mejorar la adhesión, como establecer el [Patrón de fondo de la capa inicial](../top_bottom/top_bottom_pattern_0.md) a "concéntrico".

Alabeo ('Warping')
----
Quizás la causa más común de una pata de elefante real es el alabeo. Cuando el material se enfría, se encoge un poco. A veces, el material de la(s) capa(s) inferior(es) no puede encogerse. Siguen teniendo su tamaño original, pero las capas superiores se encogen un poco. Hay varias razones por las que las capas inferiores pueden ser incapaces de encogerse:
* Está pegada a la placa de impresión, que no se encoge.
* Está calentada por la placa de impresión, lo que impide que se encoja.
* Hay una piel adyacente que bloquea la contracción. (En las capas superiores puede haber relleno en su lugar).

Para evitar el alabeo, eche un vistazo al [artículo de solución de problemas](warping.md) al respecto. Específicamente para este tipo de alabeo, aquí hay algunas cosas que puede probar:
* Aumentar el [grosor de la pared](../shell/wall_thickness.md) para evitar que las paredes junto al relleno se contraigan.
* Reducir la [temperatura de la placa de impresión](../material/material_bed_temperature.md) para permitir que la primera capa se encoja tanto como las demás. Si la temperatura de la cama era muy alta, también puede permitir que el material se hunda un poco, lo que hace que sea más ancho en la parte inferior. Este efecto suele ser pequeño, pero también se evitará reduciendo la temperatura del lecho.
* Aumente el [grosor del fondo](../espesor_del_fondo/espesor_del_fondo.md) para pasar más gradualmente a un tamaño reducido. Incluso puede considerar imprimir el modelo completamente sólido (preferiblemente estableciendo el espesor inferior extremadamente alto) para deshacerse de la diferencia de contracción por completo.
<!--si cura_version>=5.0-->* [Alternar las direcciones de las paredes](../experimental/material_alternate_walls.md) para reducir las tensiones internas en el modelo.<!--endif-->

Ajustes de la placa de impresión
----
La pata de elefante también puede ser causada por tener la placa de impresión demasiado cerca de la boquilla mientras se imprime la primera capa. Esto efectivamente sobreextruye, lo que hace que la primera capa sea empujada hacia afuera.

Para ajustar la placa de impresión, consulte el manual de su impresora 3D. La mayoría de las impresoras tienen tornillos de ajuste en la cama o el pórtico para ajustar la diferencia de altura de la placa de impresión durante la primera capa. Ajuste la placa de impresión durante la impresión (durante el borde, la falda o la balsa, preferiblemente) hasta que la primera capa sea agradable y suave y no más delgada que cualquier otra capa.

También puede ajustar directamente el [flujo en la primera capa](../material/material_flow_layer_0.md) en Cura para compensar cualquier sobreextrusión. Alternativamente, reducir el [ancho de línea de la capa inicial](../resolution/initial_layer_line_width_factor.md) también puede normalizar la extrusión lo suficiente como para evitar la pata de elefante.

Deformación por encima de la transición vítrea
----
En el caso de impresiones muy pequeñas, existe la posibilidad de que la capa anterior no se haya solidificado todavía cuando se empuja la siguiente capa sobre ella. El material se empuja con una fuerza considerable desde la boquilla, por lo que si la capa anterior aún no se ha solidificado, esta capa se aplastará y se expandirá horizontalmente. Esto se manifiesta como una pata de elefante. La solución a esto es asegurarse de que el material está solidificado en el momento en que la siguiente capa es empujada sobre ella. Intente ajustar las siguientes configuraciones:

* Reducir la [temperatura de impresión durante la primera capa](../material/material_print_temperature_layer_0.md), para que el material no tenga que enfriarse tanto.
* Reducir la [temperatura de la cama durante la primera capa](../material/material_bed_temperature_layer_0.md), para que la primera capa se enfríe más rápido, expulsando más calor a la placa de impresión. Los plásticos para la impresión 3D están diseñados para solidificarse muy rápidamente en un punto de temperatura preciso, su [temperatura de transición vítrea] (https://en.wikipedia.org/wiki/Glass_transition#Transition_temperature_Tg). Para evitar la deformación, busca la temperatura de transición vítrea de tu filamento en su hoja de datos, y asegúrate de que la temperatura de la base no supere demasiado esta temperatura de transición.
* Aumenta la [velocidad del ventilador durante las primeras capas](../cooling/cool_fan_speed_0.md), para enfriar el material más rápidamente. Considere también aumentar el ajuste [velocidad regular del ventilador en altura](../cooling/cool_fan_full_at_height.md), para seguir enfriando las primeras capas.
* Reducir la [velocidad de la capa inicial](../velocidad/velocidad_capa_0.md). Esto permite más tiempo para que la primera capa se enfríe después de ser impresa.
* Aumentar el [tiempo mínimo de la capa] (../cooling/cool_min_layer_time.md). El propósito de esto es asegurar un cierto tiempo para que cualquier capa se enfríe antes de que la siguiente capa se coloque encima, y también hará que se utilice la [velocidad máxima del ventilador](../cooling/cool_fan_speed_max.md). Efectivamente, esta es una forma más fácil de combinar los ajustes de la velocidad inicial de la capa y la velocidad del ventilador que se indican más arriba. Tenga en cuenta que esto se aplica a toda la impresión, sin embargo, no sólo la primera capa. 

Soluciones generales
----
Aquí hay algunas soluciones que puede probar que se deshacen de cualquier tipo de pata de elefante, independientemente de su causa:
* Usar una [balsa](../platform_adhesion/adhesion_type.md) mueve toda la impresión fuera de la placa de impresión, evitando cualquier efecto causado por la placa de impresión como su temperatura y que se pegue demasiado a la placa de impresión, y también evita la necesidad de un borde.
* Reducir la [Expansión horizontal de la capa inicial](../shell/xy_offset_layer_0.md) (posiblemente a algo negativo). Esto compensa la pata de elefante en la primera capa.