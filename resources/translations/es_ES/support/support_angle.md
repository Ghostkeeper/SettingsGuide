Ángulo de voladizo del soporte
====
El ángulo de voladizo influye en la cantidad de material que se coloca hacia abajo para soportar la impresión. El ángulo indica el ángulo mínimo que recibe soporte.

**Reducir el valor de este ajuste genera más soporte.**

<!--screenshot {
"image_path": "support_angle_low.png",
"models": [{"script": "duct.scad"}],
"camera_position": [136, 10, 10],
"camera_lookat": [0, 10, 10],
"settings": {
    "support_enable": true,
    "support_join_distance": 0.1,
    "support_angle": 40
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_angle_high.png",
"models": [{"script": "duct.scad"}],
"camera_position": [136, 10, 10],
"camera_lookat": [0, 10, 10],
"settings": {
    "support_enable": true,
    "support_join_distance": 0.1,
    "support_angle": 75
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_angle_prepare_mode.png",
"models": [{"script": "duct.scad"}],
"camera_position": [113, 77, 0],
"layer": -1
}-->
![Un ángulo de voladizo bajo genera más apoyo](../imágenes/ángulo_de_apoyo_bajo.png)
![Un ángulo de voladizo alto genera menos apoyos](../images/ángulo_de_apoyo_alto.png)
![Las áreas soportadas se indican en rojo](../images/support_angle_prepare_mode.png)

La reducción de este ajuste hace que la impresora soporte una mayor parte de la pieza impresa, incluso las superficies más inclinadas y que no se comben mucho durante la impresión. Si el soporte está apoyando partes que no necesitan ser apoyadas, aumentará el tiempo de impresión y el uso de material innecesariamente y también creará cicatrices donde el soporte tocó la impresión.

Sin embargo, reducir el ángulo del soporte es a veces necesario para evitar que el material se hunda demasiado. Por lo general, mejora la precisión dimensional de la pieza final y también hace que los voladizos tengan mejor aspecto.

Siempre que se trabaje con el soporte, es una buena idea previsualizar el aspecto del soporte en la fase de Vista Previa. Allí podrá ver dónde se generará realmente el soporte. El ajuste de esta configuración es una de las herramientas a su disposición para filtrar dónde se generará el apoyo de forma precisa.