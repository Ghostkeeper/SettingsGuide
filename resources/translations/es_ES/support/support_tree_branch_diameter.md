Diámetro de las ramas del soporte en árbol
====
Esta opción le permite ajustar la anchura de las ramas del soporte en árbol. La anchura especificada aquí será la de la parte superior de las ramas del árbol. La punta de la rama será más delgada y hacia la parte inferior se vuelve gradualmente más ancha según el ajuste [Ángulo del diámetro de las ramas del soporte en árbol](support_tree_branch_diameter_angle.md).

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
"image_path": "support_tree_branch_diameter_5mm.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_diameter": 5,
    "support_tree_branch_diameter_angle": 5,
    "support_angle": 80
},
"structures": ["helpers"],
"colours": 16
}-->
![Forma de una rama con un diámetro de 1,4 mm](../images/support_tree_branch_diameter_1_4mm_5.png)
![Forma de una rama con un diámetro de 5 mm](../images/support_tree_branch_diameter_5mm.png)

Las ramas más anchas son más estables, lo que reduce la posibilidad de que el árbol sea derribado por la boquilla si tiene que atravesarla.

Las ramas más anchas también se unirán más rápidamente. Esto ahorrará algo de material, pero también puede impedir que parte del modelo se sostenga correctamente, y de hecho también parte del propio soporte. Cuando las ramas se fusionan, ya no tienen contorno. Las ramas anchas se combinan mejor con un [espaciado] amplio (support_tree_branch_distance.md) o algún [relleno] (../support/support_infill_rate.md) para poder soportar adecuadamente las partes en medio de las ramas anchas.

Las ramas más anchas también tendrán más dificultades para desplazarse por el modelo. Esto puede provocar que una mayor parte del soporte se apoye en el modelo en lugar de en la placa de impresión. Como resultado, su modelo puede tener más cicatrices después de la eliminación de las estructuras de soporte.