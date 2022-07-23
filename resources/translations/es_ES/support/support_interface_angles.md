Direcciones de la línea de la interfaz de soporte
====
La interfaz de soporte se orienta normalmente para ser lo más perpendicular posible al modelo y al cuerpo de soporte que lo rodea. Si se ha personalizado la orientación de las líneas superiores/inferiores o de las líneas de soporte, es una buena idea personalizar también la orientación de las líneas de la interfaz de soporte. Este ajuste permite personalizar la orientación de las líneas de interfaz de soporte.

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
![Ángulo de 0° y 90°](../images/soporte_interfaz_ángulos_0.png)
![Ángulo de 45° y 135°](../images/support_interface_angles_45.png)

Se pueden rellenar varios ángulos para esta configuración, separados por comas. Cura alternará estos ángulos en las capas.

Lo ideal es que las líneas de la interfaz de soporte estén orientadas de forma perpendicular a las líneas en las que se apoyan y a las líneas que se apoyan en ellas. Al orientarlas perpendicularmente se reduce la distancia que estas líneas tienen que salvar y, por tanto, se reduce el pandeo y se mejora la calidad de los voladizos. Esto es especialmente importante cuando se trabaja con soportes que no son completamente densos.