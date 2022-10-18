Ancho de línea del techo de soporte
====
El ancho de las líneas de techo de apoyo se pueden configurar por separado del ancho del resto de las líneas de apoyo.

<!--screenshot {
"image_path": "support_roof_line_width.png",
"models": [
    {
        "script": "trash_bin_lid.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [-47, 79, 110],
"settings": {
    "support_enable": true,
    "support_roof_enable": true,
    "support_roof_line_width": 0.8
},
"layer": 192,
"colours": 64
}-->
![Las líneas del techo de soporte son más anchas que el resto de las líneas de soporte](../images/support_roof_line_width.png)

Imprimir el techo de soporte con líneas ligeramente más finas es a menudo ventajoso para la calidad de la superficie sobresaliente que soporta, puramente por tener una superficie superior más suave sobre la interfaz de soporte. Sin embargo, no aumenta necesariamente la adherencia entre la interfaz del soporte y el modelo, por lo que el soporte no será necesariamente más difícil de eliminar.

Sin embargo, si se imprimen las líneas del techo demasiado finas, se producirá una extrusión desigual, lo que reduce el efecto de soporte del techo, provocando una peor calidad del voladizo. También puede introducir un gran cambio en la velocidad de flujo a través de la boquilla, provocando una sobreextrusión cuando se empieza a imprimir el techo de soporte y una subextrusión cuando se imprime lo que viene después del techo de soporte.