Espesor del soporte de los bordes del forro
====
Cuando se imprimen formas cóncavas, habrá un poco de forro superior que termina en algún lugar a mitad de camino a través del relleno. Este ajuste añade una línea extra a través del relleno para apoyar el borde del forro, de modo que se hunde un poco menos.

<!--screenshot {
"image_path": "skin_edge_support_thickness_0.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.4)", "translateZ(-2.5)"]
    }
],
"camera_position": [-29, 29, -50],
"settings": {
    "infill_sparse_density": 10,
    "bottom_thickness": 0,
    "skin_edge_support_thickness": 0
},
"colours": 128
}-->
<!--screenshot {
"image_path": "skin_edge_support_thickness.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.4)", "translateZ(-2.5)"]
    }
],
"camera_position": [-29, 29, -50],
"settings": {
    "infill_sparse_density": 10,
    "bottom_thickness": 0,
    "skin_edge_support_thickness": 1
},
"colours": 128
}-->
![El borde del forro no está bien soportado por el relleno](../images/skin_edge_support_thickness_0.png)
![Se dibuja un perímetro a través del relleno bajo el borde del forro](../images/skin_edge_support_thickness.png)

Una sola línea a través de los huecos del relleno todavía se hundirá, por lo que la línea se puede dibujar en varias capas por debajo del borde del forro que necesita apoyo. Este ajuste configura el grosor vertical de la línea por debajo del borde del forro. También puede ajustar directamente el [número de capas](skin_edge_support_layers.md) debajo del borde del forro donde se dibujará esta línea.

Aumentar este grosor generalmente tendrá los siguientes efectos en la impresión:
* El borde del forro se apoyará mejor, dando lugar a una parte superior más suave porque el forro puede pasar completamente de un lado a otro.
* Se tarda un poco más en imprimir, y se utilizará más material.

Si la tasa de relleno es alta, este ajuste apenas tendrá efecto en la superficie superior y podría causar [sobreextrusión](../troubleshooting/overextrusion.md) en el relleno. Es mejor dejarla en 0 mm entonces.