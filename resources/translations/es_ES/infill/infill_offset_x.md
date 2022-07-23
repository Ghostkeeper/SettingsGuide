Desplazamiento del relleno sobre el eje X
====
Normalmente los patrones de relleno se centran en el centro del modelo 3D. Este ajuste, junto con el [Desplazamiento del relleno sobre el eje Y](infill_offset_y.md) permite desplazar el centro del patrón. Esta configuración ajusta la coordenada X del centro.

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
"image_path": "infill_offset_x_2.png",
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
    "infill_offset_x": 2
},
"colours": 64
}-->
![El relleno está centrado](../images/infill_offset_xy_0.png)
![Desplazado 2 mm a la derecha](../images/infill_offset_x_2.png)

Cuando se imprime con una baja densidad de relleno, se puede utilizar esto para posicionar el relleno de forma muy precisa, de manera que las líneas de relleno individuales se posicionen donde más se necesita la fuerza.