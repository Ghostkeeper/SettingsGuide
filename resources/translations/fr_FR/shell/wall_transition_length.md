Longeur de transition de la paroi
====
Dans les pièces minces, toutes les parois ne rentrent pas à l'intérieur de la forme. Si la pièce est plus fine à certains endroits qu'à d'autres, Cura doit utiliser un nombre différent de cordons à certains endroits. Ce paramètre contrôle la largeur de la zone de transition où l'on ajoute ou supprime l'un des cordons.

![Une transition très courte](../../../articles/images/wall_transition_length_0_2.png)
![Une transition plus longue](../../../articles/images/wall_transition_length_1_5.png)

La zone de transition entre différents nombres de cordons présente toujours de légers problèmes. C'est le plus visible lorsqu'une seule ligne au centre se termine et que les deux cordons environnants doivent combler le vide. Ils ne remplissent pas immédiatement l'espace, et un vide est laissé. Cela se traduit par de petits trous en haut et en bas des impressions. Le contraire se produit lorsque deux cordons se combinent en un seul, ce qui les fait se chevaucher pendant un moment jusqu'à ce qu'ils se rejoignent. La surextrusion peut entraîner une imprécision dimensionnelle, surtout lorsqu'elle se produit dans la paroi extérieure. Tout cela peut être évité en rendant la transition aussi courte que possible.

Toutefois, une transition courte oblige également la buse à effectuer des virages très serrés pour combler rapidement cet espace. Il en résulte une augmentation des vibrations, en particulier si cela se produit pour l'impression de la paroi extérieure. Si la transition est plus longue, les accélérations dans la buse sont réduites, en particulier si elles sont inférieures à la limite de [Saccade](../speed/jerk_print.md).

Fixer cette longueur à une ou deux fois la largeur de la ligne est un point de départ raisonnable. Les imprimantes dont les cadres sont plus léger ou les têtes d'impression plus lourdes peuvent avoir besoin de l'augmenter, tandis que les imprimantes qui peuvent accélérer rapidement sans vibrer peuvent se contenter de raccourcir la transition pour améliorer la qualité visuelle.

**Ce paramètre ne s'applique pas seulement aux parois normales, mais aussi aux parois à contour supplémentaire, aux parois de soutien, aux parois de remplissage et aux motifs concentriques.**
