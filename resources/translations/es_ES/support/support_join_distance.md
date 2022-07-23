Distancia de unión del soporte
====
Los soportes finos no suelen ser deseables. Son propensos a volcarse, lo que puede arruinar la impresión. Cuando hay varias piezas de soporte adyacentes, se pueden unir, formando una pieza de soporte mucho más resistente.

<!--screenshot {
"image_path": "support_join_distance_low.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 150, 75],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_join_distance": 0.1
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_join_distance_high.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 150, 75],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_join_distance": 2
},
"colours": 64
}-->
![Dos piezas de soporte están muy juntas](../images/support_join_distance_low.png)
![Con una distancia de unión suficiente, se unen](../images/support_join_distance_high.png)

Unir las piezas de soporte hace que el soporte sea más resistente y fiable. También tiende a reducir el tiempo de impresión, dependiendo del patrón. Muchos patrones requieren que se imprima una pared extra alrededor de todo el perímetro o parte de él, y unir dos piezas de soporte reduce ese perímetro.

Aumentar demasiado este ajuste puede hacer que se unan piezas de soporte que están muy alejadas. Esto puede aumentar el tiempo de impresión y el uso de material.