Extrusor del soporte de la primera capa
====
Si su impresora tiene varios extrusores, la capa de soporte que se apoya en la placa de impresión puede imprimirse con un extrusor diferente al del resto del soporte. Este ajuste le permite elegir qué extrusor se utiliza para la capa inicial del soporte.

<!--screenshot {
"image_path": "support_extruder_nr_layer_0.png",
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
    "support_extruder_nr_layer_0": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![La capa inicial del soporte se imprime en rojo, pero el resto en blanco](../images/support_extruder_nr_layer_0.png)

Algunos materiales son más adecuados que otros para la impresión de soportes. Suelen ser materiales inertes que no se adhieren bien a otros materiales, por lo que se pueden eliminar más fácilmente. Sin embargo, esta propiedad no es deseable para pegarse a la placa de impresión. Un material que se adhiere mejor a la placa de impresión puede ser utilizado para la primera capa, a la que el material de soporte normal puede adherirse mejor que al vidrio o al aluminio.