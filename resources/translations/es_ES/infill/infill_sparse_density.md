Densidad de relleno
====
Este ajuste configura la densidad del volumen dentro de la impresión, que es un factor importante en la fuerza de la impresión final, así como la calidad de la superficie superior. Cuanto mayor sea la densidad de relleno, más cerca estarán las líneas de relleno. Puedes incluso superar el 100% de densidad, pero eso provocará una sobreextrusión.

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
![20% de densidad (../images/infill_pattern_grid.png)
![10% de densidad](../images/infill_sparse_density_low.png)

Las diferentes densidades funcionan mejor con diferentes patrones de relleno. Los patrones de relleno con muchas esquinas y muchos cruces no funcionarán bien con grandes densidades de relleno. Las esquinas son un problema porque el filamento tiende a arrastrarse con la esquina, creando bolsas de aire en el exterior de la esquina donde el material debería haberse depositado. Los cruces son un problema aún mayor, porque cuando una línea se cruza con otra su flujo se interrumpe, provocando una subextrusión justo después del cruce.

Aumentar la densidad de relleno (reduciendo la distancia entre líneas) tiene un gran efecto en su impresión, a saber:
* Su impresión será más fuerte.
* La superficie superior se apoyará mejor, haciéndola más suave y hermética.
* La superficie superior se apoya mejor, haciéndola más suave y hermética.
* Su impresión requerirá más material y como resultado será más pesada.
* Tarda más en imprimirse.