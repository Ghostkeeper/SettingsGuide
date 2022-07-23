Distancia de la línea de soporte de la capa inicial
====
La densidad del patrón con el que se imprime la primera capa de soporte se puede ajustar por separado de la densidad del resto del soporte. Este ajuste configura la distancia entre dos líneas adyacentes donde el soporte se apoya en la placa de impresión.

<!--screenshot {
"image_path": "support_initial_layer_line_distance.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 64, 125],
"settings": {
    "support_enable": true,
    "support_initial_layer_line_distance": 1.333
},
"layer": 160,
"colours": 64
}-->
El patrón de la primera capa es dos veces más denso que el resto del soporte](../images/support_initial_layer_line_distance.png)

Este ajuste es útil para mejorar la adherencia entre el soporte y la placa de impresión. Si el patrón de soporte es más denso en la primera capa, aumentará el área de contacto entre el soporte y la placa de impresión, haciendo que se adhiera mejor. Las capas siguientes pueden entonces colocarse sobre un material al que se adhieren mejor.

Como este ajuste sólo afecta a la primera capa, no afecta significativamente a la resistencia del soporte ni al tiempo y coste del material. Tampoco afecta a la calidad de los voladizos. Para ajustar la densidad del soporte cerca de los voladizos, mire el ajuste [Distancia de la línea del techo del soporte](support_roof_line_distance.md).

Es una buena idea hacer que este ajuste sea un múltiplo de la distancia de la línea del cuerpo principal del soporte. De esta manera, las líneas de soporte coincidirán con las líneas de la primera capa, permitiendo que se apoyen en la primera capa en lugar de flotar en el aire.