Altura del escalón de la escalera del soporte
====
Si [Colocación del soporte](support_type.md) está ajustado a "En todas partes", se permite que el soporte se apoye en el modelo. Sin embargo, no seguirá exactamente los contornos del modelo. En su lugar, la parte inferior del soporte recibe un patrón de escalonamiento. De este modo, el soporte sólo se une al modelo en unos pocos lugares.

Este ajuste determina la altura de estos escalones.

<!--screenshot {
"image_path": "support_bottom_stair_step_height.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"settings": {
    "support_enable": true,
    "support_bottom_stair_step_height": 1
},
"colours": 64
}-->
![Formación de peldaños en la parte inferior del soporte](../images/support_bottom_stair_step_height.png)

La altura de los peldaños se cuenta por la distancia desde la superficie del modelo. Esto significa que si tiene una distancia vertical establecida en el ajuste [Distancia inferior del soporte](support_bottom_distance.md), ésta se resta de la altura y la conexión entre el modelo y el soporte será mayor. Del mismo modo, el ajuste [Suelo del soporte](support_bottom_enable.md) también hace que se reduzca el efecto de los peldaños de la escalera.

El ajuste [Ancho máximo de los peldaños del soporte](support_bottom_stair_step_width.md) limita el ancho de los peldaños. Si la superficie del modelo es tan poco profunda que una pequeña altura de peldaño supondría una gran anchura de peldaño, el soporte seguirá la superficie del modelo durante el resto de la altura del peldaño.

Si se reduce este ajuste, la parte inferior del soporte será más suave. Esto aumenta la adherencia entre el soporte y el modelo, dificultando la retirada del soporte pero también haciendo que el soporte sea más estable.