Ancho máximo del escalón de la escalera del soporte
====
Si [Colocación del soporte](support_type.md) está ajustado a "En todas partes", se permite que el soporte se apoye en el modelo. Sin embargo, no seguirá exactamente los contornos del modelo. En su lugar, la parte inferior del soporte recibe un patrón de escalonamiento. De este modo, el soporte sólo se une al modelo en unos pocos lugares.

Este ajuste determina la anchura máxima de estos escalones. El escalón normalmente obtiene una anchura que sigue la superficie del modelo con un valor dado de [Altura del escalón de la escalera de soporte](support_bottom_stair_step_height.md). Sin embargo, si esto es demasiado ancho, el ancho se limita a la anchura máxima del escalón de soporte. Entonces sigue la superficie del modelo para el resto del escalón.

<!--screenshot {
"image_path": "support_bottom_stair_step_width.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"settings": {
    "support_enable": true,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_width": 0.7
},
"colours": 64
}-->
![Peldaños de escalera limitados en anchura, haciendo que el soporte siga el modelo](../images/support_bottom_stair_step_width.png)

Este ajuste debe establecerse normalmente a la distancia máxima que puede salvar el material sin comprometer la estabilidad de las líneas de soporte por encima de él. Bajar el ajuste hace que el soporte siga al modelo más a menudo, haciendo que el soporte sea más estable. Aumentar el ajuste hace que el soporte se adhiera al valor establecido para la altura del escalón de soporte más a menudo, haciendo que el soporte sea más fácil de quitar del modelo.