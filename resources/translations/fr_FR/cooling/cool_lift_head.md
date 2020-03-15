Lorsque la [Durée minimale d’une couche](./cool_min_layer_time.md) est atteinte, la tête d'impression ralentit afin d'éviter d'imprimer plus vite que le Temps de couche minimum. De cette façon, la couche précédente a le temps de refroidir et de se solidifier avant que la couche suivante ne soit posée dessus. La tête d'impression est autorisée à ralentir jusqu'à ce que la [vitesse minimale](./cool_min_speed.md) soit atteinte.

Si ce paramètre est activé et que la tête d'impression doit se déplacer plus lentement que la vitesse minimale afin de maintenir le temps de calque minimum, alors la tête d'impression se déplacera légèrement vers le haut après l'impression du calque. Elle attendra ensuite un certain temps jusqu'à ce que le temps de calque minimum soit atteint, avant de commencer avec le calque suivant.

Si ce paramètre est désactivé, la tête d'impression attendra plutôt à la fin de la couche, la buse touchant l'impression.

![Lorsque le temps de calque minimum est atteint, la tête peut se soulever](../images/cool_fan_speed_fr.svg)

La tête d'impression se déplace toujours de 3 mm vers le haut. Il n'y a pas de réglage pour configurer cela pour le moment.
