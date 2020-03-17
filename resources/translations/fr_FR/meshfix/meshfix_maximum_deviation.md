Écart maximum
===

Bien que la haute résolution puisse sembler meilleure au début, il arrive souvent que l'imprimante ne gère pas très bien le code G haute résolution. C'est pourquoi Cura réduira la résolution de son entrée pendant le processus de découpage. Ce paramètre détermine dans quelle mesure le chemin réduit peut s'écarter du chemin original afin de réduire la résolution.

![Avant de réduire la résolution](../../../articles/images/meshfix_maximum_resolution_0.05.png)
![Après avoir réduit la résolution (ad extremum)](../../../articles/images/meshfix_maximum_resolution_1.png)

L'imprimante doit traiter le g-code pendant qu'il est exécuté. Si le g-code contient de nombreux segments de lignes minuscules, la tête d'impression peut se précipiter dans le mouvement si rapidement que le processeur de l'imprimante 3D ne peut pas suivre. Cela a pour effet que la tête d'impression ralentit sporadiquement pour permettre à l'unité centrale de rattraper le mouvement ou simplement d'attendre la prochaine commande de mouvement. La surface devient alors très rugueuse, voire présente de petites taches, car le débit sortant de la buse ne correspond pas parfaitement au mouvement sporadique de la buse. Parfois, une résolution plus faible se traduit par une meilleure qualité d'impression.

Ce réglage indique dans quelle mesure la nouvelle trajectoire à résolution réduite peut s'écarter de la trajectoire à haute résolution originale. On considère que les lignes sont jointes à d'autres segments de ligne si elles sont plus courtes que la [résolution maximale](./meshfix_maximum_resolution.md), mais si ce raccourci entraîne une déviation du trajet supérieure à la distance indiquée par ce paramètre, les lignes ne seront pas jointes.

Notez qu'il n'est pas garanti que les mêmes sommets soient retirés de chaque couche si les sommets s'alignent. La réduction de la résolution est effectuée en 2D en supprimant les sommets des formes de la couche, et non en 3D en supprimant les sommets du maillage. Par conséquent, une réduction trop importante de la résolution conduira souvent à une surface irrégulière, plutôt qu'à une surface angulaire.

Pour des raisons d'intégrité structurelle, il est fortement recommandé de ne pas laisser les trajectoires dévier de plus d'une demi-largeur de ligne. Cependant, si la surface doit être lisse ou avoir un bel aspect, ce réglage indique essentiellement la profondeur des irrégularités de la surface. La déviation maximale doit être très faible afin de ne pas être visible à l'œil nu.

Cependant, une réduction trop importante de l'écart maximal limite considérablement la réduction de la résolution. Le code g résultant peut alors ne pas s'imprimer correctement car l'unité centrale n'est pas en mesure de rattraper les commandes de mouvements courts.
