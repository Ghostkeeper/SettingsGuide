Résolution de déplacement maximum
===

Si le modèle a une très haute résolution, Cura réduira la résolution de manière à ce que le processeur de l'imprimante soit capable de suivre le traitement des commandes g-code au fur et à mesure de leur exécution. La résolution maximale des déplacements peut être déterminée séparément de la [résolution maximale](meshfix_maximum_resolution.md) lors de l'impression.

Étant donné que les déplacements sont exécutés beaucoup plus rapidement que les impressions, la tête d'impression parcourra les segments de ligne du déplacement beaucoup plus rapidement que les autres segments de ligne. L'unité centrale devrait traiter ces segments de ligne beaucoup plus rapidement afin de suivre la buse. C'est pourquoi la résolution des mouvements de déplacement devrait être inférieure à celle des mouvements d'extrusion plus lents.

La résolution du mouvement pendant les déplacements n'est souvent pas non plus importante pour la qualité d'impression. Comme il ne s'agit pas d'extrusion, il n'y a pas de surface à rendre floue ou anguleuse. C'est pourquoi la réduction de la résolution des mouvements de déplacement n'a pas d'impact significatif sur la qualité d'impression.

La plupart des déplacements de Cura sont des lignes droites. Ce sont les mouvements les plus rapides et qui produisent le moins de vibrations. Cependant, si Cura doit éviter les collisions, il a tendance à suivre la surface de la surface qu'il essaie d'éviter. Le mouvement de déplacement autour de cette surface aura alors une résolution similaire à celle de la surface qu'il évite. Par conséquent, ce paramètre ne peut avoir un effet réel que si [combing](../travel/retraction_combing.md) est activé.
