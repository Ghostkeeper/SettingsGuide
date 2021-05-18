Vitesse de déplacement
====
Ce paramètre configure la vitesse à laquelle la tête d'impression se déplace lorsqu'elle n'extrude aucun matériau.

![Diverses structures imprimées à différentes vitesses](../../../articles/images/speed_difference.png)

La vitesse de déplacement est généralement beaucoup plus élevée que tout autre réglage de vitesse. L'augmentation de la vitesse de déplacement a notamment les effets suivants :
* Une vitesse de déplacement plus élevée peut légèrement réduire le temps d'impression.
* Elle réduira le temps que le filament doit s'écouler du matériau, ce qui permettra d'obtenir une pièce plus propre avec des taches plus petites dues au suintement.
* Cependant, l'augmentation de la vitesse tend également à faire vibrer davantage l'imprimante, ce qui augmente le bourdonnement. On peut réduire ce phénomène avec des sauts en Z, mais le saut en Z prend souvent plus de temps qu'on ne peut en gagner en augmentant la vitesse de déplacement.
* Augmenter la vitesse augmente le risque de renversement de votre impression, surtout si [le Mode de détours](../travel/retraction_combing.md) est désactivé.
* Lorsqu'ils atteignent des vitesses extrêmes, les moteurs de l'imprimante peuvent également perdre certains pas, ce qui provoque un décalage des couches.

**La vitesse de déplacement a moins d'effet sur le temps total d'impression que ce que la plupart des gens pensent. En effet, le temps de déplacement ne représente généralement qu'une petite fraction du temps total d'impression, et il faut beaucoup de temps pour atteindre les vitesses élevées, qui sont principalement limitées par l'accélération plutôt que par la vitesse maximale.
