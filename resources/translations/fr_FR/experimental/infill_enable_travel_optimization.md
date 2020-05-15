Optimisation du déplacement de remplissage
====
L'activation de ce paramètre peut réduire légèrement la durée du voyage dans votre imprimé. En raccourcissant la durée des déplacements, l'impression sera légèrement plus rapide et la buse suintera également un peu moins. Cependant, il faudra également plus de temps pour découper le modèle.

Normalement, Cura optimise l'ordre dans lequel les lignes de remplissage sont tracées de manière assez naïve. Après chaque ligne, Cura cherchera la ligne suivante la plus proche pour la dessiner et la tracer. Cependant, pour certaines formes inhabituelles et complexes, le chemin jusqu'à la ligne de remplissage suivante peut être assez long car la buse doit faire un détour en raison du [Mode de détour](../travel/retraction_combing.md). Basiquement, Cura sous-estime alors la distance et peut choisir un déplacement plus long plutôt qu'un déplacement plus court. Lorsque ce paramètre est activé, la distance est calculée avec précision afin qu'un meilleur choix puisse être fait.

Ce réglage n'aura généralement que peu d'impact sur le temps de tranchage. Toutefois, pour les impressions complexes comportant de nombreuses petites zones (là où il est le plus utile), il peut augmenter le temps de découpe par des ordres de grandeur de (valeur non évaluée à rajouter).
