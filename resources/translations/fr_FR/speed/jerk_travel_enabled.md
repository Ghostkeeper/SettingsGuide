Activer les saccades de déplacement
====
Si ce paramètre est activé, les mouvements de déplacement ont leur propre taux de saccade. Le paramètre [Saccade de déplacement](jerk_travel.md) contrôle alors la vitesse à laquelle les déplacements peuvent prendre des virages.

La valeur de la saccade pendant le déplacement prendra la valeur de la ligne qui sera imprimée à la destination du déplacement. Par exemple, lorsqu'il se déplace vers le remplissage, la saccade pendant le déplacement est la [saccade du remplissage](jerk_infill.md). Lorsqu'il se déplace vers la paroi extérieur, la saccade sera la [saccade de paroi externe extérieur](jerk_wall_0.md). De cette façon, il s'approchera effectivement des structures plus sensibles avec un peu plus de précaution que les autres structures.

Ce paramètre est activé par défaut, ce qui permet de contrôler la saccade pendant les déplacements. C'est une bonne chose dans la plupart des situations, parce qu'une augmentation de la vitesse de déplacement peut faire gagner du temps, tandis que des vitesses de virage aussi élevées provoqueraient des [ondulations](../troubleshooting/ringing.md) lorsqu'elles sont utilisées pour l'impression.

Cependant, il y a deux raisons pour lesquelles vous pourriez vouloir le désactiver :

* Pour modifier le taux d'accélération pour les déplacements, Cura modifie très souvent le taux d'accélération dans les deux sens. Il passe fréquemment de l'extrusion au déplacement, en particulier avec certains motifs de remplissage et avec les petits détails des parois. Le controleur doit traiter ces commandes et peut ne pas être en mesure de suivre les calculs nécessaires. La désactivation des saccades de déplacement réduit ce problème.
* L'augmentation de la saccade de déplacement fait beaucoup vibrer l'imprimante. Ces vibrations ne sont pas encore tout à fait arrêtées à la fin du déplacement lorsque l'impression doit commencer. Cela peut également entraîner une ondulation à la fin d'un déplacement. Si vous désactivez la fonction "saccade de déplacement", la buse s'approchera des structures sensibles de l'impression (comme la paroi extérieure) avec plus de précaution que des structures moins sensibles (comme le remplissage).


