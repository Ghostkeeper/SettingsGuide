Imprimer en saccade
====
La saccade (Jerk) détermine la vitesse à laquelle la buse peut passer dans les virages. Avec des valeurs de saccade élevées, la buse ne ralentit pas autant à l'approche d'un virage, ce qui se traduit par une vitesse plus constante mais aussi par des vibrations plus importantes.

**Le terme "Jerk" (saccade)  a été introduit par Marlin dans le domaine de l'impression 3D, mais il n'est pas identique à celui de la physique. Il y a été conçu comme une solution de contournement du problème inhérent à la tentative de suivre parfaitement un chemin. Comme la buse ne peut pas s'écarter de la trajectoire (en théorie), il faudrait qu'elle décélère à 0 mm/s dans chaque coin. Cela ruinerait votre impression, car la décélération à 0 mm/s provoquerait une tache dans chaque coin. Il n'est pas permis de faire des courbes pour raccourcir le coin, ni de le dépasser. Au lieu de cela, Marlin permet un changement instantané du vecteur vitesse dans chaque coin. L'ampleur de ce changement du vecteur vitesse est appelée "saccade". Ainsi, le jerk est le changement instantané maximum de la vitesse, appliqué à chaque coin du mouvement.**

L'augmentation de la secousse aura des effets positifs et négatifs sur votre impression :
* Le temps d'impression sera réduit, car la buse ralentit moins dans les coins.
* Le temps d'impression sera réduit, car la buse ralentit moins dans les coins. La buse se déplace à un rythme plus constant, de sorte qu'elle ne s'attarde pas dans les coins pendant que le matériau continue à s'écouler par l'ouverture.
* L'imprimante vibre généralement davantage dans chaque coin, car la tête d'impression a pour instruction de changer instantanément de direction à une accélération théoriquement infinie. Ces vibrations ont tendance à créer des ondulations dans votre impression, ce qui entraîne des sonneries et une réduction de la précision dimensionnelle.
* A des valeurs extrêmes, il y a un risque que vos moteurs perdent quelques pas dans les coins, ce qui peut provoquer un décalage de la couche.
