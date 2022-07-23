Anchura de expansión mínima del forro
====
Dado que el forro está presente en todo el modelo, no es necesario expandir todas esas áreas. En su lugar, sólo se expandirán los ángulos de piel que ya son más anchos que este ajuste. De esta manera, las superficies planas con elementos que sobresalen serán reforzadas, sin aumentar innecesariamente el tiempo de impresión para el resto del modelo.

<!--screenshot {
"image_path": "max_skin_angle_for_expansion_90.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "expand_skins_expand_distance": 3,
    "max_skin_angle_for_expansion": 89
},
"colours": 64
}-->
<!--screenshot {
"image_path": "max_skin_angle_for_expansion_45.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "expand_skins_expand_distance": 3,
    "max_skin_angle_for_expansion": 45
},
"colours": 64
}-->
![Si se ajusta a 0 mm, todo el forro se expande con la configuración de la distancia de expansión del forro] (../images/max_skin_angle_for_expansion_90.png)
![Si se ajusta a 0,8 mm, sólo se expanden las zonas planas](../images/max_skin_angle_for_expansion_45.png)

Expandir el forro es útil para reforzar la conexión entre la parte superior o inferior de la impresión y las paredes de los lados. Sin embargo, también puede aumentar mucho el tiempo de impresión y el uso de material. Este ajuste le permite filtrar el material de los lados de la impresión donde es menos útil para reforzar la conexión entre las paredes y el forro.

También puede configurar este ajuste con el ajuste [Ángulo de expansión máximo del forro](max_skin_angle_for_expansion.md). Si ese ajuste se cambia, este ajuste cambiará automáticamente. Este ajuste es el que se utiliza realmente para el corte.