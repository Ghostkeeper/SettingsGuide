Evite partes impresas al desplazarse
====
Activando esta opción, el cabezal de impresión intentará evitar chocar con otros objetos cuando se desplace por el volumen de impresión. En su lugar, tomará un pequeño desvío. Si es posible un desvío que no golpee ningún otro objeto, no se activará ninguna retracción a menos que la longitud de la ruta exceda el ajuste [Distancia de peinada máxima sin retracción](retraction_combing_max_distance.md).

<!--screenshot {
"image_path": "travel_avoid_other_parts_disabled.png",
"models": [{"script": "spike_curve.scad"}],
"camera_position": [0, 0, 116],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
    "retraction_enable": false,
    "travel_avoid_other_parts": false
},
"minimum_layer": 549,
"layer": 550,
"colours": 64
}-->
<!--screenshot {
"image_path": "travel_avoid_other_parts_enabled.png",
"models": [{"script": "spike_curve.scad"}],
"camera_position": [0, 0, 116],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
    "retraction_enable": false,
    "travel_avoid_other_parts": true
},
"minimum_layer": 549,
"layer": 550,
"colours": 64
}-->
![Cuando se desactiva, los movimientos de viaje pueden atravesar otras partes](../images/travel_avoid_other_parts_disabled.png)
![Cuando están activados, los movimientos de desplazamiento evitan otras partes](../images/travel_avoid_other_parts_enabled.png)

Además de evitar otras partes, los movimientos de desplazamiento también tratarán de permanecer cerca de las paredes el menor tiempo posible. Esto significa que al salir o entrar en una pieza a través de una pared, saldrá o entrará en ella perpendicularmente a la pared.

Esta configuración tiende a mejorar la calidad de la superficie de la impresión, porque la boquilla no cruzará las paredes tan a menudo. Cruzar las paredes deja una cicatriz en la pared, por lo que debe evitarse.

Sin embargo, este ajuste aumenta la cantidad de rezumado, ya que se harán más movimientos de desplazamiento sin retracción y los movimientos de desplazamiento serán más largos. Con materiales que rezuman mucho, puede ser aconsejable desactivar el evitar otras partes.

El tiempo de impresión puede aumentar ligeramente debido a que los movimientos de desplazamiento son más largos, pero normalmente esto se compensa completamente con la reducción del número de retracciones que esto provoca.