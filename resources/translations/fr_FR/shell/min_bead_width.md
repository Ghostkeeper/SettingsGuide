Largeur minimale de la ligne de paroi fine
====
Ce paramètre permet d'imprimer de très petits détails avec une largeur de ligne qui est en fait trop grande pour eux. Au lieu d'imprimer des lignes très fines, il imprime avec une largeur de ligne plus raisonnable.

Si la [Taille minimale des entités](min_feature_size.md) est très faible, des pièces très fines peuvent être imprimées. Cela ne fonctionne pas bien. Il est possible d'imprimer des lignes plus petites que la taille de la buse, mais pas de beaucoup. L'impression de lignes trop fines entraîne une extrusion incohérente.

Au lieu de cela, ces lignes très fines sont rendues plus larges afin qu'elles soient extrudées de manière plus cohérente. Toute partie du modèle qui est plus fine que la largeur minimale de la ligne de paroi mince sera imprimée en utilisant une seule ligne de la largeur minimale de la ligne de paroi mince. Les lignes deviennent alors plus larges que la largeur originale du modèle. Cela réduit la précision dimensionnelle, mais au moins l'impression sera fiable.

La valeur de ce paramètre doit correspondre à la largeur de ligne la plus fine que l'imprimante peut atteindre de manière fiable avant de commencer à créer des surfaces rugueuses et une extrusion incohérente. Cette valeur se situe normalement entre la taille de la buse et la moitié de la taille de la buse. L'augmenter conduit à l'impression de pièces fines trop grosses, mais réduit les risques de sous-extrusion dus à l'impression de lignes trop fines.