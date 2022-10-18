Recuento de líneas del borde de soporte
====
Este parámetro ajusta el número de contornos que se dibujarán dentro del área de soporte para el borde de apoyo. Con más líneas, el borde será más ancho.

<!--screenshot {
"image_path": "support_brim_2mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
    "support_enable": true,
    "support_use_towers": false,
    "support_brim_enable": true,
    "support_brim_width": 2
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_brim_4mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
    "support_enable": true,
    "support_use_towers": false,
    "support_brim_enable": true,
    "support_brim_width": 4
},
"colours": 64
}-->
![5 líneas de borde](../images/support_brim_2mm.png)
![10 líneas de borde](../images/support_brim_4mm.png)

Un mayor número de líneas de borde aumentará la adherencia del soporte a la placa de impresión y reducirá la deformación del soporte. Como resultado, el soporte será más resistente, lo que mejora la fiabilidad de la impresión.