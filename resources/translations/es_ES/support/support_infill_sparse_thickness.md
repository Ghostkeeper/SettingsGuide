Grosor de la capa de soporte
====
Dado que la calidad visual y la resolución del soporte no son importantes, puede utilizar capas más gruesas para el soporte para reducir el tiempo de impresión. Este ajuste configura el grosor de las capas con las que se imprime el soporte.

En la vista de capas, parecerá que las líneas de soporte son mucho más anchas. Cuando se impriman realmente, las líneas de soporte bajarán más en lugar de extenderse horizontalmente.

<!--screenshot {
"image_path": "support_infill_sparse_thickness.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["scale(0.5)", "rotateX(90)"]
    }
],
"camera_position": [18, 43, 19],
"settings": {
    "support_enable": true,
    "support_infill_sparse_thickness": 0.24
},
"layer": 148,
"colours": 64
}-->
![El grosor de la capa de relleno de soporte es tres veces la altura de la capa](../images/support_infill_sparse_thickness.png)

El grosor de la capa de relleno del soporte debe ser un múltiplo de la altura de la capa ordinaria. Si no lo es, se redondeará a la altura de capa más cercana.

Este ajuste no se aplica al techo o al suelo del soporte, sólo a la estructura principal del mismo.

Este ajuste es especialmente útil cuando se imprime el soporte con un material diferente al del resto de la impresión, y más aún cuando ese material es difícil de extruir, como el PVA. Como el soporte no se extruye en cada capa, la impresora no tendrá que cambiar de extrusor tan a menudo, lo que ahorra mucho tiempo. Como se extruye más material en las capas que se imprimen, los materiales que tardan en iniciar el flujo se imprimirán de forma más fiable.

Tenga cuidado con aumentar esto demasiado. Cuando se cambia a y desde el soporte, el flujo a través de la boquilla necesita acelerar y desacelerar significativamente. Hay un cierto retraso en esto, por lo que extruirá muy poco al principio del soporte y demasiado al final del mismo.