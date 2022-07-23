Distancia de expansión del forro superior
====
Hace que las capas sólidas de la parte superior de tu impresión sean más anchas o más finas en dirección horizontal. Normalmente las capas sólidas sólo se generan debajo de las partes en las que hay aire por debajo, pero con este ajuste puedes expandirla horizontalmente un poco más, mejorando la resistencia al hacer que el forro se adhiera mejor a las paredes adyacentes y cerrando los huecos en el forro.

<!--screenshot {
"image_path": "skin_preshrink_original.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_preshrink": 0,
    "top_skin_preshrink": 0,
    "bottom_skin_expand_distance": 0,
    "top_skin_expand_distance": 0,
    "max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
<!--screenshot {
"image_path": "expand_skins_expand_distance_1mm.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
    "wall_line_count": 0,
    "infill_wall_line_count": 1,
    "bottom_skin_expand_distance": 1,
    "top_skin_expand_distance": 1,
    "max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
![Cómo se ven normalmente los forros (las partes amarillas)](../images/skin_preshrink_original.png)
![Forros expandidas 1mm](../images/expand_skins_expand_distance_1mm.png)

* Si tienes pequeños agujeros en las capas superiores del forro (agujeros que se rellenan con el patrón de relleno), ajustando esto un poco más alto los cerrará. Esto permite que la impresora imprima continuamente las líneas inferiores, mejorando en gran medida la resistencia.
* Si la parte inferior de su impresión no es plana, el aumento de este ajuste hará que el forro se imprima más allá de la zona que está directamente sobre el aire, por encima de las paredes. Esto mejorará la adhesión entre el forro y las paredes, mejorando de nuevo la resistencia.
* Si se establece este ajuste en un valor negativo, se reducirá la anchura de las capas inferiores, sustituyéndola por el relleno. Esto puede ahorrar algo de tiempo de impresión, a costa de la resistencia.

**Debido a limitaciones técnicas, no puede reducir este ajuste negativamente por debajo del valor de [Anchura de retirada del forro superior](top_skin_preshrink.md). Aumente el ajuste de Ancho de retirada del forro superior para eliminar más forro.**