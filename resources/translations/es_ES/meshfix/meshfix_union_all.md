Volúmenes de superposiciones de uniones
====
Si un modelo contiene múltiples volúmenes que se cruzan, el volumen que está dentro de ambos volúmenes normalmente no se llenará. Esta configuración hace que Cura ignore las estructuras internas y simplemente las rellene todas, independientemente de cuántas conchas haya alrededor del volumen.

<!--screenshot {
"image_path": "meshfix_union_all_shell.png",
"models": [{"script": "intersecting_cubes.py"}],
"camera_position": [34, 86, 132],
"layer": -1,
"colours": 128
}-->
<!--screenshot {
"image_path": "meshfix_union_all_disabled.png",
"models": [{"script": "intersecting_cubes.py"}],
"camera_position": [34, 86, 132],
"settings": {"meshfix_union_all": false},
"layer": 300,
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_union_all_enabled.png",
"models": [{"script": "intersecting_cubes.py"}],
"camera_position": [34, 86, 132],
"settings": {"meshfix_union_all": true},
"layer": 300,
"colours": 64
}-->
![Una malla con dos cubos que se cruzan](../images/meshfix_union_all_shell.png)
![No se han unido todos los volúmenes](../images/meshfix_union_all_disabled.png)
![La unión eliminó el agujero](../images/meshfix_union_all_enabled.png)

En términos técnicos, este ajuste cambia efectivamente la regla de enrollamiento de [Par-Impar](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule) a [No-cero](https://en.wikipedia.org/wiki/Nonzero-rule). Normalmente, un volumen se llena si está rodeado por un número impar de conchas. Con esta opción activada, se llena si está rodeado por un número distinto a cero de conchas.

**Esto sólo funciona para volúmenes dentro del mismo modelo. Si has cargado múltiples archivos y los has hecho intersecar en Cura, este ajuste no tendrá efecto. Mira el ajuste Eliminar el cruce de mallas para solucionar problemas de superposición de múltiples mallas separadas.**