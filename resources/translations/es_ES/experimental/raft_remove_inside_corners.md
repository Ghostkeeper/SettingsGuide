Eliminar las esquinas interiores de la balsa
====
Cuando esta opción está activada, todas las esquinas interiores de la balsa se eliminan completamente, convirtiendo la balsa en una [forma convexa](https://en.wikipedia.org/wiki/Convex_set). La balsa sólo tendrá esquinas exteriores.

<!--screenshot {
"image_path": "raft_remove_inside_corners.png",
"models": [{"script": "microwave_hook.scad"}],
"camera_position": [59, 59, 200],
"settings": {
	"adhesion_type": "raft",
	"raft_remove_inside_corners": true
},
"colours": 64
}-->
![La balsa ya no sigue la forma del modelo](../images/raft_remove_inside_corners.png)

Esto es efectivamente equivalente a tener un [suavizado] muy alto(../platform_adhesion/raft_smoothing.md). La eliminación de las esquinas interiores de la balsa tiene varios efectos:
* Ya no es posible que una pequeña parte de la balsa sobresalga mucho del resto de la balsa. Las partes pequeñas de la balsa son más propensas a soltarse de la placa de construcción, especialmente con materiales muy alabeados. La eliminación de las esquinas interiores reduce este efecto, haciendo que la impresión sea más fiable.
* La balsa es más grande, aumentando la fuerza de adhesión total a la placa de construcción.
* La balsa tarda más en imprimirse y utiliza más material.