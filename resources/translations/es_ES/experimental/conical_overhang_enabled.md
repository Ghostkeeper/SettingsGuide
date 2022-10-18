Convertir voladizo en imprimible
====
Este ajuste transformará su modelo de manera que ya no tenga ningún voladizo. Colocará material extra debajo de cualquier saliente y lo imprimirá como si fuera parte del modelo.

<!--screenshot {
"image_path": "conical_overhang_enabled_disabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 189, 25],
"settings": {
    "conical_overhang_enabled": false
},
"colours": 8
}-->
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
![Una torre con algunas piezas que sobresalen](../images/conical_overhang_enabled_disabled.png)
![El voladizo se hace imprimible](../images/conical_overhang_enabled_enabled.png)

Debajo de todas las piezas que sobresalen se coloca un material que se va haciendo más pequeño hacia abajo. En muchos casos el voladizo estará inclinado hacia el propio objeto. La pendiente con la que se hace crecer el voladizo hacia el objeto está determinada por el [ángulo del modelo](conical_overhang_angle.md).

Este ajuste puede ser una forma fácil de evitar que se necesite un soporte. Es especialmente eficaz cuando se imprimen modelos con superficies algo rugosas o con relieve en los laterales. Esos pequeños trozos de voladizo normalmente caerían y producirían hilos sueltos de plástico desconectados. Podrían apoyarse con algún soporte, pero esto puede ser costoso en tiempo de impresión y seguirá dejando algunas cicatrices. Si se activa este ajuste, el voladizo se suavizará hacia el modelo. Parecerá que así es como se pretendía imprimir.

Si el saliente sobresale del cuerpo principal más allá de su anchura, puede que siga produciendo algún saliente en forma de línea. Esto ocurre porque la protuberancia se encoge entonces infinitamente, haciendo que desaparezca. Si esto ocurre, puede considerar si todavía es necesario imprimir el soporte. En el caso de las imágenes anteriores, esto sucede con los pequeños bloques del lateral de la torre, pero es tan pequeño que un simple puente probablemente permitirá que sobresalga sin problemas.