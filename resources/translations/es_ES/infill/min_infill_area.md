Área de relleno mínima
====
Este ajuste hace que las piezas muy pequeñas se rellenen con el patrón de piel en lugar de con el patrón de relleno, haciéndolas completamente sólidas.

<!--screenshot {
"image_path": "min_infill_area_disabled.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-64, 224, 82],
"settings": {
    "wall_line_count": 0,
    "min_infill_area": 0
},
"colours": 32
}-->
<!--screenshot {
"image_path": "min_infill_area_150.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-64, 224, 82],
"settings": {
    "wall_line_count": 0,
    "min_infill_area": 150
},
"colours": 32
}-->
![Si se ajusta a 0, los pies delgados de este modelo se rellenan con relleno](../images/min_infill_area_disabled.png)
![Si se ajusta a 150, los pies se rellenan con piel](../images/min_infill_area_150.png)

A veces, las áreas huecas muy pequeñas no pueden rellenarse correctamente con relleno, ya que las líneas de relleno serían tan cortas que el material no tiene tiempo de fluir correctamente. Este ajuste hace que se rellenen con piel en su lugar, haciéndolas más fuertes y evitando un borde entre la piel y el relleno.

Si se ajusta a 0, se desactiva esta función.