Utilizar capas de adaptación
====
Las capas de adaptación ajustarán el grosor de las capas de su impresión localmente para optimizar el tiempo y la calidad de la impresión en función de las características de la superficie del modelo. Las capas se harán más delgadas donde hay pendientes poco profundas, o se harán más gruesas donde las paredes son empinadas. El propósito de esto es imprimir rápido cuando sea posible, pero aún así imprimir detalladamente cuando sea necesario.

<!--screenshot {
"image_path": "adaptive_layer_height_enabled.png",
"models": [{"script": "barn.scad"}],
"camera_position": [-108, -229, 118],
"settings": {
    "adaptive_layer_height_enabled": true,
    "layer_height": 0.2
},
"colour_scheme": "layer_thickness",
"colours": 128
}-->
![Con el esquema de colores de "grosor de capa", puede ver que colorea las capas más finas de azul y las más gruesas de amarillo](../images/adaptive_layer_height_enabled.png)

La altura de las capas se ajusta de forma que la distancia horizontal entre los bordes de las capas se mantenga constante. Las superficies poco profundas provocan un gran desplazamiento horizontal con un pequeño desplazamiento vertical, por lo que se realiza un pequeño desplazamiento vertical para mantener constante el desplazamiento horizontal. En el caso de las superficies empinadas, se produce un pequeño desplazamiento horizontal con un gran desplazamiento vertical, por lo que se realiza un gran desplazamiento vertical para mantener constante el desplazamiento horizontal. De este modo, el efecto topográfico de las capas se mantiene constante. La distancia máxima entre dos capas adyacentes se mantiene a una distancia constante del ajuste [Threshold](adaptive_layer_height_threshold.md).

Si el modelo tiene superficies poco profundas y superficies empinadas a la misma altura, el grosor de la capa se toma como el menor de los grosores de la capa. Esto a veces hace que la altura de la capa sea innecesariamente pequeña porque hay una superficie horizontal al lado. Esto puede verse en la captura de pantalla de arriba, así como en la altura del silo de la izquierda.

Las capas adaptativas están fuertemente restringidas para mejorar la calidad de la impresión. No se permite que la altura de la capa se desvíe más de una [Variación máxima](adaptive_layer_height_variation.md) especificada del ajuste original de [Altura de la capa](../resolution/layer_height.md). Entre dos capas adyacentes, la diferencia de altura de la capa no puede ser superior a un determinado [Tamaño de paso](adaptive_layer_height_variation_step.md). Esto hace que el grosor de la capa transite gradualmente en lugar de reducirse repentinamente a la mitad de una capa a la siguiente.

Las capas adaptativas pueden reducir considerablemente el tiempo de impresión sin sufrir una pérdida de calidad de impresión, o incluso mejorando la calidad en algunos casos. El efecto de ajustar el grosor de las capas es inmenso. En la mayoría de los casos, el tiempo de impresión se reducirá en gran medida, debido a la utilización de capas más gruesas donde el modelo es vertical. El [efecto de topografía](../troubleshooting/topography.md) también se reduce porque las capas están más espaciadas horizontalmente.

Sin embargo, esta característica puede introducir una serie de problemas también.
* Al cambiar la altura de la capa, normalmente hay que ajustar también otros parámetros, como la temperatura de la boquilla. Las capas adaptativas no se ajustan automáticamente. Esto puede hacer que la impresión no sea óptima para, por ejemplo, los voladizos que irían mejor con una temperatura de impresión más baja.
* Si la altura de la capa se cambia en toda la capa para una pequeña característica en algún lugar de una pequeña parte de la capa, la banda será visible en el resto de la capa.
* Las distancias verticales se ajustan involuntariamente con esto también. Esto puede tener un efecto negativo en la calidad de impresión. Por ejemplo, el [Top/Bottom Thickness](../top_bottom/top_bottom_thickness.md) normalmente será más bajo porque Cura mantendrá el ajuste [Top Layers](../top_bottom/top_layers.md) como verdad, y las capas se vuelven más delgadas. Esto puede causar la formación de almohadillas. Los ajustes afectados que pueden dejar de ser correctos son:
  * [Espesor superior](../top_bottom/top_thickness.md)
  * Espesor inferior](../top_bottom/bottom_thickness.md)
  * Ángulo máximo de la piel para la expansión](../top_bottom/max_skin_angle_for_expansion.md)
  * Altura del escalón de relleno gradual](../infill/gradual_infill_step_height.md)
  * Altura del escalón de relleno gradual](../support/gradual_support_infill_step_height.md)
  * Espesor de la capa de relleno](../infill/infill_sparse_thickness.md)
  * Espesor de la capa de relleno de apoyo](../support/support_infill_sparse_thickness.md)
  * [Distancia Z del soporte](../support/support_z_distance.md)
  * [Espesor del techo de apoyo](../support/support_roof_height.md)
  * [Espesor del suelo de apoyo](../soporte/altura_inferior_de_apoyo.md)
  * [Ángulo del voladizo de apoyo](../soporte/ángulo_de_apoyo.md)
  * [Altura del escalón de apoyo](../support/support_bottom_stair_step_height.md)
  * [Ángulo del techo de la torre](../support/support_tower_roof_angle.md)
  * [Ángulo del escudo de exudado](../dual/ooze_shield_angle.md)
  * [Ángulo máximo del modelo](../experimental/conical_overhang_angle.md)