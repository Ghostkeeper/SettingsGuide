Distancia de la línea de relleno
====
En lugar de establecer la [Densidad de relleno](infill_sparse_density.md) como un porcentaje, también es posible configurar la densidad de relleno estableciendo la distancia entre líneas de relleno adyacentes. Una mayor distancia entre líneas de relleno dará lugar a una menor densidad de relleno en general.

La distancia entre líneas de relleno es una forma diferente de ver esta propiedad que la densidad. La distancia entre líneas de relleno da una indicación de la distancia que las líneas de superficie superior tienen que cruzar de una línea de relleno a la siguiente. Al reducir la distancia de las líneas de relleno, se reduce la distancia de los puentes y se mejora la calidad de las superficies superiores.

<!--screenshot {
"image_path": "infill_pattern_grid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "grid"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_sparse_density_low.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_sparse_density": 10
},
"colours": 64
}-->
![Distancia de 4 mm entre líneas, con una densidad del 20%](../images/infill_pattern_grid.png)
![8mm de distancia entre líneas, dando como resultado un 10% de densidad](../images/infill_sparse_density_low.png)

Normalmente, la distancia de la línea de relleno se calcula a partir de la densidad de relleno deseada, dependiendo del patrón de relleno seleccionado y del ancho de la línea. La distancia de la línea de relleno es líder.

Aumentar la densidad de relleno (reduciendo la distancia de la línea) tiene un gran efecto en su impresión, a saber:
* Su impresión será más fuerte.
* La superficie superior se apoyará mejor, haciéndola más suave y hermética.
* La superficie superior se apoya mejor, haciéndola más suave y hermética.
* Su impresión requerirá más material y como resultado será más pesada.
* Tarda más en imprimirse.