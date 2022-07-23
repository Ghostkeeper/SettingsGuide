Área del soporte mínima
====
Este ajuste impone un tamaño mínimo permitido para las piezas de soporte. Si un trozo de soporte tiene un área menor que el valor de este ajuste en una determinada capa, el soporte se deja fuera de ella.

<!--screenshot {
"image_path": "minimum_support_area_0.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 190, 47],
"settings": {
    "support_enable": true,
    "minimum_support_area": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "minimum_support_area_10.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 190, 47],
"settings": {
    "support_enable": true,
    "minimum_support_area": 10
},
"colours": 64
}-->
![No se filtra el área (el área mínima es 0)](../images/minimum_support_area_0.png)
![Se omiten las piezas pequeñas de soporte](../images/minimum_support_area_10.png)

Este ajuste existe porque los pilares de soporte delgados son propensos a volcarse. También tienden a soportar pequeñas características que probablemente se imprimirían bien sin soporte. Si el soporte se derrumba, quedarán muchas manchas en la impresión. Por lo tanto, puede ser mejor dejar estos pilares delgados fuera. Este ajuste proporciona una manera de filtrar el soporte por el área de la sección transversal del pilar.

Aumentando el área se reduce la cantidad de soporte impreso, reduciendo ligeramente el tiempo y el uso de material. Más importante aún, mejora la fiabilidad de la impresión ya que hay menos posibilidades de que los pilares de apoyo se vuelquen. Sin embargo, también se eliminará el apoyo a las pequeñas características en su impresión, por lo que la calidad de voladizo puede empeorar para esas piezas.

Para algunas formas esto puede tener el desagradable efecto secundario de eliminar la parte superior del soporte si la parte superior cae por debajo del área del umbral pero la parte inferior no. Esto puede dejar sin soporte partes que normalmente se esperaría que estuvieran soportadas.

<!--screenshot {
"image_path": "minimum_support_area_problem.png",
"models": [{"script": "overhang_bridging_cooling.scad"}],
"camera_position": [117, 0, 15],
"settings": {
    "support_enable": true,
    "minimum_support_area": 50
},
"colours": 64
}-->
![El extremo del arco no tiene soporte porque el área de esas capas es demasiado pequeña](../images/minimum_support_area_problem.png) 