Escalones de relleno de soporte
====
El soporte gradual reduce la cantidad de material de soporte utilizado, reduciendo la densidad de soporte en las capas inferiores. Esto ahorra tiempo y material de impresión, pero no reduce mucho la calidad del voladizo. El propósito principal del soporte es apoyar las áreas que sobresalen. Esta función centra el soporte únicamente en ese propósito.

Este ajuste indica en cuántos pasos se reduce la densidad del soporte. En cada paso, la densidad del soporte se reduce a la mitad. Por ejemplo, partiendo de una densidad del 20% y dos pasos graduales de apoyo, la densidad de apoyo de las partes inferiores será del 10% y del 5% respectivamente.

<!--screenshot {
"image_path": "gradual_support_infill_step_height_1mm.png",
"models": [
    {
        "script": "stair.scad",
        "transformation": ["rotateY(-90)", "scaleZ(0.5)"]
    }
],
"camera_position": [49, 91, -38],
"settings": {
    "support_enable": true,
    "support_pattern": "grid",
    "support_wall_count": 0,
    "support_infill_rate": 50,
    "gradual_support_infill_steps": 3,
    "gradual_support_infill_step_height": 1
},
"colours": 64
}-->
![El soporte se reduce a una menor densidad en 3 pasos](../images/gradual_support_infill_step_height_1mm.png)

El aumento del número de pasos hace que la densidad se reduzca cada vez más a la mitad, dando lugar a un soporte de menor densidad. Esto ahorra mucho material y tiempo de impresión, pero hará que el soporte sea más débil.

Parte del soporte quedará flotando en el aire. Sin embargo, en la práctica, con la mayoría de los patrones de soporte, esto se reparará rápidamente, ya que las capas pueden acumularse adecuadamente incluso en las capas inferiores debilitadas. La intención de la [Altura necesaria de los escalones de relleno de soporte](gradual_support_infill_step_height.md) es dejar tiempo suficiente para que las capas se reparen por sí solas antes de apilar el siguiente escalón de soporte gradual.

Este ajuste se combina mejor con al menos una [Línea de pared de soporte](support_wall_count.md). Esto da a las líneas de soporte algo a lo que agarrarse, en lugar de estar suspendidas en el aire.