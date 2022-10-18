Capas de la superficie superior del forro
====
Una parte de la parte superior de la impresión puede separarse e imprimirse con diferentes ajustes. Este ajuste determina el tamaño de la parte a separar. ¿Cuántas capas de la parte superior de la impresión tendrán ajustes separados?

<!--screenshot {
"image_path": "roofing_layer_count.png",
"models": [
    {
        "script": "question_stick_clip.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, -90, 60],
"settings": {
    "wall_line_count": 0,
    "skin_outline_count": 0,
    "roofing_layer_count": 1,
    "speed_roofing": 10,
    "cool_min_layer_time": 1,
    "roofing_extruder_nr": 1
},
"colour_scheme": "speed",
"colours": 32
}-->
![La capa más alta de la parte superior se imprime más lentamente (azul) que el resto de la piel (verde)](../images/roofing_layer_count.png)

Algunos ajustes pueden mejorar mucho la calidad de la superficie superior de la impresión, pero pueden hacer que la impresión tarde mucho más tiempo, ya que se aplican a todas las capas de la piel en la parte superior. Se puede conseguir un efecto similar ajustando esos parámetros sólo para la capa superior o dos, pero imprimiendo el resto de las capas de piel más rápidamente. Esto no tendrá un efecto negativo tan grande en el tiempo de impresión entonces.

Las configuraciones que se pueden ajustar para la superficie superior son:
* [Top Surface Skin Extruder](roofing_extruder_nr.md)
* [Flujo de la piel de la superficie superior](../material/roofing_material_flow.md)
* [Velocidad de la piel de la superficie superior](../speed/speed_roofing.md)
* [Aceleración de la piel de la superficie superior](../speed/acceleration_roofing.md)
* [Tirón de la piel de la superficie superior](../speed/jerk_roofing.md)
* Ancho de línea de la piel de la superficie superior](../experimental/roofing_line_width.md)
* [Patrón de piel de la superficie superior](../experimental/roofing_pattern.md)
* [Direcciones de la línea de piel de la superficie superior](../experimental/roofing_angles.md)

Para conseguir una superficie superior más bonita, intente reducir la velocidad y aumentar el impulso.

Cuando se imprime la superficie superior en un color diferente (utilizando el ajuste [Extrusor de la superficie superior del forro](roofing_extruder_nr.md), a menudo es necesario imprimir más de una capa en el otro color. De lo contrario, el color original seguirá siendo el mismo.