Alineación de costuras en Z
====
Este ajuste permite elegir dónde se coloca la costura de cada contorno. Hay varias opciones disponibles que dan un gran control sobre dónde se coloca la costura para minimizar su impacto o para permitirle eliminar la costura más fácilmente en el post-procesamiento.

La costura es el lugar donde comienza y termina la impresión del contorno. Incluso si la trayectoria de la boquilla es un círculo cerrado, sigue quedando una costura donde empieza y termina la extrusión porque el proceso de impresión nunca es completamente preciso. Con este ajuste se puede minimizar la visibilidad de la costura ocultándola en algún lugar o extendiéndola.

<!--screenshot {
"image_path": "z_seam_type_user.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
    "z_seam_corner": "z_seam_corner_outer",
    "z_seam_position": "left",
    "z_seam_type": "back"
},
"colours": 32
}-->
Especificada por el usuario
----
![Especificada por el usuario](../images/z_seam_type_user.png)

Esta opción le permite elegir una ubicación manualmente. La costura se colocará en la esquina más cercana a la ubicación elegida. Esto normalmente alineará las esquinas muy juntas, lo que le permite cortar la costura fácilmente. También permite un control fino sobre dónde debe estar la costura.

Por defecto se elige una ubicación en la parte trasera de la impresora. La idea es que los usuarios suelen dejar la parte delantera de sus modelos de cara a la parte frontal de la impresora, por lo que una ubicación en la parte trasera ocultará mejor la costura.

<!--screenshot {
"image_path": "z_seam_type_shortest.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
    "z_seam_corner": "z_seam_corner_outer",
    "z_seam_type": "shortest"
},
"colours": 32
}-->
Más corta
----
![Más corta](../images/z_seam_type_shortest.png)

Esta opción simplemente minimiza la longitud de los movimientos de viaje que conducen a la costura, sin hacer ningún esfuerzo para colocarla en algún lugar en particular. Dado que la ruta de viaje es más corta, ahorrará una pequeña cantidad de tiempo en los movimientos de viaje. La costura también será ligeramente más pequeña, porque se colocará menos rezuma en el lugar donde la boquilla se posa en el contorno.

La preferencia de la esquina deseada se mantiene eligiendo una esquina cercana a donde está la boquilla. No se elige la esquina más cercana, sino que se utiliza una preferencia ponderada para minimizar un poco los movimientos de desplazamiento, pero también se utiliza una esquina adecuada para el ajuste [Preferencia de la esquina de la costura](z_seam_corner.md).

<!--screenshot {
"image_path": "z_seam_type_random.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
    "z_seam_corner": "z_seam_corner_outer",
    "z_seam_type": "random"
},
"colours": 32
}-->
Aleatoria
----
[Aleatoria](../images/z_seam_type_random.png)

Se elige una ubicación aleatoria alrededor del perímetro para la costura. Esta ubicación aleatoria se cambia en cada capa, por lo que la costura se repartirá de manera bastante uniforme alrededor del modelo. Como las costuras de las diferentes capas no se alinean, la costura apenas será visible. Sin embargo, la superficie tendrá un aspecto algo más desordenado.

<!--screenshot {
"image_path": "z_seam_type_sharpest.png",
"models": [{"script": "seams_on_curves.scad"}],
"camera_position": [51, -36, 132],
"settings": {
    "z_seam_corner": "z_seam_corner_outer",
    "z_seam_type": "sharpest_corner"
},
"colours": 32
}-->
Esquina más pronunciada
----
![Esquina más pronunciada](../images/z_seam_type_sharpest.png)

La costura se colocará en la esquina más aguda de todo el contorno, según la preferencia de esquina elegida en el ajuste [Preferencia de esquina de la costura](z_seam_corner.md). Esto puede incurrir en movimientos de desplazamiento más largos, pero asegura que la costura quede oculta o expuesta al máximo según la preferencia establecida para las esquinas.