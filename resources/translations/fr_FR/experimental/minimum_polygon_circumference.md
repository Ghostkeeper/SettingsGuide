Circonférence minimale du polygone
====
Cura supprime normalement les détails du modèle qui sont plus petits que ce que la buse peut imprimer. Avec ce réglage, vous pouvez ajuster ce seuil pour supprimer plus ou moins de détails. Ce paramètre mesure la circonférence de chaque forme sur chaque couche et si elle est plus petite que la valeur de ce paramètre, cette forme ne sera pas imprimée.

Il est conseillé de supprimer les détails dont la largeur est inférieure à une ligne. Cela permet d'accélérer légèrement le découpage. Cependant, cela ne fonctionne pas toujours avec les parties plus petites que la [Largeur de la ligne de paroi extérieure](../resolution/wall_line_width_0.md) lorsque la fonction [Imprimer les parois minces](../shell/fill_outline_gaps.md) est activée. Si de très petites pièces doivent pourtant être essayées, vous pouvez réduire ce paramètre.

L'augmentation de ce paramètre peut également aider à supprimer les petits détails et à obtenir une impression plus rapide. S'il n'est pas nécessaire d'imprimer ces petits détails, il est possible d'économiser quelques déplacements pour les atteindre.
