Résolution de collision du support arborescent
====

Un inconvénient majeur du support d'arbre est qu'il faut beaucoup de temps pour le couper lorsqu'il est activé. La plupart des calculs nécessaires au support de l'arbre portent sur les branches de l'arbre afin d'éviter les collisions avec le maillage. Ce paramètre détermine la précision de ces calculs d'évitement des collisions. Augmenter cette résolution (précision plus faible) permettra de gagner beaucoup de temps dans les calculs, mais fera également apparaître le support comme déchiqueté lorsqu'il est proche du maillage.

![Une faible résolution (0,2 mm) entraîne une dénivellation des branches](../../../articles/images/support_tree_collision_resolution_lo.png)
![Une haute résolution (0,02mm) crée des branches lisses](../../../articles/images/support_tree_collision_resolution_hi.png)

Le contexte technique de ce cadre est le suivant. Pour éviter les collisions avec l'objet imprimé lorsque le support de l'arbre est activé, Cura calculera les volumes tridimensionnels que les centres des branches de l'arbre ne sont pas autorisés à entrer. Un tel volume est calculé pour chaque diamètre possible des branches de l'arbre, ce qui prend beaucoup de temps. Le nombre de diamètres de branches possibles augmente considérablement à mesure que l'arbre devient plus grand et avec de grandes valeurs pour [Angle de diamètre des branches de support arborescent](./support_tree_branch_diameter_angle.md). Pour cette raison, le diamètre est arrondi au multiple le plus proche de ce paramètre de résolution. Toutefois, en certains points de la hauteur de l'arbre, le volume de collision dont la branche a besoin pour éviter de s'accrocher à l'échantillon suivant du diamètre d'une branche, ce qui laisse soudainement plus d'espace pour que la branche puisse se déplacer. Cela donne à l'arbre un aspect déchiqueté.

En augmentant ce paramètre, la tranche prendra moins de temps à Cura. Cela rendra également le support plus déchiqueté, ce qui compromet sa solidité, et augmentera le risque que le support se casse pendant l'impression, ce qui pourrait entraîner une défaillance de l'impression.
