Colocación del soporte
====
Este ajuste permite elegir el soporte que se puede colocar encima.

<!--screenshot {
"image_path": "support_type_everywhere.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
    "support_enable": true,
    "support_type": "everywhere"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "support_type_touching_buildplate.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
    "support_enable": true,
    "support_type": "buildplate"
},
"colours": 32
}-->
![El soporte se genera para todas las superficies que sobresalen](../images/support_type_everywhere.png)
![El soporte sólo se genera donde puede apoyarse en la placa de impresión](../images/support_type_touching_buildplate.png)

Colocar el soporte en todas partes es más fiable para el soporte. Todos los voladizos que se comben se soportan correctamente. Sin embargo, el soporte puede apoyarse también en la parte superior del modelo, dejando una cicatriz donde toca. Esto reduce la calidad visual y la suavidad de la superficie del modelo después de retirar el soporte.

En cambio, colocar el soporte sólo si toca la placa de impresión evita que el soporte descanse sobre el modelo. Sin embargo, esto puede dejar algunas partes de su modelo sin soporte.

**Como truco cuando se utiliza el soporte sólo en la placa de impresión, pruebe a [habilitar el soporte cónico](../experimental/support_conical_enabled.md) y dar al [Ángulo de soporte cónico](../experimental/support_conical_angle.md) un valor negativo. Esto permite que el soporte crezca alrededor del modelo y siga soportando la mayor parte de la malla sin apoyarse en el modelo. Como alternativa, pruebe el soporte de árbol.**