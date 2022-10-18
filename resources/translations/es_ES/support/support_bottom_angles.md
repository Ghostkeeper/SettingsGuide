Direcciones de línea del suelo de soporte
====
El suelo de soporte se orienta normalmente para que sea lo más perpendicular posible al soporte de arriba y al modelo de abajo. Si se ha personalizado la orientación de las líneas de la superficie superior o de las líneas de soporte, es una buena idea personalizar también la orientación de las líneas del suelo de soporte. Este ajuste permite personalizar la orientación de las líneas del suelo de soporte.

<!--screenshot {
"image_path": "support_interface_angles_0.png",
"models": [
    {
        "script": "plug.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 36, 92],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_interface_pattern": "lines",
    "support_interface_angles": [0, 90]
},
"layer": 118,
"colours": 128
}-->
<!--screenshot {
"image_path": "support_interface_angles_45.png",
"models": [
    {
        "script": "plug.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 36, 92],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_interface_pattern": "lines",
    "support_interface_angles": [45, 135]
},
"layer": 118,
"colours": 128
}-->
![Tanto el techo como el suelo con ángulos de 0° y 90°](../images/support_interface_angles_0.png)
![Tanto el techo como el suelo tienen ángulos de 45° y 135°](../images/support_interface_angles_45.png)

Se pueden rellenar múltiples ángulos para esta configuración, separados por comas. Cura alternará estos ángulos en las capas.

Lo ideal es que las líneas de suelo de soporte estén orientadas de forma perpendicular a las líneas del modelo en las que se apoyan, así como a las líneas de soporte que se apoyan en ellas. Orientarlas perpendicularmente reduce la distancia que estas líneas tienen que salvar y, por tanto, reduce el pandeo y mejora la estabilidad del soporte.