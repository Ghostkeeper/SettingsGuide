Activer l'accélération de déplacement
====
Si ce paramètre est activé, les déplacements ont leur propre taux d'accélération. Le paramètre [Accélération de déplacement](acceleration_travel.md) contrôle alors le taux d'accélération pendant les déplacements.

La valeur de l'accélération pendant le déplacement prendra la valeur de la ligne qui sera imprimée à la destination du déplacement. Par exemple, lorsqu'il se déplace vers le remplissage, l'accélération pendant le déplacement est l'[Accélération de remplissage](acceleration_infill.md). Lorsqu'il se dirige vers la paroi extérieure, l'accélération sera l'[Accélération de la paroi extérieure](acceleration_wall_0.md). De cette façon, il s'approchera effectivement des structures plus sensibles avec un peu plus de précaution que les autres structures.

Ce paramètre est activé par défaut, ce qui permet de contrôler l'accélération pendant les déplacements. C'est une bonne chose dans la plupart des situations, car une accélération accrue du voyage peut faire gagner du temps, tandis qu'une accélération aussi élevée provoquerait des [vibrations](../troubleshooting/ringing.md) lorsqu'elle est utilisée pour l'impression elle-même.

Cependant, il y a deux raisons pour lesquelles vous pourriez vouloir la désactiver :

* Pour modifier le taux d'accélération pour les déplacements, Cura change l'accélération dans les deux sens très souvent. Il passe fréquemment de l'extrusion au déplacement, en particulier avec certains motifs de remplissage et avec les petits détails des murs. Le microprogramme doit traiter ces commandes et peut ne pas être en mesure de suivre les calculs nécessaires. La désactivation des accélérations de déplacement réduit ce problème.
* L'augmentation des accélérations de déplacement fait beaucoup vibrer l'imprimante. Ces vibrations ne sont pas encore tout à fait arrêtées à la fin du déplacement lorsque l'impression doit commencer. Cela peut également entraîner une vibration à la fin d'un déplacement. En désactivant l'accélération du déplacement, la buse s'approchera des structures sensibles de l'impression (comme la paroi extérieure) avec plus de précaution que des structures moins sensibles (comme le remplissage).


