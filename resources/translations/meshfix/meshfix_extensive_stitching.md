Cosido amplio
====
Cura necesita saber dónde está el interior del modelo para poder rellenarlo con material. Si la superficie de su modelo no es precisamente cerrada o tiene paredes internas, puede ser ambiguo precisar dónde está el interior del modelo.

Un caso común de que el modelo no sea múltiple, es cuando una pieza extra del modelo está unida a una parte que de otra manera estaría cerrada. Esto es común cuando se editan mallas con software de CAD que no fue diseñado para la fabricación (sino sólo para la representación digital) como Blender o SketchUp. Puedes ver un ejemplo de esto en las imágenes de abajo.

<!--screenshot {
"image_path": "meshfix_extensive_stitching_xray.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"layer": -1
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_disabled.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"settings": {
    "meshfix_extensive_stitching": false
},
"colours": 32
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_enabled.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"settings": {
    "meshfix_extensive_stitching": true
},
"colours": 32
}-->
![La vista de rayos X revela una superficie extra en el interior](../images/meshfix_extensive_stitching_xray.png)
![Con este ajuste desactivado, sólo se imprime el volumen correctamente cerrado](../images/meshfix_extensive_stitching_disabled.png)
![Con este ajuste activado, la pieza extra se une correctamente](../images/meshfix_extensive_stitching_enabled.png)

Este ajuste hace que Cura haga un mejor intento de cerrar los huecos en la malla si ésta no es adecuadamente hermética. Esto aumenta las posibilidades de una buena impresión, pero aumenta el tiempo de corte y a veces puede conectar superficies equivocadas.