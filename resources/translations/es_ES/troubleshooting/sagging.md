Hundimiento ('Sagging')
====
La fabricación con filamento fundido funciona mediante la colocación de una línea de plástico fundido. Esta línea es blanda y, si no se apoya en nada, se hunde. Esto se llama hundimiento.

¡[Hundimiento en las partes que sobresalen](../images/sagging.jpg)

El hundimiento tiende a hacer que las partes que sobresalen parezcan fibrosas. En lugar de seguir suavemente la superficie prevista del modelo, será demasiado baja. En casos extremos, la parte inferior de una superficie se vuelve tan rasgada que se puede ver el interior hueco de la impresión.

Causas
----
En realidad, el hundimiento no está causado, o apenas, por la gravedad. Se debe principalmente a la fuerza del material que sale por la boquilla. Por ello, incluso las impresoras que se ponen boca abajo o que imprimen en microgravedad experimentarán este fenómeno. La presión con la que se extruye el material lo empuja hacia abajo porque la boquilla está (normalmente) orientada hacia abajo.

Normalmente la presión dentro de la cámara de la boquilla es necesaria para empujar el material (viscoso) hacia el exterior y aplanarlo en forma de una línea ancha y plana de material, aplastándolo entre la boquilla y la capa anterior o la placa de impresión. Sin embargo, si no había material en la capa anterior, no habrá contrapresión para aplanar el cordón. En su lugar, será empujado demasiado hacia abajo.

Puentes ('Bridging')
----
Una técnica para mejorar la calidad de los rebordes es optimizar la forma de puentear el hueco que sobresale. Esto implica reducir la presión con la que se empuja el material fuera de la boquilla, así como intentar aumentar la viscosidad del material o hacer que se solidifique más rápido. Además, se pueden reorientar las líneas impresas para reducir la distancia a lo largo de la cual las líneas no se sostienen. El conjunto de estas técnicas se denomina "bridging".

Cura ofrece una serie de formas de mejorar el puenteado. Proporcionará aún más si se habilitan [ajustes de puente](../experimental/bridge_settings_enabled.md). Al habilitarlo, aparecerán más ajustes y también se ajustan los parámetros de impresión de las zonas de puente por defecto.

Al configurar el puenteado para reducir el pandeo, considere los siguientes ajustes:
* Reducir la [temperatura de impresión](../material/material_print_temperature.md) hace que el termoplástico sea más viscoso, haciendo que se pandee menos.
* Reducir la [altura de la capa](../resolution/layer_height.md) o el [ancho de línea](../resolution/line_width.md) reduce la presión con la que el material es empujado fuera de la boquilla. Esto por sí mismo reduce el pandeo, pero estas líneas también tienen una menor capacidad de calor, haciendo que los ventiladores del cabezal de impresión sean más efectivos en la refrigeración.
* Reduciendo la [velocidad de impresión] (../speed/speed_print.md) se reduce también la presión con la que el material es empujado fuera de la boquilla. En este caso la capacidad térmica no se reduce, pero los ventiladores estarán soplando sobre el material durante más tiempo, lo que también aumenta su eficacia y reduce el hundimiento. Si la configuración de los puentes está activada, la velocidad de impresión de los puentes se puede ajustar por separado. La reducción de la [velocidad de impresión de los muros puente](../experimental/bridge_wall_speed.md) es eficaz para mejorar los voladizos inclinados. La reducción de la [velocidad de impresión de la piel del puente](../experimental/bridge_skin_speed.md) es eficaz para reducir el pandeo en las zonas de voladizos completamente horizontales. También hay una variante de esto que ajusta la [velocidad para muros salientes](../experimental/wall_overhang_speed_factor.md). Este ajuste se activará incluso si la superficie no es completamente horizontal, permitiendo una velocidad de impresión de salientes específica sólo para paredes inclinadas.
* Reducir la [velocidad de flujo](../material/material_flow.md) es similar a reducir el ancho de línea. Esto reducirá la presión con la que el material es empujado hacia fuera así como la capacidad térmica, permitiendo que el material se solidifique más rápido. Esta configuración se puede ajustar también sólo para las áreas de puente, por separado para las [paredes](../experimental/bridge_wall_material_flow.md) o la [piel](../experimental/bridge_skin_material_flow.md). Reducir el flujo para grandes áreas tiende a producir huecos en la superficie y un aspecto irregular, así que visualmente el voladizo puede seguir pareciendo malo si se ajusta esto. Sin embargo, la precisión dimensional debe ser mejorada.
* Aumente la [velocidad del ventilador] (../cooling/cool_fan_speed.md) para enfriar el material más rápido. Esto solidifica el material más rápido, evitando que se caiga.
* Imprime las paredes de [dentro a fuera](../shell/outer_inset_first.md). Esto permitirá que la pared exterior se apoye sobre la pared interior adyacente, lo que evita que se caiga. Esto es más efectivo con un pequeño [ancho de línea](../resolution/wall_line_width_0.md).

<!--screenshot {
"image_path": "support_enable.png",
"models": [{"script": "pipe_corner.scad"}],
"camera_position": [77, 197, 40],
"settings": {"support_enable": true},
"colours": 64
}-->
Soporte
----
![Una estructura de soporte sostiene el modelo](../images/support_enable.png)

La forma más común y fiable de mejorar las piezas que sobresalen es apoyarlas con una estructura de soporte durante la impresión. Esta estructura de soporte se retira posteriormente una vez que el material se ha solidificado. El soporte de impresión es muy efectivo para prevenir el pandeo sin importar el tamaño del área sobresaliente, pero toma tiempo y material extra y deja una cicatriz donde el soporte fue adherido.

<!--if cura_version >= 4.7-->Cura tiene dos técnicas para generar el soporte, indicadas con el ajuste [Support Structure](../support/support_structure.md). Hay un método "normal" por defecto, y un método "de árbol". La construcción normal suele ser más eficaz para reducir el hundimiento, pero a veces también dará un lado inferior más irregular. El soporte de árbol tiende a dejar que las cuerdas se comben un poco más, pero también de manera más uniforme.<!--endif-->
<!--if cura_version < 4.7:Cura tiene dos técnicas para generar el soporte. Hay un método de "soporte de área" por defecto, que se genera si [el soporte está habilitado](../support/support_enable.md). Alternativamente, se genera un método de soporte de árbol si [soporte de árbol está habilitado](../experimental/support_tree_enable.md). La técnica por defecto es generalmente más efectiva para reducir el hundimiento, pero a veces también dará un lado inferior más desigual. El soporte de árbol tiende a dejar que las cuerdas se comben un poco más, pero también de manera más uniforme.

La generación de soportes de Cura decidirá dónde colocar los soportes automáticamente. En la mayoría de los casos esto funciona bien, pero para algunos modelos puede añadir muy poco o demasiado apoyo. Por suerte, Cura también proporciona muchos métodos para personalizar la colocación de los apoyos.
* Ajustar el [ángulo de voladizo] (../support/support_angle.md) es la forma más básica de ajustar la cantidad de material de soporte que se coloca. Debería ajustar este parámetro de manera que todas las áreas que sobresalen sean apoyadas. Este ajuste también determina qué áreas se dibujan en rojo en la etapa de Preparación. Reducir el ángulo del voladizo hará que se imprima más soporte, lo que reduce el hundimiento en más partes de la impresión, pero también llevará más tiempo y material y causará más cicatrices.
* Puede eliminar las partes que sobresalen por encima de otras partes estableciendo el ajuste [Colocación del soporte](../support/support_type.md) a "Tocar la placa de impresión". Si se ajusta a "En todas partes", se puede evitar que el voladizo sea malo.
* Asegúrese de que el [Minimum Support Area](../support/minimum_support_area.md) no está borrando trozos finos de soporte.
* Con la herramienta de bloqueo de soporte, puedes colocar cubos en tu escena para evitar que se genere soporte allí. También puedes seleccionar estos bloques y en la herramienta de configuración por modelo decirle a Cura que los "imprima como soporte". Entonces se imprimirán como una nueva pieza de soporte. De este modo, puede personalizar cuidadosamente el lugar exacto en el que se coloca el soporte. Incluso puede cargar un modelo 3D completo en Cura con la forma exacta de su soporte, y decirle a Cura que lo imprima como soporte en la herramienta de configuración por modelo.

Incluso si el voladizo está apoyado por el soporte, puede que se hunda un poco. Para permitir que el soporte se retire, se mantiene una cierta [distancia vertical](../soporte/support_z_distance.md) entre el modelo y el soporte. El modelo se hundirá hasta esta distancia antes de que el soporte sea efectivo, por lo que reducir la distancia Z reducirá el hundimiento (pero hará que el soporte sea más difícil de quitar). Algunos materiales están diseñados para ser retirados más fácilmente, al no adherirse químicamente al material de construcción o disolverse. Estos materiales pueden permitirse el lujo de reducir la distancia Z, reduciendo aún más el hundimiento, mientras que todavía es posible eliminar el apoyo después. La impresión también puede combarse entre las líneas de soporte, por lo que reducir la [distancia entre las líneas de soporte] (../support/support_line_distance.md) también reducirá el pandeo (pero aumentará el tiempo de impresión y de nuevo dificultará la retirada del soporte).

Ajustar el modelo
----
Si usted tiene la libertad de ajustar el modelo que se imprime, puede dar lugar a un resultado mucho más limpio que tratar de salvar los voladizos o apoyarlos. En lugar de dejar que el material se hunda en los salientes, diseña y orienta tu modelo de forma que no haya salientes.

<!--screenshot {
"image_path": "support_minimise_overhang.png",
"models": [
    {
        "script": "dowel.scad",
        "transformation": ["rotateY(127)"]
    }
],
"settings": {"support_angle": 55},
"camera_position": [21, -104, -30],
"layer": -1
}-->
![Esta orientación permite imprimir el objeto con muy poco apoyo](../images/support_minimise_overhang.png)

El truco más básico para aplicar esto es rotar el modelo. Si tu impresora es capaz de imprimir ángulos de 45 grados sin pandeo, puedes rotar un modelo con una pieza vertical y otra horizontal de forma que sean dos inclinaciones de 45 grados, reduciendo ligeramente la calidad de la pared vertical, pero evitando el pandeo en la parte horizontal. Sin embargo, tenga cuidado de no hacer el área de contacto con la placa de impresión demasiado pequeña, o la impresión podría desprenderse de la placa de impresión y arruinarse aún.

Añadir chaflanes también puede ayudar a reducir la cantidad de salientes en el modelo con relativamente poco material añadido. Cura proporciona un método automatizado para añadir chaflanes a su modelo, a través de la configuración [Convertir voladizo en imprimible](../experimental/conical_overhang_enabled.md). Añadir chaflanes esencialmente añade la estructura de soporte al modelo real. Entonces se imprimirán sin problemas en el modelo, lo que tiene un aspecto más bonito. También se ahorra en material, en comparación con la impresión del soporte, ya que el material de soporte lleva las fuerzas rápidamente hacia el resto del modelo. Y al final, tu objeto será más fuerte.

En general, cuando se diseñan objetos para la impresión 3D, es mejor evitar los voladizos en absoluto. Si la geometría del objeto no te lo permite, considera la posibilidad de dividir el modelo en varias partes y ensamblarlas después.