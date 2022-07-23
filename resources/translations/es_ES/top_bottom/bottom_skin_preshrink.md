Anchura de retirada del forro inferior
====
Elimina las partes finas de las capas inferiores completamente rellenas, imprimiéndolas con relleno en su lugar. Esto ahorra tiempo de impresión y material.

Con superficies empinadas, las capas inferiores suelen ser muy finas. No son necesarias, ya que la resistencia horizontal de las paredes es más que suficiente si la superficie es casi completamente vertical.

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
![Antes de la eliminación](../images/skin_preshrink_original.png)
![Después de la eliminación](../images/skin_preshrink_shrunk.png)

Si la parte inferior de su modelo tiene una pendiente muy pronunciada, el forro se volverá muy fino. En este punto, el [espesor de las paredes] horizontal(../shell/wall_thickness.md) es el que más contribuye a la resistencia de la cáscara. Dado que el grosor de las paredes ya debería estar ajustado para que la resistencia sea suficiente, no compensa añadir más material ahí. Dejar este material fuera del forro fuera ahorra mucho tiempo de impresión.

Aumentar demasiado este ajuste puede hacer que la parte inferior de las piezas pequeñas quede abierta, porque se rellena con material de relleno en lugar de forro.