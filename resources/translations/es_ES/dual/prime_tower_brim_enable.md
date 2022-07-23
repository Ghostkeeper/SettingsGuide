Borde de la torre de purga
====
El borde de la torre de purga es un borde adicional, similar a la opción de borde en el [Tipo de adhesión de la placa de construcción] (../platform_adhesion/adhesion_type.md). Este borde se puede activar y desactivar por separado de la adhesión ordinaria. Cuando se activa, se imprime un borde adicional alrededor de la torre de purga. Este borde es un disco plano alrededor de la torre de purga de una sola capa que mejora la adhesión de la torre de purga a la placa de construcción.

<!--screenshot {
"image_path": "prime_tower_brim_enable.png",
"models": [
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 0
        }
    },
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 1
        },
        "transformation": ["translateX(40)"]
    }
],
"camera_position": [50, -32, 133],
"camera_lookat": [93, -122, 5],
"settings": {
    "prime_tower_enable": true,
    "prime_tower_brim_enable": true,
    "prime_tower_position_x": 600,
    "prime_tower_position_y": 600,
    "adhesion_type": "skirt"
},
"colours": 16
}-->
La adherencia está ajustada a falda, pero todavía hay un borde alrededor de la torre de purga](../images/prime_tower_brim_enable.png)

Activar el borde de la torre de purga dará a la torre de purga más superficie para conectarse a la placa de construcción. Debido a que la torre principal puede llegar a ser bastante alta y delgada, puede volcarse en impresiones muy altas. Este borde de la torre de purga está destinada a evitar eso con un pequeño coste de tiempo de impresión, material y espacio en la placa de construcción.

El borde de la torre de purga tendrá la anchura definida en el ajuste [Brim Width](../platform_adhesion/brim_width.md). Si el tipo de adhesión de la placa de construcción se establece en Brim, este ajuste duplica efectivamente la anchura del borde alrededor de la torre de purga.

El borde de la torre de purga no puede combinarse con una balsa.