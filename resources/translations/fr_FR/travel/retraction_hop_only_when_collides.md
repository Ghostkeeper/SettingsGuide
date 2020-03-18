Décalage en Z uniquement sur les pièces imprimées
===

Ce réglage amène l'imprimante à essayer d'éviter plus souvent d'autres objets horizontalement plutôt que de passer au-dessus d'eux verticalement.

Si le paramètre [Eviter les pièces imprimées](travel_avoid_other_parts.md) est activé, la buse évitera les autres pièces lorsqu'elle se déplace d'un endroit à un autre. Normalement, si un saut en Z est appliqué, il n'est plus nécessaire d'éviter les pièces imprimées. Ce réglage inverse cette logique : S'il n'est pas possible d'éviter les parties imprimées, un saut Z est appliqué.

Les sauts en Z peuvent être problématiques pour l'usure de l'axe Z de certaines imprimantes. Ce réglage peut réduire le nombre de sauts en Z en contournant un objet horizontalement plutôt que verticalement. Pour certaines imprimantes, se déplacer horizontalement plutôt que verticalement peut également être plus rapide.
