Multiplicateur de ligne de remplissage
===

En augmentant ce paramètre, Cura placera davantage de lignes de remplissage directement à côté des autres lignes de remplissage.

![Multiplié par 3](../../../articles/images/infill_multiplier.png)

Cela augmente effectivement la densité de remplissage au-delà de ce que le paramètre [Densité du remplissage](infill_sparse_density.md) spécifie, mais au lieu d'espacer les lignes de remplissage de manière égale, les lignes sont placées directement les unes à côté des autres. Par rapport à une simple augmentation de la densité de remplissage, cela peut augmenter la résistance du remplissage puisque les lignes de remplissage peuvent s'appuyer les unes sur les autres pour plus de rigidité.

Lorsqu'un multiplicateur impair est défini, les lignes de remplissage d'origine restent en place, mais des lignes de remplissage supplémentaires s'enroulent autour des trous du modèle de remplissage. Lorsqu'un multiplicateur pair est défini, les lignes de remplissage d'origine sont retirées et les boucles sont placées directement à leur place.

Par rapport à l'alternative consistant à augmenter la densité de remplissage par le même multiplicateur, cela aura quelques effets sur votre impression.
* Le remplissage devient plus rigide dans l'ensemble, tout comme l'augmentation de la largeur de la ligne de remplissage, car les lignes de remplissage peuvent s'appuyer les unes sur les autres lorsqu'elles sont soumises à des forces de cisaillement.
* Le remplissage brillera davantage à travers la peau, ce qui réduira la qualité de la surface.
* Les espaces entre les lignes de remplissage sont plus grands, car les lignes sont plus serrées les unes contre les autres. La peau s'affaisse donc davantage et permet de s'affaisser.

**Ce réglage n'a aucun effet si la densité de remplissage est de 100 % ou plus.**
