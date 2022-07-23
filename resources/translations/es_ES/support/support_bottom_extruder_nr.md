Extrusor del suelo del soporte
====
Si su impresora tiene múltiples extrusores, la parte inferior del soporte, donde el soporte se apoya en el modelo, puede imprimirse con un extrusor diferente al del techo del soporte, donde el modelo se apoya en el soporte. Este ajuste le permite elegir qué extrusor se utiliza para el suelo del soporte.

<!--screenshot {
"image_path": "support_bottom_extruder_nr.png",
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
    "support_bottom_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![El suelo del soporte está impreso en rojo, pero el techo del soporte en blanco](../images/support_bottom_extruder_nr.png)

Algunos materiales ofrecen mejores propiedades de voladizo que otros materiales cuando se utilizan como soporte. Por ejemplo, pueden imprimir más cerca de la superficie porque no se adhieren químicamente a ella, o son solubles en agua. Sin embargo, estos materiales suelen ser caros y tardan más en imprimirse. Esta configuración le permite imprimir el fondo del soporte con un extrusor diferente. Esto puede ahorrar parte del material caro o de impresión lenta.

El suelo del soporte es menos importante que el techo del soporte para la calidad de los voladizos. Si se va a utilizar un material caro con moderación, el suelo del soporte es un buen candidato para imprimir con el material más barato.