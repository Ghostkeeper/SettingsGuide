Desplazamiento del relleno sobre el eje Y
====
Normalmente los patrones de relleno están centrados en el centro del modelo 3D. Este ajuste, junto con el [Desplazamiento del relleno sobre el eje X](infill_offset_x.md) permite desplazar el centro del patrón. Esta configuración ajusta la coordenada Y del centro.

<!--screenshot {
"image_path": "infill_offset_xy_0.png",
"models": [
    {
        "script": "hexagonal_prism.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 90],
"settings": {
    "top_layers": 0,
    "infill_pattern": "triangles",
    "infill_offset_x": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_offset_y_2.png",
"models": [
    {
        "script": "hexagonal_prism.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 90],
"settings": {
    "top_layers": 0,
    "infill_pattern": "triangles",
    "infill_offset_y": 2
},
"colours": 64
}-->
![El relleno está centrado](../images/infill_offset_xy_0.png)
![Desplazado 2 mm hacia arriba](../images/infill_offset_y_2.png)

Cuando se imprime con baja densidad de relleno, se puede utilizar esto para posicionar el relleno con mucha precisión, de manera que las líneas de relleno individuales se colocan donde la fuerza es más necesaria.