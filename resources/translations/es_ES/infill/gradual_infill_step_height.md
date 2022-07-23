Altura del escalón de relleno gradual
====
Cuando se utiliza el relleno gradual, la densidad del relleno se reduce de arriba a abajo en varios pasos. En cada paso, la densidad del relleno se reduce a la mitad. Este ajuste indica la altura de estos pasos, la distancia entre dos lugares donde el relleno se reduce a la mitad.

<!--screenshot {
"image_path": "gradual_infill_step_height_small.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
    "wall_line_count": 0,
    "bottom_layers": 0,
    "gradual_infill_steps": 3,
    "gradual_infill_step_height": 1.5
},
"colours": 16
}-->
<!--screenshot {
"image_path": "gradual_infill_step_height_large.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
    "wall_line_count": 0,
    "bottom_layers": 0,
    "gradual_infill_steps": 3,
    "gradual_infill_step_height": 5
},
"colours": 16
}-->
![Altura del escalón de relleno gradual de 1,5 mm](../images/gradual_infill_step_height_small.png)
![Altura del escalón de relleno gradual de 5 mm](../images/gradual_infill_step_height_large.png)

El Relleno Gradual, por su naturaleza, suspenderá parte del relleno en el aire. Sin embargo, esto normalmente se repara automáticamente. La primera capa de relleno colgará en el aire y sólo se adherirá a los lados de la impresión correctamente. Las capas colocadas encima pueden apoyarse un poco en la capa anterior en los extremos, pero seguirán colgando en el centro. Esto mejora gradualmente, capa por capa.

* Reduzca el tamaño del paso de relleno gradual para descender rápidamente a una densidad de relleno baja. Esto ahorra tiempo de impresión y uso de material.
* Aumente el Tamaño del Paso de Relleno Gradual si el relleno no va a tener suficiente espacio para repararse por sí mismo para cuando se produzca el siguiente paso en la densidad de relleno. Aumentar el valor de este ajuste hace que la impresión sea más fiable.