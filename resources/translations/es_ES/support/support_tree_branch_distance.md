Distancia de las ramas del soporte en árbol
====
Este ajuste determina la distancia entre dos ramas adyacentes donde las ramas tocan la placa de impresión.

<!--screenshot {
"image_path": "support_tree_branch_distance_1_4.png",
"models": [
    {
        "script": "gutter_lift.scad",
        "transformation": ["scale(0.5)", "rotateZ(-90)"]
    }
],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_distance": 1.4
},
"minimum_layer": 1310,
"layer": 1311,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_tree_branch_distance_5.png",
"models": [
    {
        "script": "gutter_lift.scad",
        "transformation": ["scale(0.5)", "rotateZ(-90)"]
    }
],
"camera_position": [0, 0, 180],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_distance": 5
},
"minimum_layer": 1310,
"layer": 1311,
"colours": 64
}-->
![Ramas colocadas a 1,4 mm de distancia](../images/árbol_de_soporte_distancia_de_ramas_1_4.png)
![Ramas colocadas a 5 mm de distancia](../images/support_tree_branch_distance_5.png)

Para apoyar el modelo, el soporte en árbol colocará puntos de contacto debajo del modelo en un patrón de cuadrícula escalonado. Este ajuste determina esencialmente el tamaño de esa cuadrícula y, por tanto, la distancia entre las ramas. Debido a la alineación de las ramas con respecto a la dirección (por defecto) de las líneas de piel, la distancia que las líneas de piel deben salvar será probablemente mayor que esta distancia.

Si se reduce la distancia de las ramas, se puede conseguir una mejor calidad del voladizo, ya que las líneas que descansan sobre el soporte no tendrán que salvar tanta distancia. El soporte también será más rígido porque se utilizará más material hacia la parte superior del soporte, lo que hará que la impresión sea más fiable.

Sin embargo, la reducción de la distancia de la rama también hará que el soporte necesite más material y tiempo de impresión.

Reducir la distancia de las ramas por debajo del [diámetro de las ramas] (support_tree_branch_diameter.md) hará que las ramas se fusionen antes de que puedan formarse correctamente. Como resultado, el centro de las grandes áreas de voladizo puede no tener un soporte adecuado.