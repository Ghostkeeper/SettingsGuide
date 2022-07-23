Ángulo máximo del modelo
====
Con este ajuste se configura el ángulo del voladizo (en grados) que se produce para [hacer imprimible el voladizo](conical_overhang_enabled.md). Aumentar este ángulo permite un mayor voladizo, haciendo que Cura modifique menos el modelo. Reducir este ángulo hace que el objeto apenas sobresalga.

<!--screenshot {
"image_path": "conical_overhang_enabled_enabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
    "conical_overhang_enabled": true,
    "conical_overhang_angle": 50
},
"colours": 8
}-->
<!--screenshot {
"image_path": "conical_overhang_angle_20.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
    "conical_overhang_enabled": true,
    "conical_overhang_angle": 20
},
"colours": 8
}-->
![Un ángulo máximo del modelo de 50°](../images/conical_overhang_enabled_enabled.png)
![Un ángulo máximo del modelo de 20°](../images/conical_overhangle_20.png)

Un ángulo de 90° dejará el modelo como estaba con todo su voladizo. El modelo no será alterado. Un ángulo de 0° hará que todos los voladizos sean completamente verticales.

Reduciendo este ángulo se reduce el voladizo en el modelo. Esto permite que el modelo se imprima mejor. No se combará tanto y, por tanto, la superficie de los lados inferiores será más suave. Sin embargo, también hará que el objeto impreso sea menos fiel al modelo original. También se necesitará algo más de tiempo y material para imprimirlo.

El ángulo también puede ser negativo. Esto hace que toda la impresión sea cónica con una base ancha. Esto puede producir efectos interesantes, pero no tiene ninguna utilidad práctica real.