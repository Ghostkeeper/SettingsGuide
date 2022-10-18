Direcciones de línea del techo de soporte
====
El techo de soporte se orienta normalmente para que sea lo más perpendicular posible al modelo que está por encima y al cuerpo de soporte que está por debajo. Si se ha personalizado la orientación de las líneas de fondo o de las líneas de soporte, es conveniente personalizar también la orientación de las líneas del techo de soporte. Este ajuste permite personalizar la orientación de las líneas de techo de soporte.

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
![Tanto el techo como el suelo tienen un ángulo de 0° y 90°](../images/support_interface_angles_0.png)
![Tanto el techo como el suelo tienen un ángulo de 45° y 135°](../images/support_interface_angles_45.png)

Se pueden rellenar varios ángulos para esta configuración, separados por comas. Cura alternará estos ángulos entre las capas.

Lo ideal es que las líneas de techo de soporte estén orientadas de forma perpendicular a las líneas de soporte en las que se apoyan, así como a las líneas del modelo que se apoyan en ellas. Al orientarlas perpendicularmente se reduce la distancia que estas líneas tienen que salvar y, por tanto, se reduce el pandeo y se mejora la calidad de los voladizos. Esto es especialmente importante cuando se trabaja con soportes que no son completamente densos.