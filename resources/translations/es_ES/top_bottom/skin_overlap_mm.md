Superposición del forro
====
Este ajuste hace que la piel se solape un poco con las estructuras adyacentes. Esto hace que la piel se adhiera mejor a esas estructuras.

<!--screenshot {
"image_path": "skin_overlap_none.png",
"models": [{"script": "mounting_plate.scad"}],
"camera_position": [0, 0, 84],
"settings": {
    "skin_outline_count": 0,
    "skin_overlap": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "skin_overlap_20.png",
"models": [{"script": "mounting_plate.scad"}],
"camera_position": [0, 0, 84],
"settings": {
    "skin_outline_count": 0,
    "skin_overlap": 40
},
"colours": 64
}-->
![No overlap](../images/skin_overlap_none.png)
![Some overlap](../images/skin_overlap_20.png)

Este solapamiento produce técnicamente una sobreextrusión, pero la cantidad de sobreextrusión es lo suficientemente pequeña como para que no sea visible. Sin embargo, tendrá una influencia significativa en la resistencia, porque el forro puede adherirse mejor a las paredes y al relleno. Al fin y al cabo, estas estructuras sólo aumentan la resistencia del modelo si tienen algo a lo que agarrarse.

Un poco de solapamiento también puede ayudar a reducir la aparición de huecos en el forro.