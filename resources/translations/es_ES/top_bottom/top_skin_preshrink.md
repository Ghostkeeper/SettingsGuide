Anchura de retirada del forro superior
====
Elimina las partes finas de las capas superiores completamente rellenas, imprimiéndolas con relleno en su lugar. Esto ahorra tiempo de impresión y material.

Con superficies empinadas, las capas superiores suelen ser muy finas. No son necesarias, ya que la resistencia horizontal de las paredes es más que suficiente si la superficie es casi completamente vertical.

<!--screenshot {
"image_path": "skin_preshrink_original.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_preshrink": 0,
    "top_skin_preshrink": 0,
    "max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_preshrink_shrunk.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_preshrink": 1,
    "top_skin_preshrink": 1,
    "max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
![Antes de la retirada](../images/skin_preshrink_original.png)
![Después de la retirada](../images/skin_preshrink_shrunk.png)

Aumentar demasiado este ajuste puede hacer que la parte superior de las piezas pequeñas quede abierta, porque se llena de relleno en lugar de forro.