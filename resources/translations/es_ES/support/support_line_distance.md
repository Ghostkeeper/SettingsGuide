Distancia de la línea de soporte
====
Este ajuste define la distancia entre dos líneas adyacentes en el patrón de soporte. Esta forma de ajustar la densidad de soporte puede ser más intuitiva que el ajuste de la densidad de soporte, ya que ajusta directamente la distancia que deben salvar las líneas de soporte.

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
![Distancia de línea grande](../images/support_infill_rate_low.png)
![Distancia entre líneas pequeña](../images/support_infill_rate_high.png)

Reducir la distancia entre las líneas de soporte tiene algunos efectos positivos y negativos. Estos son algunos de los efectos que hay que sopesar:
* La superficie que se apoya sobre este soporte se combará menos, porque tiene que salvar una distancia menor entre dos líneas de soporte.
* El soporte será más fuerte, mejorando la fiabilidad de la impresión.
* Es más difícil retirar el soporte debido a la mayor superficie de adherencia.
* Se necesitará más material para imprimir el soporte.
* La impresión tardará más en completarse.