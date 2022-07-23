Extrusor del relleno del soporte
====
Si su impresora tiene varios extrusores, el cuerpo principal del soporte puede imprimirse con un extrusor diferente al de la interfaz del soporte. Este ajuste le permite elegir qué extrusor se utiliza para el cuerpo principal del soporte.

<!--screenshot {
"image_path": "support_infill_extruder_nr.png",
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
    "support_infill_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![El cuerpo del soporte se imprime en rojo, pero la interfaz en blanco](../images/support_infill_extruder_nr.png)

Algunos materiales son más adecuados para imprimir soportes que otros, pero esos materiales también pueden ser más caros o más lentos de imprimir. Imprimir sólo la interfaz con el material caro pero la mayor parte del cuerpo con un material más barato puede ahorrar mucho tiempo y dinero. La interfaz seguirá imprimiéndose con el material caro, por lo que la parte que toca el modelo tendrá un buen aspecto o será más fácil de romper, pero la mayor parte del soporte se imprimirá con materiales más baratos.

Si está utilizando materiales solubles para imprimir la interfaz del soporte, pero materiales insolubles para imprimir el cuerpo del soporte, tenga en cuenta que el cuerpo puede no ser capaz de ser retirado de las cavidades si es físicamente imposible mover el cuerpo del soporte a través de una pequeña abertura. Donde normalmente un material soluble puede fluir a través de una cavidad en solución, los materiales insolubles pueden no ser capaces de pasar.