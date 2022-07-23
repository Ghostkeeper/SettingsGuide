Extrusor de la interfaz de soporte
====
Si su impresora tiene varios extrusores, las capas de interfaz donde el soporte toca el modelo pueden imprimirse con un extrusor diferente al del cuerpo principal del soporte. Este ajuste le permite elegir qué extrusor se utiliza para la interfaz del soporte.

<!--screenshot {
"image_path": "support_interface_extruder_nr.png",
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
    "support_extruder_nr": 3,
    "support_interface_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![La interfaz de soporte se imprime en rojo, pero el cuerpo principal en blanco](../images/support_interface_extruder_nr.png)

Algunos materiales son más adecuados que otros para la impresión de soportes. Por ejemplo, es posible que no se adhieran químicamente al material de impresión y que sea más fácil romperlos, o que se disuelvan en agua o alcohol. Sin embargo, estos materiales suelen ser caros y tardan más en imprimirse. Esta configuración te permite imprimir la interfaz de soporte con un extrusor diferente al del cuerpo principal, de modo que la mayor parte del soporte sigue imprimiéndose rápidamente y/o con materiales más baratos, pero las ventajas del material de soporte especializado siguen siendo efectivas.

Si está utilizando materiales solubles para imprimir la interfaz del soporte, pero materiales insolubles para imprimir el cuerpo del soporte, tenga en cuenta que el cuerpo puede no ser capaz de ser retirado de las cavidades si es físicamente imposible mover el cuerpo del soporte a través de una pequeña abertura. Donde normalmente un material soluble puede fluir a través de una cavidad en solución, los materiales insolubles pueden no ser capaces de pasar.