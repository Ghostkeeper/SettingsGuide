Ancho de línea de interfaz de soporte
====
El ancho de las líneas de interfaz de soporte pueden configurarse por separado de los anchos del resto de las líneas de soporte.

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
![Las líneas de la interfaz de soporte son más anchas que el resto de las líneas de soporte](../images/support_roof_line_width.png)

La impresión de la interfaz de soporte con líneas ligeramente más finas es a menudo ventajosa para la calidad de la superficie sobresaliente que soporta, puramente por tener una superficie superior más suave por encima de la interfaz de soporte. Sin embargo, no aumenta necesariamente la adherencia entre la interfaz de soporte y el modelo, por lo que el soporte no será necesariamente más difícil de eliminar.

Del mismo modo, el suelo del soporte se pegará más uniformemente, reduciendo las cicatrices donde el soporte se apoyaba en el modelo sin que el soporte sea más débil.

Sin embargo, si se imprimen las líneas de interfaz demasiado finas, se producirá una extrusión desigual, lo que reduce el efecto de soporte de la interfaz, provocando una peor calidad del voladizo y un soporte menos estable. También puede introducir un gran cambio en la velocidad de flujo a través de la boquilla, causando sobreextrusión cuando comienza a imprimir la interfaz de soporte y subextrusión cuando imprime lo que viene después de la interfaz de soporte.