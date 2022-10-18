Ángulo del diámetro de las ramas de soporte en árbol
====
Las ramas del soporte para árboles son más anchas hacia la parte inferior que hacia la superior. Esto asegura que las ramas permanezcan estables sin importar la altura del soporte. Con este ajuste, puede controlar la velocidad a la que se ensancha el soporte.

<!--screenshot {
"image_path": "support_tree_branch_diameter_1_4mm_5.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_diameter": 1.4,
    "support_tree_branch_diameter_angle": 5,
    "support_angle": 80
},
"structures": ["helpers"],
"colours": 16
}-->
<!--screenshot {
"image_path": "support_tree_branch_diameter_angle_10.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_diameter": 1.4,
    "support_tree_branch_diameter_angle": 10,
    "support_angle": 80
},
"structures": ["helpers"],
"colours": 16
}-->
![Forma de una rama con un ángulo de diámetro de 5°](../images/support_tree_branch_diameter_1_4mm_5.png)
![Forma de una rama con un ángulo de diámetro de 10°](../images/support_tree_branch_diameter_angle_10.png)

Cuanto mayor sea el ángulo, más ancha será la parte inferior del soporte del árbol, especialmente en los modelos altos. Esto tiene varios efectos:
* La mayor anchura de la parte inferior hace que el soporte sea más difícil de derribar. Esto aumenta la fiabilidad del soporte del árbol.
* El fondo más ancho requiere más material y tiempo de impresión.
* El ángulo del soporte se suma al máximo [ángulo](support_tree_angle.md) en el que las ramas pueden sobresalir, por lo que valores muy altos pueden hacer que el soporte del árbol sea menos resistente también en algunos casos.
* Las ramas más anchas tienen más dificultades para desplazarse por la malla, lo que hace más difícil alcanzar algunas partes del voladizo desde la placa de impresión. Como resultado, el soporte puede tener que apoyarse en el modelo en lugar de en la placa de impresión, aumentando la cantidad de cicatrices.
* La evitación de colisiones del árbol es más difícil de calcular para Cura, lo que provoca un aumento del tiempo de corte. Esto se puede contrarrestar aumentando el ajuste [Resolución de colisión del soporte del árbol](support_tree_collision_resolution.md), pero eso reduce también la integridad estructural del soporte del árbol.

En general, querrás que el ángulo sea tal que el soporte del árbol sea lo suficientemente amplio como para soportarse a cualquier altura sin tambalearse demasiado.