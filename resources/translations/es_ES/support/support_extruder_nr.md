Extrusor del soporte
====
Si su impresora tiene varios extrusores, este ajuste le permite elegir cuál de estos extrusores se utiliza para imprimir la estructura de soporte.

<!--screenshot {
"image_path": "support_extruder_nr.png",
"models": [
    {
        "script": "question_stick_clip.scad",
        "transformation": ["rotateY(90)"],
        "object_settings": {"extruder_nr": 1}
    }
],
"camera_position": [134, 134, 113],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_use_towers": false,
    "support_extruder_nr": 3
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![El soporte está impreso en un material blanco, mientras que el modelo está impreso en azul](../images/support_extruder_nr.png)

El uso de un tipo de material diferente tiende a hacer que el soporte sea más fácil de quitar sin comprometer la fuerza del soporte. Los diferentes tipos de material no se adhieren muy bien entre sí, especialmente si tienen diferentes tasas de contracción.

Además, algunos materiales están diseñados para imprimir el soporte. Por ejemplo, pueden hacerse extremadamente frágiles a propósito, para que se rompan más fácilmente. Algunos materiales se disuelven en agua o en etanol, por lo que se puede quitar el soporte incluso si se imprime muy cerca del modelo.

Sin embargo, imprimir el soporte con un extrusor diferente al del resto del modelo requiere que la impresora cambie de material en cada capa, lo que podría aumentar el tiempo de impresión. Si el material de soporte tiene un color diferente al del material de impresión, el residuo de soporte en la impresión podría ser muy visible.