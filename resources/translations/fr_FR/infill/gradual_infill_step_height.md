Hauteur de l'étape de remplissage progressif
====
En cas de remplissage progressif, la densité du remplissage sera réduite de haut en bas en plusieurs étapes. À chaque étape, la densité de remplissage est réduite de moitié. Ce réglage indique la hauteur de ces marches, la distance entre deux endroits où le remplissage est réduit de moitié.

![Hauteur des marches de 1,5 mm](../../../articles/images/gradual_infill_step_height_small.png)
![Remplissage progressif, hauteur de pas de 5mm](../../../articles/images/gradual_infill_step_height_large.png)

Par nature, le remplissage progressif cré une partie du remplissage dans le vide. Cependant, en règle générale, il se répare automatiquement. La première couche de remplissage sera suspendue dans le vide et ne s'attachera que sur les côtés de l'impression correctement. Les couches posées dessus peuvent reposer un peu sur la couche précédente aux extrémités, mais s'affaisseront toujours au milieu. Cela s'améliore progressivement, couche par couche.

* Réduire la taille de l'étape de remplissage graduel afin de descendre rapidement à une faible densité de remplissage. Cela permet d'économiser du temps d'impression et de la matière.
* Augmenter la taille de l'étape de remplissage progressif si le remplissage ne peut pas se réparer d'ici à la prochaine étape de densité de remplissage. Augmenter la valeur de ce paramètre rend l'impression plus fiable.
