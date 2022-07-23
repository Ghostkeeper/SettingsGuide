Extrusor para el techo del soporte
====
Si su impresora tiene varios extrusores, la parte superior del soporte, donde el modelo se apoya en el soporte, puede imprimirse con un extrusor diferente al del suelo del soporte, donde el soporte se apoya en el modelo. Este ajuste le permite elegir qué extrusor se utiliza para el techo del soporte.

<!--screenshot {
"image_path": "support_roof_extruder_nr.png",
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
    "support_roof_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![El techo de soporte está impreso en rojo, pero el suelo del soporte en blanco](../images/support_roof_extruder_nr.png)

Algunos materiales ofrecen mejores propiedades de voladizo que otros materiales cuando se utilizan como soporte. Por ejemplo, pueden imprimir más cerca de la superficie porque no se adhieren químicamente a ella, o son solubles en agua. Sin embargo, estos materiales suelen ser caros y tardan más en imprimirse. Esta configuración le permite imprimir el techo del soporte con un extrusor diferente al del suelo del soporte. De esta manera, el material caro o lento se utiliza con moderación, pero sigue siendo eficaz para crear buenos voladizos.

El techo de soporte es más importante que el suelo del soporte para la calidad de los voladizos, por lo que si un material caro debe ser utilizado con moderación, es mejor utilizarlo al menos para el techo de soporte.