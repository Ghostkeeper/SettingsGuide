Torre de Purga Circular
====
Si esta opción está activada, la torre de purga tendrá la forma de un cilindro. Si está desactivado, la torre de purga tendrá forma cuadrada.

<!--screenshot {
"image_path": "prime_tower_circular_enabled.png",
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
"camera_position": [470, -384, 150],
"camera_lookat": [470, -470, 5],
"settings": {
    "prime_tower_enable": true,
    "prime_tower_min_volume": 3
},
"colours": 16
}-->
![Square prime tower](../images/prime_tower_circular_disabled.png)
![Circular prime tower](../images/prime_tower_circular_enabled.png)

En cualquier caso, la torre de purga sigue siendo hueca. La torre de purga circular es estrictamente más pequeña que la torre de purga cuadrada (ya que las esquinas están cortadas). El [volumen mínimo] (prime_tower_min_volume.md) seguirá siendo correcto.

Si el material tiene tendencia a deformarse, la torre de purga cuadrada tiene cuatro esquinas que pueden soltarse de la placa de construcción. Esto hace que sea más probable que se vuelque, en comparación con la torre de imprimación circular. También hay mayores aceleraciones en la impresión de una torre de imprimación cuadrada. Estas aceleraciones hacen que la tasa de flujo sea inconsistente, lo cual no es lo que se desea para cebar el material.

La torre de purga circular es mejor en casi todos los aspectos. Por eso se ha eliminado el ajuste en las nuevas versiones de Cura. Estas versiones siempre tendrán una torre de imprimación circular.