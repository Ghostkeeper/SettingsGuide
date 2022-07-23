Recuento de líneas de pared del soporte
====
Este ajuste añade un número de paredes alrededor del perímetro del soporte.

<!--screenshot {
"image_path": "support_wall_count_0.png",
"models": [{"script": "plug.scad"}],
"camera_position": [0, 66, 169],
"settings": {
    "support_enable": true,
    "support_pattern": "lines",
    "support_offset": 0.2,
    "support_wall_count": 0
},
"layer": 236,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_wall_count_3.png",
"models": [{"script": "plug.scad"}],
"camera_position": [0, 66, 169],
"settings": {
    "support_enable": true,
    "support_pattern": "lines",
    "support_offset": 0.2,
    "support_wall_count": 3
},
"layer": 236,
"colours": 64
}-->
![No hay paredes adicionales](../images/support_wall_count_0.png)
![3 paredes adicionales](../images/soporte_pared_conteo_3.png)

Las paredes adicionales añaden fuerza al soporte, reduciendo la posibilidad de que se vuelque. También permite que el soporte soporte mejor los bordes de la zona del voladizo. Para los modelos con esquinas afiladas, estos bordes tienden a ser problemáticos porque las líneas terminan en el aire allí. Este ajuste puede hacer que terminen en una línea de soporte en su lugar.

Sin embargo, las paredes adicionales también tardan más en imprimirse, utilizan más material y hacen que el soporte sea más difícil de retirar del objeto después. Cuando se trabaja con materiales de soporte solubles, las paredes adicionales hacen que el soporte tarde más en disolverse porque el disolvente ya no puede entrar en la estructura de soporte desde el lateral.