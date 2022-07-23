Resolución de colisión del soporte en árbol
====
Una de las principales desventajas del soporte de árbol es que tarda mucho tiempo en cortarse cuando se activa. La mayoría de los cálculos necesarios para el soporte de árbol son para que las ramas del árbol eviten colisionar con la malla. Este ajuste determina la precisión de estos cálculos para evitar colisiones. Aumentar esta resolución (menor precisión) ahorrará mucho tiempo de cálculo, pero también hará que el soporte aparezca dentado cuando esté cerca de la malla.

<!--screenshot {
"image_path": "support_tree_collision_resolution_lo.png",
"models": [{"script": "castle_low.scad"}],
"camera_position": [-128, -63, 30],
"settings": {
    "z_seam_position": "backright",
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "support_tree_collision_resolution_hi.png",
"models": [{"script": "castle_low.scad"}],
"camera_position": [-128, -63, 30],
"settings": {
    "z_seam_position": "backright",
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.02
},
"colours": 32
}-->
![Una resolución baja (0,2 mm) hace que las ramas se vuelvan irregulares](../images/support_tree_collision_resolution_lo.png)
![Una resolución alta (0,02mm) crea ramas suaves](../images/support_tree_collision_resolution_hi.png)

La base técnica de este ajuste es la siguiente. Para evitar colisiones con el objeto impreso cuando el soporte de árbol está activado, Cura calculará volúmenes tridimensionales en los que los centros de las ramas del árbol no pueden entrar. Se calcula un volumen de este tipo para cada diámetro posible de las ramas del árbol, lo que lleva mucho tiempo. El número de diámetros posibles de las ramas aumenta drásticamente a medida que el árbol es más alto y con valores grandes de [Ángulo del diámetro de las ramas del soporte del árbol](support_tree_branch_diameter_angle.md). Por esta razón, el diámetro se redondea al múltiplo más cercano de este ajuste de resolución. Sin embargo, en algunos puntos a lo largo de la altura del árbol, el volumen de colisión que la rama necesita evitar se ajusta a la siguiente muestra de un diámetro de rama, permitiendo de repente más espacio para que la rama se mueva. Esto hace que el árbol parezca irregular.

Aumentar este ajuste hará que el corte tarde menos tiempo en Cura. También hará que el soporte sea más dentado, lo que compromete su resistencia, aumentando la posibilidad de que el soporte se rompa durante la impresión, lo que puede hacer que la impresión falle.