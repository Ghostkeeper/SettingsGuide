X début couche
====
S'il y a plusieurs parties à imprimer sur une couche, Cura optimisera l'ordre dans lequel ces parties sont imprimées. Pour permettre à la pièce de refroidir avant l'impression de la couche suivante, elle imprimera chaque couche à peu près dans le même ordre. Les paramètres **X début de couche** et [Y début de couche](layer_start_y.md) déterminent quelle partie sera imprimée en premier : La partie qui est la plus proche des coordonnées spécifiées. Ce paramètre détermine la coordonnée X de cette partie.

Il s'agit d'un paramètre différent de la couture Z. Les paramètres d'alignement de la couture Z déterminent seulement où l'imprimante commencera à imprimer le contour d'une pièce, alors que ce paramètre détermine avec quelle pièce elle commencera.

Si votre imprimante fait quelque chose de spécifique lorsqu'elle commence avec une nouvelle couche ou lorsqu'elle change d'extrudeuse, il est bon de régler ces coordonnées à l'endroit où la tête d'impression termine lorsqu'elle est prête à poursuivre l'impression. Cela permet de réduire au minimum les déplacements et les suintements.

Ces coordonnées se trouvent dans le système de coordonnées g-code, qui est différent du système de coordonnées que Cura utilise pour montrer le placement des objets.
