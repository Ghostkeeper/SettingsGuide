Grosor de la capa de relleno
====
Como la altura de la capa de relleno no es importante para la calidad visual, puede utilizar capas más gruesas para el relleno para reducir el tiempo de impresión. Este ajuste hace que las capas de relleno se combinen entre sí, siempre que haya varias capas de relleno directamente encima de otras. Entonces no imprimirá ningún relleno en algunas de las capas, pero en la más alta de las capas combinadas extruirá más material para compensarlo.

En la vista de capas, parecerá que las líneas de relleno son mucho más anchas. Cuando se imprima realmente, las líneas de relleno bajarán más en lugar de extenderse horizontalmente.

<!--screenshot {
"image_path": "infill_sparse_thickness.png",
"models": [{"script": "cooking_utensil_hook.scad"}],
"camera_position": [6, 51, 27],
"camera_lookat": [0, 0, 7],
"settings": {
    "layer_height": 0.2,
    "wall_line_count": 0,
    "infill_pattern": "zigzag",
    "infill_sparse_thickness": 0.6
},
"layer": 19,
"colours": 64
}-->
![El grosor de la capa de relleno se establece en tres veces la altura de la capa](../images/infill_sparse_thickness.png)

El grosor de la capa de relleno debe ser un múltiplo de la altura de la capa ordinaria. Si no lo es, se redondeará a la altura de capa más cercana.

* Tenga cuidado con aumentar esto demasiado. Cuando se cambia a y desde el relleno, la tasa de flujo a través de la boquilla necesita acelerar y desacelerar significativamente. Hay un cierto retraso en esto, por lo que extruirá muy poco al principio del relleno y demasiado al final del mismo.
* En las capas intermedias, seguirá imprimiendo relleno con un grosor de capa inferior cuando no haya relleno en las capas de alrededor. Esto puede hacer que se impriman pequeñas líneas de relleno a lo largo de las paredes inclinadas.