Dirección de línea de relleno de soporte
====
El patrón de soporte se orienta normalmente de forma que las líneas sean perpendiculares a la mayoría de los elementos que soporta. De este modo, se minimiza la distancia que debe salvar el material soportado. Con esta configuración, la orientación de las líneas de soporte se puede personalizar.

<!--screenshot {
"image_path": "support_infill_angle_0.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_infill_angles": [0]
},
"layer": 160,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_angle_30.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_infill_angles": [30]
},
"layer": 160,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_infill_angles.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_infill_angles": [30, 60]
},
"layer": 160,
"colours": 64
}-->
![Un ángulo de 0°](../images/soporte_ángulo_de_relleno_0.png)
![Un ángulo de 30°](../images/support_infill_angle_30.png)
![Alternando entre 30° y 60°](../images/support_infill_angles.png)

Este ajuste permite introducir múltiples ángulos, separados por comas. Cuando se introducen múltiples ángulos, Cura alternará entre estos ángulos sobre las capas.

Si se han ajustado las [Direcciones de la línea superior/inferior](../top_bottom/skin_angles.md), es conveniente ajustar el ángulo del soporte en consecuencia, para que siga siendo perpendicular a las líneas de la parte inferior de la impresión. Esto permite que estas líneas del fondo se apoyen correctamente en el soporte, en lugar de caer entre las líneas del soporte. Esto es especialmente importante en el caso de las líneas y el zigzag [Patrones del soporte](support_pattern.md) donde hay largas rectas entre las líneas de soporte que no proporcionan ningún soporte.