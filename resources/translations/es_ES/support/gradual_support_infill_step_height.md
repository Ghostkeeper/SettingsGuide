Altura necesaria de los escalones de relleno de soporte
====
Cuando se utiliza el apoyo gradual, la densidad del apoyo se reduce periódicamente de arriba a abajo en varios pasos. En cada paso, la densidad del soporte se reduce a la mitad. Este ajuste indica la altura de estos pasos, la distancia entre dos lugares donde la densidad del soporte se reduce a la mitad.

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
<!--screenshot {
"image_path": "gradual_support_infill_step_height_3mm.png",
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
    "gradual_support_infill_step_height": 3
},
"colours": 64
}-->
![Altura de escalón de 1 mm](../images/gradual_support_infill_step_height_1mm.png)
![Altura de escalón de 3 mm](../images/gradual_support_infill_step_height_3mm.png)

El soporte gradual, por su naturaleza, suspenderá parte del apoyo en el aire. Sin embargo, esto normalmente se repara automáticamente. La primera capa de soporte colgará en el aire y sólo se sujetará a los lados del soporte correctamente. Las capas superiores pueden apoyarse un poco en la capa anterior en los extremos, pero se hundirán en el centro. Esto mejora gradualmente, capa a capa. Si la altura del escalón de apoyo gradual es lo suficientemente grande, el apoyo es adecuadamente resistente para cuando se produce el siguiente escalón de densidad.

Reduzca la altura del paso de soporte gradual para descender rápidamente a una densidad de soporte baja. Esto ahorra tiempo de impresión y uso de material. Aumente la altura del paso de relleno del soporte gradual si el soporte no tiene suficiente espacio para repararse cuando se produzca el siguiente paso de densidad del soporte. Aumentar el valor de este ajuste hace que la impresión sea más fiable.