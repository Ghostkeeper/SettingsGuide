Relleno de espaguetis
====
Si este ajuste está activado, Cura extruirá todo el relleno de varias capas a la vez en una capa superior. Esto sirve como una forma extrema de [Espesor de la capa de relleno] (../infill/infill_sparse_thickness.md), pero sin el objetivo de mantener la rigidez del relleno. Tiene un poco de funcionalidad para hacer frente a las cantidades extremas de extrusión.

Esta característica no es funcional para los materiales ordinarios. Normalmente, usted querrá la resistencia de los patrones de relleno ordinarios, o dejar de lado el relleno por completo. Sin embargo, hay dos casos de uso para ello.

Casos de uso
----
Con materiales flexibles, esta técnica puede producir texturas muy suaves. El relleno de espaguetis tiende a producir anillos colocados de forma suelta que no se adhieren bien entre sí. Estos anillos son igualmente blandos en todas las direcciones. Para conseguir este efecto, la densidad del relleno no puede ser demasiado baja, o todos los espaguetis acabarán en el fondo de la impresión. Es aconsejable utilizar una [densidad de flujo](spaghetti_flow.md) entre el 30% y el 60%, dependiendo de la anchura de la línea y la altura de la capa. El resultado será un relleno igualmente rígido en todas las direcciones y bastante suave.

La otra aplicación para el relleno de espagueti es la fundición. Si usted tiene una impresora que incluye una herramienta para fundir en lugares específicos, esta característica se puede utilizar para llenar su modelo de manera bastante uniforme con las deposiciones de material controlado. Si se utiliza esto, la [densidad de flujo](spaghetti_flow.md) probablemente necesita ser aproximadamente el 100%, dependiendo de la relación de contracción/expansión del material fundido.

Ajuste de otras configuraciones para el relleno de espaguetis
----
Ambas aplicaciones requieren un manejo muy especial de su relleno. Estos son algunos ajustes que probablemente querrá ajustar a su necesidad:
* La [velocidad de impresión del relleno](../velocidad/velocidad_de_relleno.md) tiene que ser masivamente reducida. Si la boquilla necesita extrudir el relleno de 10 capas al mismo tiempo, querrá reducir la velocidad de impresión en al menos un factor de 8.
* Establezca su [espesor de la capa de relleno](../infill/infill_sparse_thickness.md) para que sea igual a la altura de la capa.
* Aumente su [temperatura de impresión](../material/material_print_temperature.md) ligeramente (para el extrusor que imprimirá el relleno). Esto permite que el material fluya correctamente fuera de la boquilla y permite una extrusión más rápida.
* Establecer la [alineación de la costura](../shell/z_seam_type.md) para que sea aleatoria para extender la estructura al azar.

**En la vista de capas de Cura, el relleno se mostrará como líneas muy gruesas. Esto se debe a que Cura asume que el material se mantiene en la misma capa y se extiende por ella. En realidad, caerá hacia abajo.**

**Mientras se utiliza el relleno de espagueti, el ajuste [infill line width](../resolution/infill_line_width.md) ya no tiene efecto. La anchura de la línea se ajusta a las necesidades de los ajustes [distancia de la línea de relleno](../relleno/distancia_de_línea_de_relleno.md) y [flujo de espaguetis](flujo_de_espaguetis.md).**.