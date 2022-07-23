Densidad de soporte
====
Este ajuste define la velocidad de llenado de las estructuras de soporte. Con un alto índice de relleno, las líneas de soporte se colocarán muy juntas. Con una tasa de relleno baja, las líneas se colocarán más separadas.

<!--screenshot {
"image_path": "support_infill_rate_low.png",
"models": [{"script": "spiral_stair.scad"}],
"camera_position": [-95, 18, 116],
"settings": {
    "support_enable": true,
    "support_infill_rate": 10
},
"layer": 256,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_rate_high.png",
"models": [{"script": "spiral_stair.scad"}],
"camera_position": [-95, 18, 116],
"settings": {
    "support_enable": true,
    "support_infill_rate": 20
},
"layer": 256,
"colours": 64
}-->
![Densidad de soporte baja](../images/support_infill_rate_low.png)
![Densidad de soporte alta](../images/support_infill_rate_high.png)

El aumento de la densidad de soporte tiene algunos efectos positivos y negativos. Estos son algunos de los efectos que hay que sopesar:
* Como la distancia entre las líneas de soporte es menor, la superficie que se apoya sobre este soporte se combará menos.
* El soporte será más fuerte, mejorando la fiabilidad de la impresión.
* Es más difícil quitar el soporte debido a la mayor superficie de adherencia.
* Se necesitará más material para imprimir el soporte.
* La impresión tardará más tiempo en completarse.