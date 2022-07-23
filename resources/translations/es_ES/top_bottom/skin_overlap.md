Porcentaje de superposición del forro
====
Este ajuste hace que el forro se solape un poco con las estructuras adyacentes. Esto hace que la piel se adhiera mejor a esas estructuras.

La superposición en este ajuste se expresa como un porcentaje de la anchura media de la línea entre las líneas de la piel y las líneas de la pared más interna.

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
![Sin superposición](../images/skin_overlap_none.png)
![Algo de superposición](../images/skin_overlap_20.png)

Esta superposición produce técnicamente una sobreextrusión, pero la cantidad de sobreextrusión es lo suficientemente pequeña como para que no sea visible. Sin embargo, tendrá una influencia significativa en la resistencia, ya que la piel puede adherirse mejor a las paredes y al relleno. Al fin y al cabo, estas estructuras sólo aumentan la resistencia del modelo si tienen algo a lo que agarrarse.

Un poco de solapamiento también puede ayudar a reducir la aparición de huecos en el forro.