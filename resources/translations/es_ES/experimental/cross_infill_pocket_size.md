Cross 3D de bolsillo
====
El patrón Cross 3D [infill pattern](../infill/infill_pattern.md) fue hecho para facilitar las impresiones flexibles. Sin embargo, el patrón contiene cruces de 4 vías que son muy rígidos. Este ajuste hace que el patrón evite el cruce para evitar ser demasiado rígido en ciertos lugares. Esto hará que el patrón deje una bolsa de aire en el cruce. Este ajuste determina el tamaño de la bolsa.

<!--screenshot {
"image_path": "infill_pattern_cross_3d.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross_3d",
    "cross_infill_pocket_size": 2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "cross_infill_pocket_size_0_5.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross_3d",
    "cross_infill_pocket_size": 0.5
},
"colours": 32
}-->
![El tamaño de bolsillo por defecto de 2mm](../images/infill_pattern_cross_3d.png)
![Un tamaño de bolsillo de 0.5mm](../images/cross_infill_pocket_size_0_5.png)

El patrón varía la distancia alrededor del cruce de 4 vías. Este ajuste determina el tamaño del bolsillo en las capas cuando las líneas se tocan completamente. El tamaño máximo de la cavidad está determinado por la densidad del relleno. El tamaño de la bolsa no se dibujará más grande que la raíz cuadrada de 2 veces la distancia de la línea de relleno. Si se introduce un valor mayor no tendrá efecto, pero se pueden introducir valores mayores para facilitar tamaños de cajón más grandes en caso de que se utilice [relleno gradual](../infill/gradual_infill_steps.md) o [densidad de relleno variable](cross_infill_density_image.md).

Aumentar el valor de este ajuste hace que el relleno sea más débil en la dirección vertical y reparte mejor la fuerza para crear una distribución de fuerza más uniforme.