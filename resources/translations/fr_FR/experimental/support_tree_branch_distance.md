Distance des branches de support arborescent
===

Ce réglage détermine la distance entre deux branches adjacentes lorsque les branches touchent la plaque de construction.

![Branches placées à 1,4 mm l'une de l'autre](../../../articles/images/support_tree_branch_distance_1_4.png)
![Branches placées à 5mm d'intervalle](../../../articles/images/support_tree_branch_distance_5.png)

Afin de soutenir le modèle, un support en forme d'arbre placera des points de contact sous le modèle selon un quadrillage en quinconce. Ce réglage détermine essentiellement la taille de cette grille et donc la distance entre les branches. En raison de l'alignement des branches par rapport à la direction (par défaut) des lignes de la peau, la distance que les lignes de la peau doivent franchir sera très probablement supérieure à cette distance.

En réduisant la distance entre les branches, on peut obtenir une meilleure qualité de surplomb, car les lignes reposant sur le support n'auront pas besoin de franchir cette distance. Le support sera également plus rigide, car davantage de matériau sera utilisé vers le haut du support, ce qui rendra l'impression plus fiable.

Toutefois, la réduction de la distance entre les branches entraînera également une augmentation de la quantité de matériau utilisée et du temps d'impression.

Si la distance entre les branches est inférieure au [diamètre de la branche](support_tree_branch_diameter.md), les branches fusionneront avant de pouvoir être formées correctement. Par conséquent, le centre des grandes zones en surplomb risque de ne pas être correctement soutenu à ce moment-là.
