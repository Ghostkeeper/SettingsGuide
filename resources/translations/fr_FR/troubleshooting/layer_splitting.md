Séparation des couches
====
L'adhésion entre les couches est souvent le principal point faible de la structure des objets imprimés en 3D. Si l'adhérence entre les couches diminue pendant ou peu après l'impression, on parle de séparation des couches, de séparation des couches ou de délamination.

![Les couches se sont séparées sur le côté de ce conteneur](../../../articles/images/layer_splitting.jpg)

Les ruptures de couche peuvent être difficiles à gérer, car l'impression se divise toujours au niveau du maillon le plus faible. Les suggestions ci-dessous visent à rendre l'impression plus constante et l'extrusion plus fiable, afin de supprimer les zones d'adhésion faibles entre les couches.

Gauchissement
----
La majorité des ruptures de couches sont causées par le [décollement](warping.md). Ce phénomène est particulièrement fréquent avec les polymères semi-cristallins. Ceux-ci forment des structures cristallines microscopiques lorsqu'ils refroidissent, et se rétractent beaucoup pour former ces structures. La forme la plus courante de gauchissement est celle de la partie inférieure de l'impression qui se déforme vers le haut, ce qui ne provoque pas d'éclatement des couches. Cependant, si le gauchissement se produit plus haut dans l'impression, les couches se déforment et se séparent de leurs couches adjacentes.

Pour éviter le gauchissement dans les couches supérieures, un certain nombre de mesures peuvent être prises pour réduire le risque de séparation des couches :
* Utilisez un [Motif de remplissage supérieure/inférieure](../top_bottom/top_bottom_pattern.md) concentrique . Un motif linéaire comporte des lignes qui vont toutes se rétracter dans la même direction, ce qui va tirer ces couches vers le haut dans la même direction. Le motif concentrique permet de répartir les contraintes.
* L'augmentation de la [température du volume de construction](../material/build_volume_temperature.md) réduit le gauchissement en [recuisant](https://en.wikipedia.org/wiki/Annealing_%28glass%29) le plastique. Pour ce faire, l'imprimante a besoin d'un volume de construction fermé, qui garde la chaleur à l'intérieur.
* De même, l'utilisation d'un [bouclier](../experimental/draft_shield_enabled.md) permet de conserver une partie de la chaleur, mais de manière moins efficace qu'un volume de construction fermé.
* Évitez les angles vifs dans le modèle 3D. L'ajout d'un congé sur les angles aigus empêche les lignes de peau de tirer directement sur les murs sous-jacents. C'est souvent à cet endroit que la séparation des couches se produit.
* Utilisez un matériau qui ne se rétracte pas autant. Par exemple, le PLA se déforme moins que le polypropylène. Cependant, la plupart des gens choisissent leur matériau en fonction d'exigences spécifiques, ce qui ne constitue pas une option pour eux.


Pression insuffisante
----
Pour que les couches adhèrent bien les unes aux autres, il est nécessaire de pousser fortement le plastique sur la couche précédente. Si la buse n'extrude pas assez de matériau ou si le matériau n'est pas poussé assez fort contre la couche précédente, la force d'adhésion entre les couches s'en trouve réduite, ce qui leur permet de se séparer plus facilement. Même si cela ne provoque pas immédiatement la rupture d'une couche, cela réduit également la résistance de la pièce finale.

C'est principalement un problème pour les parois. La peau présente une telle surface qu'elle n'a pas tendance à se séparer. Entre le remplissage et les murs, les murs fournissent la majorité de l'adhésion de la couche, car le remplissage est souvent imprimé très rapidement, en utilisant des lignes peu distribuées et souvent non empilées verticalement.

Pour assurer une pression suffisante, il est important de s'assurer qu'il n'y a pas de [sous-extrusion](underextrusion.md). Toutes les causes de sous-extrusion sont applicables, mais certaines d'entre elles sont particulièrement préoccupantes pour le fractionnement des couches :
* Lorsque l'on met l'impression en pause à mi-chemin, il faut un certain temps pour que l'extrusion reprenne sa vitesse. Le script Pause at Height a une option pour <!--if cura_version >= 4.7-->refaire une couche<!--endif--><!--if cura_version < 4.7:refaire les dernières couches-->. Cela amorcera le matériau avant de continuer vers le haut, empêchant une couche faible avec une pression insuffisante de la buse.
* Réduire la [vitesse d'impression des murs](../speed/speed_wall.md) rend l'impression des murs plus constante. Cela réduit le risque de développer des points faibles, tout en réduisant la sous-extrusion sur les murs.
* Réduisez la [Hauteur de couche](../resolution/layer_height.md) ou la [Largeur de ligne de mur](../resolution/wall_line_width.md). Les débits élevés nécessitent une pression plus importante. Si l'imprimante n'est pas en mesure de fournir cette pression, le matériau extrudé sera insuffisant pour remplir les couches épaisses ou les lignes larges. Cela rend l'impression plus faible.
* Augmentez la [température d'impression](../material/material_print_temperature.md) pour vous assurer que le matériau s'écoule plus facilement, en utilisant pleinement la surface de contact, plutôt que de rester concentré au centre du cordon.
* Réduisez la [longueur des rétractions] (../travel/retraction_amount.md). Les rétractions longues permettent à plus de matériau de fuir pendant la rétraction, provoquant une sous-extrusion ultérieure. Elles interrompent également davantage l'écoulement. Il faudra plus de temps pour que l'écoulement se stabilise ensuite. En réduisant la longueur de la rétraction, on réduit le risque de voir se développer de faibles liaisons sur la hauteur de l'impression en raison d'un écoulement irrégulier.


Surface insuffisante
----
L'adhésion entre les couches est fonction de la force de la liaison entre les matériaux, multipliée par la surface à laquelle elle se lie. L'augmentation de la surface permet de réduire le risque de séparation des couches.

Le paramètre le plus important à cet égard est l'[épaisseur de la paroi](../shell/wall_thickness.md). Un plus grand nombre de parois augmente considérablement la surface. Les murs sont imprimés plus lentement et sont situés à l'endroit où ils commenceront à se séparer, ils sont donc un moyen très efficace d'augmenter l'adhésion des couches. Cependant, l'impression d'un plus grand nombre de murs augmente aussi considérablement le temps d'impression et l'utilisation de matériaux.

Une surface insuffisante est souvent un problème lors de l'impression de grandes impressions, où la déformation est forte, avec une seule paroi et sans remplissage. Le mur commencera à se déformer à cause du gauchissement et il n'y a rien pour l'arrêter. Cela peut être une raison pour désactiver l'utilisation du mode [spirale](../blackmagic/magic_spiralize.md), puisqu'il imprime une seule paroi et empêche la génération de remplissage. Au lieu de cela, vous devrez peut-être imprimer avec deux murs et régler manuellement la densité de remplissage sur 0 % pour obtenir un effet similaire.

Matériaux incompatibles
----
Dans les impressions comportant différents types de plastique, veillez à ce que les plastiques adhèrent les uns aux autres. En général, les plastiques dont les taux de rétraction sont très différents ne pourront pas adhérer les uns aux autres. En raison d'effets chimiques différents, les plastiques se repoussent également, ce qui les empêche de coller. Si cela se produit dans une grande zone plate au milieu de votre impression, il y a de fortes chances que l'impression se détache à cet endroit.

Pour éviter que cela ne se produise, il peut être nécessaire de concevoir un joint de verrouillage mécanique entre les deux surfaces. Traitez les différents matériaux comme s'ils étaient imprimés séparément, sauf qu'ils n'auront pas besoin d'être assemblés ultérieurement.
