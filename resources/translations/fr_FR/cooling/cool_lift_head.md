Relever la tête
====
Lorsque la [Durée minimale d’une couche](cool_min_layer_time.md) est atteinte, la tête d'impression ralentit afin d'éviter d'imprimer plus vite que le Temps de couche minimum. De cette façon, la couche précédente a le temps de refroidir et de se solidifier avant que la couche suivante ne soit posée dessus. La tête d'impression est autorisée à ralentir jusqu'à ce que la [vitesse minimale](cool_min_speed.md) soit atteinte.

Si ce paramètre est activé et que la tête d'impression doit se déplacer plus lentement que la vitesse minimale afin de maintenir le temps de couche minimum, alors la tête d'impression se déplacera légèrement vers le haut après l'impression de la couche. Elle attendra ensuite un certain temps jusqu'à ce que le temps de couche minimum soit atteint, avant de commencer avec la couche suivante.

Si ce paramètre est désactivé, la tête d'impression attendra plutôt à la fin de la couche, la buse touchant l'impression.

![Lorsque le temps de couche minimum est atteint, la tête peut se soulever](../images/cool_fan_speed_fr.svg)

La tête d'impression se déplace toujours de 3 mm vers le haut. Il n'y a pas de réglage pour configurer cela pour le moment.

Compromis
----
Il y a un compromis à faire lorsque l'on ralentit la buse pour permettre à la couche de mieux se refroidir. Le temps de couche minimum est destiné à donner un certain temps au matériau pour se refroidir en ralentissant le mouvement de la tête d'impression. Pendant ce temps, les ventilateurs souffleront à leur puissance maximale pour le refroidir plus rapidement, mais la buse chaude est également toujours sur le plastique. Pour les très petites pièces, la buse chaude peut transférer plus de chaleur dans l'impression que ce que les ventilateurs peuvent évacuer. Cela fait fondre le plastique encore plus que si vous n'aviez pas de temps de calque minimum.

Avec Relever la tête, ce problème est résolu. Vous pouvez toujours ralentir jusqu'à un certain point, mais pour les très petites couches, la buse chaude s'éloignera, de sorte qu'elle ne transférera plus de chaleur dans la pièce. La tête est maintenue suffisamment près pour que les ventilateurs de la tête continuent à souffler sur l'impression.

L'inconvénient de cette méthode est qu'elle effectue un [Z hop](../travel/retraction_hop.md), ce qui entraîne un [stringing](../troubleshooting/stringinging.md). Bien que le fait de soulever la tête puisse améliorer l'affaissement et le ballonnement, cela provoquera un autre type de désordre. Un peu de post-traitement manuel à l'aide d'un couteau peut nettoyer les ficelles qu'il provoque.
