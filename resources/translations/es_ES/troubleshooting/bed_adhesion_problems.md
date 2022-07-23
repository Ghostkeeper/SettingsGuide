Problemas de adherencia de la cama
====
Uno de los fallos más comunes en las impresiones 3D es que la impresión se suelte de la placa de impresión mientras se está imprimiendo. Este artículo repasa algunos ajustes que puedes hacer para evitar que esto ocurra.

Si la impresión se pierde de la placa de impresión, generalmente verás un montón de cables sueltos por toda la placa de impresión. Si tienes más suerte, puede manifestarse también como un simple [cambio de capa] (layer_shift.md) (y habrá menos que limpiar). De cualquier manera, la impresión está arruinada.

Métodos de adhesión de la cama
----
Cura proporciona varios métodos para mejorar la adhesión de la cama. Puede elegir entre estos métodos con el ajuste [Build Plate Adhesion Type](../platform_adhesion/adhesion_type.md). Están disponibles las siguientes opciones.
* Brim, la técnica más común, añade un borde alrededor de la parte inferior de la impresión, que se suma a la superficie para que la impresión se adhiera mejor a la placa de construcción.
* Un raft es una placa debajo de toda la impresión. Esta placa obtiene una mayor superficie también, para que se pegue bien. Si la balsa se imprime con un material que se adhiere bien a la impresión (como con el mismo material) entonces la impresión se mantendrá en su lugar de esa manera.
* Un faldón no se adhiere a la impresión, sino que sólo la rodea. Esta línea asegura que el material está fluyendo antes de que la impresión real comience, por lo que no hay subextrusión en la primera capa que podría arruinar la adhesión.
* También puede no tener adherencia seleccionando "Ninguno". Esto ahorra tiempo y material y evita otros efectos negativos de los métodos mencionados. Utilice esto sólo si su impresora tiene una técnica de imprimación diferente, como un cubo de purga.

El borde y la balsa son las técnicas más eficaces para aumentar la adherencia, ya que están diseñadas expresamente para ello. La mayoría de las impresiones de tamaño razonable necesitarán cualquiera de ellas.

Si se utiliza un borde, se puede aumentar la adherencia aún más aumentando el [ancho del borde] (../platform_adhesion/brim_width.md). También se puede añadir un borde en el [interior de los soportes](../soporte/soporte_brim_enable.md) y en la [torre principal](../dual/torre principal_brim_enable.md) así como entre el [modelo y soporte](../platform_adhesion/brim_replaces_support.md) y los [agujeros interiores](../platform_adhesion/brim_outside_only.md) del modelo.

Del mismo modo, si se utiliza una balsa, se puede aumentar la adherencia aún más aumentando el [ancho de la balsa](../platform_adhesion/raft_margin.md). Sin embargo, la balsa siempre se imprimirá debajo de todo, ya que las capas tienen que coincidir. Si la adhesión entre el modelo y la balsa es un problema, considere reducir el [air gap](../platform_adhesion/raft_airgap.md) entre la balsa y el modelo. Además, puede considerar aumentar el [ancho de la línea base de la balsa](../platform_adhesion/raft_base_line_width.md).

Prevención de la deformación
----
Si su impresión sufre de alabeo, el área de contacto entre la impresión y la placa de construcción se reduce considerablemente. Para evitarlo, consulta el artículo sobre [warping](warping.md). En resumen, estos son algunos ajustes a realizar para evitar el warping.
* Configure el [Patrón de fondo de la capa inicial](../top_bottom/top_bottom_pattern_0.md) como concéntrico.
* Reduzca la [Temperatura de la placa de construcción](../material/material_bed_temperature.md) y aumente la [Temperatura del volumen de construcción](../material/build_volume_temperature.md).
* Ajuste el modelo de manera que haya menos esquinas exteriores afiladas en la primera capa.

Nivelar la placa de construcción
----
Otra fuente común de problemas de adhesión es que la placa de construcción no está nivelada. Cura asumirá que la boquilla toca la placa de impresión cuando se mueve a la coordenada Z 0, pero esto es raramente el caso. Las placas de impresión se inclinan, se mueven hacia arriba y hacia abajo, e incluso se doblan. Si la placa de impresión no está en la coordenada 0 en todas partes, Cura extruirá más material del que cabe en el espacio entre la boquilla y la placa de impresión, y obtendrá sobreextrusión o subextrusión. Cuando el lecho está demasiado cerca, la sobreextrusión puede dar lugar a manchas, lo que puede hacer que la boquilla arranque la impresión de la placa de impresión en un movimiento de desplazamiento. Cuando la cama está demasiado lejos, la subextrusión impide que el material sea empujado a la placa de impresión, lo que impide que se conecte correctamente a ella. En cualquier caso, la impresión no es fiable.

Algunas impresoras tienen sensores que pueden medir dónde está la placa de impresión y compensarlo en el firmware. Para esas impresoras, mover la boquilla a la coordenada Z 0 hará que la boquilla toque la cama. Sin embargo, esto tiene la desventaja de que el modelo se deforma. Para compensar una placa de impresión inclinada, se obtendría un lado inferior inclinado, o toda la impresión puede inclinarse, girarse o deformarse. Si su impresora es incapaz de compensar una cama que no está nivelada, hay algunas cosas que se pueden hacer desde el lado de Cura también:
* Aumentar la [altura inicial de la capa] (../resolution/layer_height_0.md). Esto ofrece un poco más de margen de error. También aumenta la fuerza con la que el material es empujado fuera de la boquilla y en la placa de impresión.
* Reduce la [Velocidad de desplazamiento de la capa inicial](../speed/speed_layer_0.md). Esto reduce la posibilidad de que un movimiento de desplazamiento saque las líneas previamente impresas de la placa de impresión.
* Del mismo modo, considere ajustar la [Aceleración de la capa inicial](../speed/acceleration_layer_0.md) y la [Impulso de la capa inicial](../speed/jerk_layer_0.md) también. Estos reducen las vibraciones, que pueden causar la subextrusión y la sobreextrusión periódicas.
* Aumentar el [Número de capas lentas](../speed/speed_slowdown_layers.md). Esto reduce la posibilidad de que los movimientos rápidos arranquen las capas anteriores.

Ajustes varios
----
Estos ajustes también pueden ser ajustados si los métodos normales de adhesión de la cama no son suficientes.
* Aumentar el [Ancho de línea de la capa inicial](../resolution/initial_layer_line_width_factor.md). Esto empuja el material hacia fuera con más fuerza, pegándolo bien a la placa de impresión.
* Aumentar la [Temperatura de impresión de la capa inicial](../material/material_print_temperature_layer_0.md) hace que el material fluya más hacia la placa de impresión, aumentando el área de contacto.
* Al igual que al aumentar la temperatura, también puede reducir la [Velocidad del ventilador de la capa inicial](../cooling/cool_fan_speed_0.md) o aumentar la [duración de ese ajuste](../cooling/cool_fan_full_at_height.md) para mantener el material fluido durante más tiempo.
* Del mismo modo, reduzca la [Velocidad de la capa inicial](../speed/speed_layer_0.md). Reducir la [Velocidad de impresión de la capa inicial](../speed/speed_print_layer_0.md) hace que el material vuelva a fluir más, ya que el material se mantiene fluido durante más tiempo por la boquilla caliente.

Plataformas de impresión
----
Aparte de una buena impresión, una buena placa de impresión también es importante para la adhesión. Una buena placa de impresión debe estar:
* ...¡limpia! Es muy importante que la placa de impresión no contenga grasa (como la de los dedos) ni polvo. Limpiarla bajo un grifo caliente es muy eficaz. Lo ideal es utilizar alcohol y un paño de microfibra.
* ...¡nivelada! Si la placa de impresión está demasiado cerca, el flujo que sale de la boquilla será inconsistente, lo que dará lugar a bultos que la boquilla arrancará cuando se acerque la próxima vez. Si la placa de impresión está demasiado lejos, el material no se empuja bien sobre la placa de impresión, lo que reduce mucho la superficie. La mayoría de las impresoras permiten ajustar la placa de impresión con unos tornillos de mariposa, así que asegúrate de que está perfectamente nivelada y separada correctamente de la boquilla.
* ...¡áspera! Con una placa de impresión ligeramente rugosa, el área de contacto entre la placa de impresión y la impresión aumenta considerablemente en comparación con una placa de impresión perfectamente lisa. Algunas impresoras vienen con vidrio esmerilado o metal anodizado por esta razón.

El material de la placa de impresión también tiene un gran impacto en las propiedades adhesivas. Esto puede ser muy diferente con diferentes materiales de impresión. Los materiales más comunes de las placas de impresión son el vidrio, el acrílico, el aluminio, el acero o el aluminio anodizado. Cada uno de ellos se adhiere a diferentes materiales. Las placas de impresión de plástico pueden adherirse químicamente a su material. Otros materiales se basan en una superficie rugosa para aumentar el área de contacto.

También hay métodos de adhesión a la cama que se pueden aplicar a cualquier placa de impresión:
* Las barras de pegamento de papel genérico funcionan muy bien. Aunque el pegamento se seca rápidamente, produce una superficie áspera con mayor superficie para que la impresión se adhiera.
* La cinta adhesiva tiene un efecto similar, ya que tiene una superficie rugosa hecha de papel, pero a diferencia del papel se mantiene perfectamente plana en la placa de impresión. Los tipos más gruesos de cinta adhesiva fabricados para uso exterior son los más eficaces.
* La laca funciona de forma similar al pegamento, ya que deja una superficie rugosa de grano fino en la placa de impresión. Es muy fácil aplicarla uniformemente.
* Aplique un poco de papel de lija a la placa de impresión para hacerla más áspera y aumentar el área de contacto. No la desbastes demasiado, o tendrás una superficie desigual para imprimir. Utiliza papel de lija de grano muy fino para hacerlo, de grano 500 o más.
* Muchos vendedores de impresoras 3D venden "hojas de adhesión" especializadas que se pueden extender sobre la placa de impresión. Funcionan de forma similar a la cinta adhesiva, pero están hechas para durar más tiempo. Algunas están hechas de un plástico que se adhiere químicamente al material impreso.