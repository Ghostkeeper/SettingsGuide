Mantener caras desconectadas
====
Cura necesita saber dónde está el interior de su modelo para poder llenar el volumen con material. Si el modelo no está bien cerrado, esto es ambiguo. Normalmente, Cura no imprimirá las piezas que no estén bien cerradas.

Con esta configuración activada, se mantendrán las capas cuyo perímetro no esté correctamente cerrado. El perímetro se cerrará artificialmente con una línea recta. Esto puede arreglar algunos modelos que tienen pequeños huecos en sus superficies. Sin embargo, también puede malinterpretar el interior de su modelo.

<!--screenshot {
"image_path": "meshfix_keep_open_polygons_shell.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"layer": -1
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_disabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
    "meshfix_keep_open_polygons": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_enabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
    "meshfix_keep_open_polygons": true
},
"colours": 64
}-->
![A este cubo le falta una esquina](../images/meshfix_keep_open_polygons_shell.png)
![Normalmente las capas que no están cerradas no se imprimen](../images/meshfix_keep_open_polygons_disabled.png)
![Con este ajuste activado, la forma se cierra artificialmente](../images/meshfix_keep_open_polygons_enabled.png)

La vista de rayos X mostrará en rojo los huecos que se pueden cerrar con esta configuración.