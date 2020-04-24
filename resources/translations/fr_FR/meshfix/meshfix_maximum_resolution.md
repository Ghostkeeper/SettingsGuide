Résolution maximum
====
Bien que la haute résolution puisse sembler meilleure au début, il arrive souvent que l'imprimante ne gère pas très bien le G-Code en haute résolution. C'est pourquoi Cura réduit la résolution de base pendant le processus de découpage. Ce paramètre détermine la résolution que Cura maintiendra au maximum.

![Avant de réduire la résolution](../../../articles/images/meshfix_maximum_resolution_0.05.png)
![Après avoir réduit la résolution (ad extremum)](../../../articles/images/meshfix_maximum_resolution_1.png)

L'imprimante doit traiter le G-Code pendant qu'il est exécuté. Si le  G-Code contient de nombreux segments de lignes minuscules, la tête d'impression doit réaliser des mouvements si rapidement que le processeur de l'imprimante 3D ne peut pas suivre. Cela a pour effet que la tête d'impression ralentit sporadiquement pour permettre à l'unité de pilotage de rattraper le mouvement ou simplement d'attendre la prochaine commande de mouvement. La surface devient alors très rugueuse, voire présente de petites marques, car le débit sortant de la buse ne correspond pas parfaitement au mouvement sporadique de la buse. Parfois, une résolution plus faible se traduit par une meilleure qualité d'impression.

Ce réglage indique une longueur minimale pour les segments de ligne. Les segments de ligne qui sont plus courts que la longueur spécifiée seront considérés comme pouvant être joints à d'autres segments de ligne. Ils seront alors joints si le nouveau chemin ne s'écarte pas de son chemin d'origine de plus de la [Déviation maximale](meshfix_maximum_deviation.md).

Notez qu'il n'est pas garanti que les mêmes sommets soient retirés de chaque couche si les sommets s'alignent. La réduction de la résolution est effectuée en 2D en supprimant les sommets des formes de la couche, et non en 3D en supprimant les sommets du maillage. Par conséquent, une réduction trop importante de la résolution conduira souvent à une surface irrégulière, plutôt qu'à une surface angulaire réglée.

Il est recommandé de réduire la résolution du modèle de manière à ce que la tête d'impression ne ralentisse pas de manière significative pour laisser le temps au CPU de rattraper son retard. Si la résolution n'est pas suffisamment réduite, la surface deviendra rugueuse du fait que la tête d'impression réduira sa vitesse pendant que l'extrusion se poursuit. Si la résolution est trop réduite, la surface sera également rendue rugueuse par le fait que les murs ne s'aligne pas exactement partout.

