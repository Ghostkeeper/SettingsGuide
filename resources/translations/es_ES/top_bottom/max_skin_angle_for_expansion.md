Ángulo máximo de expansión del forro
====
Dado que el forro está presente en todo el modelo, no es necesario expandir todas esas áreas. En su lugar, sólo se expandirán las áreas en las que el ángulo entre la superficie de la piel y el horizonte sea menor que este ajuste. De esta manera, las superficies planas con elementos que sobresalen serán reforzadas, sin aumentar innecesariamente el tiempo de impresión para el resto del modelo.

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
![Si se ajusta a 90 grados, todo el forro se expande con la configuración de la distancia de expansión de la piel](../images/max_skin_angle_for_expansion_90.png)
![Si se ajusta a 45 grados, sólo se expanden las zonas planas](../images/max_skin_angle_for_expansion_45.png)

Expandir el forro es útil para reforzar la conexión entre la parte superior o inferior de la impresión y las paredes de los lados. Sin embargo, también puede aumentar mucho el tiempo de impresión y el uso de material. Este ajuste permite filtrar el material de los lados de la impresión, donde es menos útil para reforzar la conexión entre las paredes y el forro.

Para este ajuste, 0° es horizontal. Si se ajusta a 0°, no se expande ningún forro. 90° es vertical, y hace que se expandan todas las áreas de forro.