Dirección de línea de relleno de soporte
====
El patrón de soporte se orienta normalmente de forma que las líneas sean perpendiculares a la mayoría de los elementos que soporta. De este modo, se minimiza la distancia que debe salvar el material soportado. Con este ajuste, la orientación de las líneas de soporte se puede personalizar.

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
![Un ángulo de 0°](../images/support_infill_angle_0.png)
![Un ángulo de 30°](../images/support_infill_angle_30.png)

Si se han ajustado las [Direcciones de la línea superior/inferior](../top_bottom/skin_angles.md), es conveniente ajustar el ángulo del soporte en consecuencia, de modo que siga siendo perpendicular a las líneas de la parte inferior de la impresión. Esto permite que estas líneas del fondo se apoyen correctamente en el soporte, en lugar de caer entre las líneas del soporte. Esto es particularmente importante para las líneas y zigzag [Patrones del soporte](support_pattern.md) donde hay largas rectas entre las líneas de soporte que no proporcionan ningún soporte.

<!--if cura_version >= 4.3-->
**En Cura 4.3 este ajuste fue eliminado en favor de [Direcciones de línea de soporte](support_infill_angles.md).**
<!--endif-->